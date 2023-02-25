import random

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time

# define parameters
start_time = time.time()
initial_equity = 3000
win_rate = 0.5
win_pct = 0.01
loss_pct = 0.005
n_simulations = 400
n_runs = 1000

sudden_error_lower = 0.01
sudden_error_upper = 0.01

sudden_convex_lower = 0.01
sudden_convex_upper = 0.01

# Define the simulation fun
def simulate_equity_curve(initial_equity, win_rate, win_pct, loss_pct, n_simulations):
    equity_array = np.zeros(n_simulations)
    equity_array[0] = initial_equity
    equity_counter = initial_equity
    commissions = -4




