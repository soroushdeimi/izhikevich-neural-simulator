# Izhikevich Neuron Parameter Behavior Summary
## Parameter Effects

### Parameter a (0.01 - 0.1)
- **Function**: Controls the time scale of recovery variable u
- **Effect**: Determines how quickly the neuron recovers after firing
- **Lower values**: Slower recovery, longer interspike intervals
- **Higher values**: Faster recovery, can transition from regular spiking to fast spiking

### Parameter b (0.1 - 0.3)
- **Function**: Controls sensitivity of recovery variable u to membrane potential v
- **Effect**: Influences subthreshold dynamics and resonance
- **Lower values**: Weaker coupling between v and u, more independent dynamics
- **Higher values**: Stronger coupling, more responsive to changes in membrane potential

### Parameter c (-75 to -45)
- **Function**: After-spike reset value of membrane potential v
- **Effect**: Determines post-spike hyperpolarization depth
- **More negative values**: Deeper hyperpolarization, longer refractory periods
- **Less negative values**: Reduced hyperpolarization, can lead to bursting

### Parameter d (2 - 8)
- **Function**: After-spike reset of recovery variable u
- **Effect**: Controls spike frequency adaptation
- **Lower values**: Less adaptation, more consistent firing (tonic spiking)
- **Higher values**: Stronger adaptation, firing rate decreases during sustained input

## Key Neuronal Behaviors

Different parameter combinations produce distinct firing patterns:

| Behavior Type | a | b | c | d | Characteristics |
|---------------|---|---|---|---|-----------------|
| Regular Spiking | 0.02 | 0.2 | -65 | 8 | Moderate adaptation, regular firing |
| Fast Spiking | 0.1 | 0.2 | -65 | 2 | Little adaptation, high firing rate |
| Intrinsically Bursting | 0.02 | 0.2 | -55 | 4 | Initial burst followed by regular spikes |
| Chattering | 0.02 | 0.2 | -50 | 2 | Rhythmic bursting with high-frequency spikes |
| Low-threshold Spiking | 0.02 | 0.25 | -65 | 2 | Can fire at very low input currents |
| Resonator | 0.1 | 0.26 | -65 | 2 | Responds preferentially to specific input frequencies |

This summary highlights the flexibility of the Izhikevich model in reproducing diverse neuronal behaviors with simple parameter adjustments.
