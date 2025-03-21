import os
import numpy as np
import matplotlib.pyplot as plt
from izhikevich.single_neuron import run_izhikevich_model, analyze_firing_rate_vs_current
from izhikevich.visualization import visualize_membrane_potential, draw_fi_relationship

IMAGES_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "images")
os.makedirs(IMAGES_DIR, exist_ok=True)

def save_current_plot(filename):
    plt.savefig(os.path.join(IMAGES_DIR, filename), dpi=300, bbox_inches='tight')
    plt.close()

def analyze_parameter_effect(param_name, param_values, base_params, I=10, T=1000, dt=0.1):
    print(f"Analyzing effect of parameter '{param_name}'...")
    
    plt.figure(figsize=(15, 10))
    
    for i, value in enumerate(param_values):
        params = base_params.copy()
        params[param_name] = value
        
        time, v, _, spikes = run_izhikevich_model(
            params['a'], params['b'], params['c'], params['d'], I, T, dt)
        
        plt.subplot(len(param_values), 1, i+1)
        plt.plot(time, v, 'b-', linewidth=1)
        if spikes:
            spike_indices = [np.abs(time - spike_time).argmin() for spike_time in spikes]
            plt.plot(time[spike_indices], v[spike_indices], 'ro', markersize=4)
        
        plt.axhline(y=30, color='r', linestyle='--', alpha=0.3)
        plt.ylabel('V (mV)')
        plt.title(f"{param_name} = {value}")
        
        if i == len(param_values) - 1:
            plt.xlabel('Time (ms)')
    
    plt.tight_layout()
    save_current_plot(f"membrane_potential_{param_name}.png")
    
    plt.figure(figsize=(10, 8))
    
    I_range = np.arange(0, 21, 1)
    
    for value in param_values:
        params = base_params.copy()
        params[param_name] = value
        
        firing_rates = analyze_firing_rate_vs_current(
            params['a'], params['b'], params['c'], params['d'], I_range, T=1000, dt=0.1)
        
        plt.plot(I_range, firing_rates, 'o-', linewidth=2, label=f"{param_name}={value}")
    
    plt.xlabel('Input Current (I)')
    plt.ylabel('Firing Rate (Hz)')
    plt.title(f'F-I Curve with Varying {param_name}')
    plt.grid(True, alpha=0.3)
    plt.legend()
    
    save_current_plot(f"fi_curve_{param_name}.png")
    
    return

def run_parameter_analysis():
    base_params = {'a': 0.02, 'b': 0.2, 'c': -65, 'd': 8}
    
    param_ranges = {
        'a': [0.01, 0.02, 0.05, 0.1],
        'b': [0.1, 0.2, 0.25, 0.3],
        'c': [-75, -65, -55, -45],
        'd': [2, 4, 6, 8]
    }
    
    for param, values in param_ranges.items():
        analyze_parameter_effect(param, values, base_params)

if __name__ == "__main__":
    run_parameter_analysis()
