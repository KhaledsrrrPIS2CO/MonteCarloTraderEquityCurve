import numpy as np
import matplotlib.pyplot as plt
import random
import time

# Define the parameters
start_time = time.time()
# initial equity amount of the options trader
initial_equity = 3000
# the percentage loss when a trade is not successful
loss_pct = 0.01
# the percentage gain when a trade is successful
win_pct = 0.03
# the win rate of the trader's trades
win_rate = 0.41
# number of trades to be simulated
n_simulations = 400
# number of runs or nuber of paths
number_of_runs = 100000

# the sudden loss interval is in the function to generate real random interval
sudden_error_upper = 0.01  # the sudden loss upper rate
sudden_error_lower = 0.01  # the sudden loss  lower rate
# the sudden convex interval is in the function to generate real random interval
convex_payoff_upper = 0.15  # upper bound for the random convex payoff
convex_payoff_lower = 0.05  # lower bound for the random convex payoff


# Define the simulation function to calculate the equity curve of the options trader
def simulate_equity_curve(initial_equity_loc, loss_pct_loc, win_pct_loc, win_rate_loc, n_simulations_loc):
    equity_array = np.zeros((n_simulations_loc,))  # Initialize an array to store the equity value at each trade
    equity_array[0] = initial_equity_loc  # Set the initial equity value
    equity_counter = initial_equity_loc  # Set the initial value for the equity counter
    commissions = -4  # Set the fixed value for commissions
    sudden_loss_interval = random.randint(20, 40)  # the sudden loss interval
    sudden_convex_interval = random.randint(40, 80)  # the sudden convex interval

    #  Loop through the number of trades to be simulated
    for i in range(1, n_simulations_loc):
        # n: the number of Bernoulli trials,
        # p: the probability of success in each trial
        win = np.random.binomial(1, win_rate_loc, 1)

        if win:
            # If the trade was successful, calculate the daily return
            daily_return = equity_counter * win_pct_loc
            # Add  the daily return and commissions to the equity counter
            equity_counter += daily_return
            equity_counter += commissions
        else:
            # If the trade was not successful, calculate the daily loss
            daily_return = -equity_counter * loss_pct_loc
            # Add the daily loss and commissions to the equity counter
            equity_counter += daily_return
            equity_counter += commissions

        # Store the equity counter value in the equity array
        equity_array[i] = equity_counter

        # Introduce a random convex payoff with a random frequency
        if i % sudden_convex_interval == 0:
            # Generate a random convex payoff rate
            convex_payoff = np.random.uniform(convex_payoff_lower, convex_payoff_upper)
            # Calculate the convex payoff
            convex_payoff_amount = equity_counter * convex_payoff
            equity_counter += convex_payoff_amount

        # Introduce the sudden loss of a random percentage between 5% and 10% with any desired frequency
        if i % sudden_loss_interval == 0:
            # Generate a random percentage loss between 5% and 10%
            sudden_loss_pct = np.random.uniform(sudden_error_upper, sudden_error_lower)
            # Calculate the sudden loss
            sudden_loss = -equity_counter * sudden_loss_pct
            # Add the sudden loss to the equity counter
            equity_counter += sudden_loss

        if equity_counter <= 0:
            break

    # Return the final equity array
    return equity_array


n_runs = number_of_runs   # number of runs for simulations
simulation_results = []

for i in range(n_runs):
    result = simulate_equity_curve(initial_equity, loss_pct, win_pct, win_rate, n_simulations)
    simulation_results.append(result)

# Plot all the simulations on one graph
plt.figure(figsize=(7, 7))
for i in range(n_runs):
    plt.plot(simulation_results[i], color=plt.cm.cool(i / n_runs), label="")

# Calculate the minimum and maximum equity values across all simulations
min_equity = np.min([result[-1] for result in simulation_results])
max_equity = np.max([result[-1] for result in simulation_results])
avg_equity = np.average([result[-1] for result in simulation_results])
print("Min equity:", round(min_equity, 2), "\nAvg equity: ", round(avg_equity, 2)
      , "\nMax equity: ", round(max_equity, 2), )
print("\nNumber of paths:", n_runs)

# Plot the minimum and maximum equity values
plt.plot([0, n_simulations-1], [max_equity, max_equity], color='green', label="max")
plt.plot([0, n_simulations-1], [avg_equity, avg_equity], color='blue', label="avg")
plt.plot([0, n_simulations-1], [min_equity, min_equity], color='red', label="min")

# Add text label for max, avg, min
plt.text(0, min_equity, f'${min_equity:.0f}', fontsize="12")
plt.text(0, max_equity, f'${max_equity:.0f}', fontsize="12")
plt.text(0, avg_equity, f'${avg_equity:.0f}', fontsize="12")

# probability of being above or below average equity
n_above_avg = np.count_nonzero([result[-1] > avg_equity for result in simulation_results])
p_above_avg = round(n_above_avg / n_runs * 100, 2)
p_below_avg = 100 - p_above_avg
print("Above avg equity probability:", p_above_avg, "%")
print("Below avg equity probability:", p_below_avg, "%")

# plot
plt.legend()
plt.title("Monte Carlo Simulation")
plt.ylabel("$$$$$")
plt.xlabel("Num of simulations")
plt.show()

# Time needed for the whole MC simulation
elapsed_time = time.time() - start_time
rounded_time = round(elapsed_time, 2)
print("Time elapsed: ", rounded_time, "seconds")

exit()



