"""Single Izhikevich neuron simulation.
"""

import numpy as np


def run_izhikevich_model(a, b, c, d, I, T, dt, noise_std=0):
    #number of time steps
    n_steps = int(T / dt)
    
    time = np.arange(0, T, dt)
    v = np.zeros(n_steps)
    u = np.zeros(n_steps)
    
    v[0] = -65.0 
    u[0] = b * v[0] 
    spike_times = []
    
    if np.isscalar(I):
        I = I * np.ones(n_steps)
    
    for i in range(1, n_steps):
        #noise
        I_noisy = I[i-1] + noise_std * np.random.randn() if noise_std > 0 else I[i-1]
        
        dv = (0.04 * v[i-1]**2 + 5 * v[i-1] + 140 - u[i-1] + I_noisy) * dt
        du = (a * (b * v[i-1] - u[i-1])) * dt
        
        v[i] = v[i-1] + dv
        u[i] = u[i-1] + du
        
        #spike and reset ?
        if v[i] >= 30:
            spike_times.append(time[i])
            v[i] = c
            u[i] += d
    
    return time, v, u, spike_times


def analyze_firing_rate_vs_current(a, b, c, d, I_range, T=1000, dt=0.1, noise_std=0, discard_time=200):
    firing_rates = np.zeros_like(I_range, dtype=float)
    
    for i, I in enumerate(I_range):
        _, _, _, spike_times = run_izhikevich_model(a, b, c, d, I, T, dt, noise_std)
        
        valid_spikes = [t for t in spike_times if t >= discard_time]
        
        if len(valid_spikes) > 0:
            firing_rates[i] = len(valid_spikes) / ((T - discard_time) / 1000)
    
    return firing_rates