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
num_of_runs = 1000

sudden_error_interval_lower = random.randint(40)
sudden_error_interval_upper = random.randint(80)
sudden_error_rate_lower = 0.01
sudden_error_rate_upper = 0.01

sudden_convex_interval_lower = random.randint(40)
sudden_convex_interval_upper = random.randint(80)
sudden_convex_payoff_rate_lower = 0.01
sudden_convex_payoff_rate_upper = 0.01

# Define the simulation fun
def simulate_equity_curve(initial_equity, win_rate, win_pct, loss_pct, n_simulations):
    equity_array = np.zeros(n_simulations)
    equity_array[0] = initial_equity
    equity_counter = initial_equity
    commissions = -4
    sudden_error_interval = random.randint(sudden_error_interval_lower, sudden_error_interval_upper)
    sudden_convex_interval = random.randint(sudden_convex_interval_lower, sudden_convex_interval_upper)

    for i in range (1, n_simulations):
        win = np.random.binomial(1, win_rate, 1)

        if win:
            daily_return = equity_counter * win_pct
        else:
            daily_return = equity_counter * loss_pct

        equity_counter += daily_return
        equity_counter += commissions

        if i %  sudden_convex_interval == 0:
            sudden_convex_payoff_rate = np.random.uniform(sudden_convex_payoff_rate_lower, sudden_convex_interval_upper)
            sudden_convex_payoff_amount = equity_counter * sudden_convex_payoff_rate
            equity_counter += sudden_convex_payoff_amount

        if i % sudden_error_interval == 0:
            sudden_error_rate = np.random.uniform(sudden_error_rate_lower,sudden_error_rate_upper)
            sudden_error_amount = equity_counter * sudden_error_rate
            equity_counter += sudden_error_amount

        if equity_counter <= 0:
            break
        return equity_array


n_runs = num_of_runs
simulations_results = []








