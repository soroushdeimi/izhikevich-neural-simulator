"""Network simulation example.
"""

import matplotlib.pyplot as plt
import time
from izhikevich.network import run_network_simulation
from izhikevich.visualization import generate_spike_raster


def demonstrate_network():
    """Runs a network simulation example."""
    print("Simulating network of 1000 Izhikevich neurons...")
    
    T = 500
    dt = 2.0
    
    start_time = time.time()
    print(f"Starting network simulation with T={T}, dt={dt}")
    
    spike_times, spike_indices = run_network_simulation(T, dt, seed=42, verbose=True)
    
    sim_time = time.time() - start_time
    print(f"Simulation complete in {sim_time:.2f} seconds. Recorded {len(spike_times)} spikes.")
    
    generate_spike_raster(spike_times, spike_indices, T)
    
    if spike_times:
        total_spikes = len(spike_times)
        average_rate = total_spikes / (T/1000 * 1000)  
        print(f"Average firing rate: {average_rate:.2f} Hz per neuron")
    
    plt.show()


if __name__ == "__main__":
    demonstrate_network()