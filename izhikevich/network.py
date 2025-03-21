"""Simulates 1000 interconnected neurons (800 excitatory, 200 inhibitory).
"""

import numpy as np
import time


def run_network_simulation(T=1000, dt=1.0, seed=None, verbose=False):
    if seed is not None:
        np.random.seed(seed)
    
    Ne = 400
    Ni = 100
    N = Ne + Ni
    
    if verbose:
        print(f"Network simulation with {Ne} excitatory and {Ni} inhibitory neurons")
    
    n_steps = int(T / dt)
    
    random_e = np.random.rand(Ne)
    a_e = 0.02 * np.ones(Ne)
    b_e = 0.2 * np.ones(Ne)
    c_e = -65 + 15 * (random_e**2)
    d_e = 8 - 6 * (random_e**2)
    
    random_i = np.random.rand(Ni)
    a_i = 0.02 + 0.08 * random_i
    b_i = 0.25 - 0.05 * random_i
    c_i = -65 * np.ones(Ni)
    d_i = 2 * np.ones(Ni)
    
    a = np.concatenate((a_e, a_i))
    b = np.concatenate((b_e, b_i))
    c = np.concatenate((c_e, c_i))
    d = np.concatenate((d_e, d_i))
    
    v = -65 * np.ones(N)  
    u = b * v 
    
    if verbose:
        print("Creating synaptic matrix...")
    start_time = time.time()
    S = build_connection_matrix(Ne, Ni, verbose)
    if verbose:
        print(f"Synaptic matrix created in {time.time() - start_time:.2f} seconds")

    spike_times = []
    spike_indices = []
    
    report_interval = max(1, n_steps // 10)
    
    if verbose:
        print(f"Starting simulation for {n_steps} steps...")
    
    sim_start = time.time()
    for t in range(n_steps):
        if verbose and t % report_interval == 0:
            progress = t / n_steps * 100
            elapsed = time.time() - sim_start
            print(f"Progress: {progress:.1f}% (Step {t}/{n_steps}, Time: {elapsed:.1f}s)")
        
        I = np.zeros(N)
        I[:Ne] = 5 * np.random.randn(Ne)  
        I[Ne:] = 2 * np.random.randn(Ni) 
        
        fired = np.where(v >= 30)[0]
        
        if len(fired) > 0:
            spike_times.extend([t * dt] * len(fired))
            spike_indices.extend(fired.tolist())
            
            v[fired] = c[fired]
            u[fired] += d[fired]
            
            I += np.sum(S[:, fired], axis=1)
        
        dv = (0.04 * v**2 + 5 * v + 140 - u + I) * dt
        du = (a * (b * v - u)) * dt
        
        v += dv
        u += du
    
    if verbose:
        total_time = time.time() - sim_start
        print(f"Simulation completed in {total_time:.2f} seconds with {len(spike_times)} spikes")
    
    return spike_times, spike_indices


def build_connection_matrix(Ne=800, Ni=200, verbose=False):
    N = Ne + Ni
    
    if verbose:
        print(f"Creating {N}x{N} synaptic matrix...")
    
    connection_prob = 0.1
    
    S = np.zeros((N, N))
    
    connect_mask = np.random.rand(N, N) < connection_prob
    
    S[:, :Ne] = 0.5 * np.random.rand(N, Ne) * connect_mask[:, :Ne]
    S[:, Ne:] = -1.0 * np.random.rand(N, Ni) * connect_mask[:, Ne:]
    
    if verbose:
        total_connections = np.sum(connect_mask)
        print(f"Created matrix with {total_connections} connections ({connection_prob*100:.1f}% density)")
    
    return S