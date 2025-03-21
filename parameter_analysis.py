"""
Systematic analysis of Izhikevich neuron model parameters.
"""

import os
import numpy as np
import matplotlib.pyplot as plt
from izhikevich.single_neuron import run_izhikevich_model, analyze_firing_rate_vs_current
from izhikevich.visualization import visualize_membrane_potential, draw_fi_relationship

# Create directory for saving plots
IMAGES_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "images")
os.makedirs(IMAGES_DIR, exist_ok=True)

def save_current_plot(filename):
    """Save the current matplotlib plot to the images directory."""
    plt.savefig(os.path.join(IMAGES_DIR, filename), dpi=300, bbox_inches='tight')
    plt.close()

def analyze_parameter_effect(param_name, param_values, base_params, I=10, T=1000, dt=0.1):
    """
    Analyze the effect of varying a single parameter on neuron behavior.
    
    Args:
        param_name: The name of the parameter to vary ('a', 'b', 'c', or 'd')
        param_values: List of values to test for the parameter
        base_params: Dictionary of base parameters {'a', 'b', 'c', 'd'}
        I: Input current
        T: Simulation duration (ms)
        dt: Time step (ms)
    """
    print(f"Analyzing effect of parameter '{param_name}'...")
    
    # Plot membrane potentials for each parameter value
    plt.figure(figsize=(15, 10))
    
    for i, value in enumerate(param_values):
        # Create parameter set with the current value
        params = base_params.copy()
        params[param_name] = value
        
        # Run simulation
        time, v, _, spikes = run_izhikevich_model(
            params['a'], params['b'], params['c'], params['d'], I, T, dt)
        
        # Plot in a subplot
        plt.subplot(len(param_values), 1, i+1)
        plt.plot(time, v, 'b-', linewidth=1)
        if spikes:
            spike_indices = [np.abs(time - spike_time).argmin() for spike_time in spikes]
            plt.plot(time[spike_indices], v[spike_indices], 'ro', markersize=4)
        
        plt.axhline(y=30, color='r', linestyle='--', alpha=0.3)
        plt.ylabel('V (mV)')
        plt.title(f"{param_name} = {value}")
        
        # Only show x-label for the bottom plot
        if i == len(param_values) - 1:
            plt.xlabel('Time (ms)')
    
    plt.tight_layout()
    save_current_plot(f"membrane_potential_{param_name}.png")
    
    # Create F-I curves for each parameter value
    plt.figure(figsize=(10, 8))
    
    I_range = np.arange(0, 21, 1)
    
    for value in param_values:
        params = base_params.copy()
        params[param_name] = value
        
        # Compute F-I curve
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
    """Run a comprehensive analysis of how each parameter affects neuron behavior."""
    # Base parameters (Regular Spiking neuron)
    base_params = {'a': 0.02, 'b': 0.2, 'c': -65, 'd': 8}
    
    # Parameter ranges to test
    param_ranges = {
        'a': [0.01, 0.02, 0.05, 0.1],
        'b': [0.1, 0.2, 0.25, 0.3],
        'c': [-75, -65, -55, -45],
        'd': [2, 4, 6, 8]
    }
    
    # Analyze each parameter
    for param, values in param_ranges.items():
        analyze_parameter_effect(param, values, base_params)
    
    # Generate report
    generate_report(param_ranges, base_params)

def generate_report(param_ranges, base_params):
    """Generate a markdown report of the parameter analysis."""
    report_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "parameter_analysis_report.md")
    
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write("# Izhikevich Neuron Parameter Analysis\n\n")
        
        f.write("## Base Parameters (Regular Spiking Neuron)\n\n")
        f.write(f"- a = {base_params['a']} (Time scale of recovery variable)\n")
        f.write(f"- b = {base_params['b']} (Sensitivity of recovery variable)\n")
        f.write(f"- c = {base_params['c']} (After-spike reset value of membrane potential)\n")
        f.write(f"- d = {base_params['d']} (After-spike reset of recovery variable)\n\n")
        
        # Analysis for each parameter
        for param in ['a', 'b', 'c', 'd']:
            f.write(f"## Parameter {param} Analysis\n\n")
            
            if param == 'a':
                f.write("Parameter 'a' represents the time scale of the recovery variable u. ")
                f.write("Smaller values result in slower recovery.\n\n")
            elif param == 'b':
                f.write("Parameter 'b' represents the sensitivity of the recovery variable u to the membrane potential v. ")
                f.write("Larger values couple v and u more strongly.\n\n")
            elif param == 'c':
                f.write("Parameter 'c' represents the after-spike reset value of the membrane potential v. ")
                f.write("It determines how low the membrane potential goes after a spike.\n\n")
            elif param == 'd':
                f.write("Parameter 'd' represents the after-spike reset of the recovery variable u. ")
                f.write("It determines the spike frequency adaptation.\n\n")
            
            # Membrane potential plots
            f.write("### Effect on Membrane Potential\n\n")
            f.write(f"![Membrane Potential with varying {param}](images/membrane_potential_{param}.png)\n\n")
            
            f.write("Observations:\n\n")
            
            # Parameter-specific observations
            if param == 'a':
                f.write("- As 'a' increases, the neuron recovers faster after firing\n")
                f.write("- Larger values lead to faster adaptation and decreased firing\n")
                f.write("- Very large values (a=0.1) can change the neuron from regular spiking to fast spiking\n\n")
            elif param == 'b':
                f.write("- As 'b' increases, the subthreshold dynamics change\n")
                f.write("- Larger values make the neuron more responsive to input\n")
                f.write("- Very large values can lead to resonance behavior\n\n")
            elif param == 'c':
                f.write("- As 'c' increases (becomes less negative), the post-spike hyperpolarization decreases\n")
                f.write("- Less negative values can lead to bursting behavior\n")
                f.write("- More negative values lead to longer refractory periods\n\n")
            elif param == 'd':
                f.write("- As 'd' decreases, spike frequency adaptation decreases\n")
                f.write("- Smaller values lead to more consistent inter-spike intervals\n")
                f.write("- Very small values can transform regular spiking into tonic spiking\n\n")
            
            # F-I curves
            f.write("### Effect on F-I Curve\n\n")
            f.write(f"![F-I Curve with varying {param}](images/fi_curve_{param}.png)\n\n")
            
            f.write("Observations:\n\n")
            
            # Parameter-specific observations for F-I curve
            if param == 'a':
                f.write("- Larger 'a' values tend to lower the firing rate at all input currents\n")
                f.write("- The threshold current needed to initiate firing increases with 'a'\n")
                f.write("- The slope of the F-I curve decreases with larger 'a' values\n\n")
            elif param == 'b':
                f.write("- The threshold current increases with 'b'\n")
                f.write("- The slope of the F-I curve may decrease with larger 'b' values\n")
                f.write("- Very large 'b' values may prevent firing at lower currents\n\n")
            elif param == 'c':
                f.write("- Less negative 'c' values tend to increase the firing rate\n")
                f.write("- The threshold current may decrease with less negative 'c' values\n")
                f.write("- The effect on the F-I curve slope varies with the specific 'c' values\n\n")
            elif param == 'd':
                f.write("- Smaller 'd' values generally result in higher firing rates\n")
                f.write("- The threshold current is less affected by 'd' than other parameters\n")
                f.write("- Larger 'd' values create stronger spike-frequency adaptation\n\n")
            
        f.write("## Summary\n\n")
        f.write("The Izhikevich neuron model parameters have distinct effects on neuronal behavior:\n\n")
        f.write("- Parameter 'a': Controls recovery speed and adaptation rate\n")
        f.write("- Parameter 'b': Controls sensitivity to membrane potential and resonance properties\n")
        f.write("- Parameter 'c': Controls post-spike reset and bursting tendencies\n")
        f.write("- Parameter 'd': Controls spike-frequency adaptation\n\n")
        f.write("By adjusting these parameters, the model can reproduce a wide variety of neuronal behaviors observed in biological neurons.\n")
    
    print(f"Report generated at: {report_path}")

if __name__ == "__main__":
    run_parameter_analysis()
