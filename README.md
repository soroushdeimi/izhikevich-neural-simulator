# Izhikevich Neural Simulator

A Python project that simulates spiking neurons using the Izhikevich model. This project provides tools for both single neuron simulation and network simulation with customizable parameters.

## About the Izhikevich Model

The Izhikevich model is a computationally efficient model for simulating spiking neurons. It uses a system of two differential equations:

- dv/dt = 0.04v² + 5v + 140 - u + I
- du/dt = a(bv - u)

When v ≥ 30 mV, a spike occurs and the variables are reset:
- v ← c
- u ← u + d

Where:
- v: membrane potential
- u: recovery variable
- I: input current
- a, b, c, d: parameters that can be adjusted to produce different firing patterns

## Features

### Part 1: Single Neuron Simulation
- Implementation of the Izhikevich neuron model
- Customizable neuron parameters (a, b, c, d)
- Optional noise addition to input current
- F-I curve computation and visualization
- Membrane potential visualization

### Part 2: Network Simulation
- Simulation of 1000 neurons (800 excitatory, 200 inhibitory)
- Random parameter generation for biologically plausible diversity
- Synaptic connectivity with weight matrix
- Raster plot visualization of network activity
