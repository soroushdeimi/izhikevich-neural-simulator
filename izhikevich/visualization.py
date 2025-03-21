"""membrane potentials, F-I curves, and raster plots.
"""

import numpy as np
import matplotlib.pyplot as plt


def visualize_membrane_potential(time, v, spike_times, title="Izhikevich Neuron Membrane Potential"):
    plt.figure(figsize=(12, 6))
    plt.plot(time, v, 'b-', linewidth=1.5)
    if spike_times:
        spike_indices = [np.abs(time - spike_time).argmin() for spike_time in spike_times]
        plt.plot(time[spike_indices], v[spike_indices], 'ro', markersize=6)
    
    plt.axhline(y=30, color='r', linestyle='--', alpha=0.5, label='Spike Threshold (30 mV)')
    plt.xlabel('Time (ms)', fontsize=12)
    plt.ylabel('Membrane Potential (mV)', fontsize=12)
    plt.title(title, fontsize=14)
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.tight_layout()


def draw_fi_relationship(I_range, firing_rates, title="F-I Curve"):
    plt.figure(figsize=(10, 6))
    plt.plot(I_range, firing_rates, 'bo-', linewidth=2)
    plt.xlabel('Input Current (I)', fontsize=12)
    plt.ylabel('Firing Rate (Hz)', fontsize=12)
    plt.title(title, fontsize=14)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()


def generate_spike_raster(spike_times, spike_indices, T, Ne=800, title="Network Raster Plot"):
    plt.figure(figsize=(14, 8))
    
    #excitatory neurons
    exc_mask = np.array(spike_indices) < Ne
    if np.any(exc_mask):
        plt.plot(np.array(spike_times)[exc_mask], 
                 np.array(spike_indices)[exc_mask], 
                 'b.', markersize=2, alpha=0.5, label='Excitatory')
    
    #inhibitory neurons
    inh_mask = np.array(spike_indices) >= Ne
    if np.any(inh_mask):
        plt.plot(np.array(spike_times)[inh_mask], 
                 np.array(spike_indices)[inh_mask], 
                 'r.', markersize=2, alpha=0.5, label='Inhibitory')
    
    plt.xlabel('Time (ms)', fontsize=12)
    plt.ylabel('Neuron Index', fontsize=12)
    plt.title(title, fontsize=14)
    plt.xlim(0, T)
    plt.ylim(0, Ne + 200)
    plt.axhline(y=Ne-0.5, color='k', linestyle='--', alpha=0.3)
    
    plt.legend()
    plt.tight_layout()