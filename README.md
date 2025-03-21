# Izhikevich Neural Simulator

Hey there! This is a Python project I built for simulating spiking neurons using the Izhikevich model. Whether you're looking to simulate a single neuron or an entire network, this toolkit has you covered with plenty of customization options.

## About the Izhikevich Model

So what's this Izhikevich model all about? It's basically a super efficient way to simulate how neurons fire. The math isn't too complicated - just two differential equations:

```math
\frac{dv}{dt} = 0.04v^2 + 5v + 140 - u + I
```
```math
\frac{du}{dt} = a(bv - u)
```

When the membrane potential (v) hits 30 mV, we get a spike and reset things:
```
v ← c
u ← u + d
```

The variables are pretty straightforward:
- **v**: membrane potential (the voltage across the cell membrane)
- **u**: recovery variable (accounts for ion channel dynamics)
- **I**: input current (stimulus)
- **a, b, c, d**: parameters you can tweak to get different firing patterns

## Features

### Part 1: Single Neuron Simulation
- Implementation of the Izhikevich neuron model
- Fully customizable neuron parameters (a, b, c, d)
- Add some noise to the input current if you want to make things more realistic
- Compute and visualize F-I curves (firing rate vs. input current)
- Plot membrane potential over time to see how neurons respond

### Part 2: Network Simulation
- Simulate a network of 1000 neurons (800 excitatory, 200 inhibitory)
- Generate random parameters to create diverse, biologically plausible neurons
- Connect neurons with a synaptic weight matrix
- Visualize network activity with raster plots

## Installation

Getting started is pretty simple:

```bash
# Clone the repository
git clone https://github.com/yourusername/izhikevich-neural-simulator.git
cd izhikevich-neural-simulator

# Create and activate a virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## Usage

Here's a quick example to get you started with a single neuron:

```python
# Example usage for single neuron simulation
from izhikevich_neural_simulator import SingleNeuron

# Create a regular spiking neuron
neuron = SingleNeuron(a=0.02, b=0.2, c=-65, d=8)

# Simulate with constant input current
result = neuron.simulate(T=100, I=10)

# Plot the results
neuron.plot_membrane_potential(result)
```

## Examples

### Different Neuron Types

One of the coolest things about the Izhikevich model is that you can simulate different types of neurons just by tweaking a few parameters:

| Neuron Type | a | b | c | d |
|-------------|---|---|---|---|
| Regular Spiking | 0.02 | 0.2 | -65 | 8 |
| Fast Spiking | 0.1 | 0.2 | -65 | 2 |
| Chattering | 0.02 | 0.2 | -50 | 2 |
| Low-Threshold Spiking | 0.02 | 0.25 | -65 | 2 |

### Network Simulation Example

Simulating a network is just as straightforward:

```python
from izhikevich_neural_simulator import NeuralNetwork

# Create a network of 1000 neurons
network = NeuralNetwork(num_neurons=1000, exc_ratio=0.8)

# Simulate for 1000ms
spikes = network.simulate(T=1000)

# Visualize spike raster plot
network.plot_raster(spikes)
```

## Contributing

Found a bug? Have a cool idea? Contributions are always welcome!

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/awesome-idea`)
3. Commit your changes (`git commit -m 'Add some awesome feature'`)
4. Push to the branch (`git push origin feature/awesome-idea`)
5. Open a Pull Request
