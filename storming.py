import numpy as np
import matplotlib as plt
import random

initial_capital = 3000
win_percent = 0.01
loss_percent = 0.01
n_simulations = 400 + 1

sudden_loss_upper = 0.01
sudden_loss_lower = 0.01
sudden_loss_interval = random.randint(20, 40)

sudden_convex_upper = 0.01
sudden_convex_lower = 0.01
sudden_convex_interval = random.randint(35, 45)

def equity_curve_simulation(initial_capital_loc,):