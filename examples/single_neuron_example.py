import numpy as np
import matplotlib.pyplot as plt
from izhikevich.single_neuron import run_izhikevich_model, analyze_firing_rate_vs_current
from izhikevich.visualization import visualize_membrane_potential, draw_fi_relationship


def demonstrate_single_neuron():
    print("Simulating regular spiking neuron...")
    a, b, c, d = 0.02, 0.2, -65, 8
    I = 10 
    T = 1000 
    dt = 0.1 
    
    time, v, u, spikes = run_izhikevich_model(a, b, c, d, I, T, dt)
    
    visualize_membrane_potential(time, v, spikes, title="Regular Spiking Neuron (a=0.02, b=0.2, c=-65, d=8)")
    
    print("Computing F-I curve...")
    I_range = np.arange(0, 21, 1)
    firing_rates = analyze_firing_rate_vs_current(a, b, c, d, I_range, T=1000, dt=0.1)
    
    draw_fi_relationship(I_range, firing_rates, title="F-I Curve for Regular Spiking Neuron")
    
    print("Simulating with noise...")
    time_noisy, v_noisy, u_noisy, spikes_noisy = run_izhikevich_model(a, b, c, d, I, T, dt, noise_std=1.0)
    
    visualize_membrane_potential(time_noisy, v_noisy, spikes_noisy, 
                 title="Regular Spiking Neuron with Noise (noise_std=1.0)")
    
    print("Simulating fast spiking neuron...")
    a_fs, b_fs, c_fs, d_fs = 0.1, 0.2, -65, 2
    time_fs, v_fs, u_fs, spikes_fs = run_izhikevich_model(a_fs, b_fs, c_fs, d_fs, I, T, dt)
    
    visualize_membrane_potential(time_fs, v_fs, spikes_fs, 
                 title="Fast Spiking Neuron (a=0.1, b=0.2, c=-65, d=2)")
    
    plt.show()


if __name__ == "__main__":
    demonstrate_single_neuron()