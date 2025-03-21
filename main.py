import matplotlib.pyplot as plt
import time
from examples.single_neuron_example import demonstrate_single_neuron
from examples.network_example import demonstrate_network


def main():
    print("Izhikevich Neural Simulator")
    print("=========================\n")
    
    print("\nSingle Neuron Simulation")
    print("---------------------------------")
    start_time = time.time()
    demonstrate_single_neuron()
    print(f"Single neuron simulation completed in {time.time() - start_time:.2f} seconds")
    
    print("\nNetwork Simulation")
    print("---------------------------")
    start_time = time.time()
    demonstrate_network()
    print(f"Network simulation completed in {time.time() - start_time:.2f} seconds")


if __name__ == "__main__":
    try:
        main()
        print("done")
    except Exception as e:
        print(f"Error encountered: {e}")
        import traceback
        traceback.print_exc()