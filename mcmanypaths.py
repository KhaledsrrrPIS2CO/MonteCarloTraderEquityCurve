import numpy as np
import matplotlib.pyplot as plt
import random
import time

# Defining parameters
start_time = time.time()
# initial equity amount of the options trader
initial_equity = 100000
# the percentage loss when a trade is not successful
loss_pct = 0.01
# the percentage gain when a trade is successful
win_pct = 0.01
# the win rate of the trader's trades
win_rate = 0.5
# number of trades to be simulated
n_simulations = 100000
# number of runs or nuber of paths
number_of_runs = 1000

# Sudden loss interval is in the function to generate real random interval
sudden_error_upper = 0.01  # the sudden loss upper rate
sudden_error_lower = 0.01  # the sudden loss  lower rate
# Sudden convex interval is in the function to generate real random interval
convex_payoff_upper = 0.01  # upper bound for the random convex payoff
convex_payoff_lower = 0.01  # lower bound for the random convex payoff


# Defining the simulation function
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
            # Calculate the daily return for a successful trade
            daily_return = equity_counter * win_pct
        else:
            # Calculate the daily return for an unsuccessful trade
            daily_return = -equity_counter * loss_pct

        # Add the daily return and commissions to the equity counter
        equity_counter += daily_return
        equity_counter += commissions

        # Store the equity counter value in the equity array
        equity_array[i] = equity_counter

        # Introduce a random convex payoff with a random frequency
        if i % sudden_convex_interval == 0:
            # Generate a random convex payoff rate
            convex_payoff = np.random.uniform(convex_payoff_lower, convex_payoff_upper)
            # Calculate and add the convex payoff
            convex_payoff_amount = equity_counter * convex_payoff
            # Add the convex payoff  to the equity counter
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
    return equity_array


#  Running the simulation and storing the results
n_runs = number_of_runs
simulation_results = []

for i in range(n_runs):
    result = simulate_equity_curve(initial_equity, loss_pct, win_pct, win_rate, n_simulations)
    simulation_results.append(result)


# Plotting the simulation results:
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


# Add $$$ label for max, avg, min
plt.text(0, min_equity, f'${min_equity:.0f}', fontsize="13")
plt.text(0, max_equity, f'${max_equity:.0f}', fontsize="13")
plt.text(0, avg_equity, f'${avg_equity:.0f}', fontsize="13")


# The probability of being above or below average equity
n_above_avg = np.count_nonzero([result[-1] > avg_equity for result in simulation_results])
p_above_avg = round(n_above_avg / n_runs * 100, 2)
p_below_avg = 100 - p_above_avg
print("Probability of above avg equity :", p_above_avg, "%")
print("Probability of below avg equity :", p_below_avg, "%")


#  The probability of a trader doubling his initial equity after number of simulations
n_doubled = 0
for i in range(n_runs):
    result = simulate_equity_curve(initial_equity, loss_pct, win_pct, win_rate, n_simulations)
    simulation_results.append(result)
    final_equity = result[-1]
    if final_equity >= 2 * initial_equity:
        n_doubled += 1
p_doubled = (n_doubled / n_runs) * 100
print("Probability of doubling initial equity:", p_doubled, "%")


# Std from average. Calculate the variation from the average equity for each simulation
variation_from_avg = [result[-1] - avg_equity for result in simulation_results]
# Calculate the standard deviation of the variation from the average equity
std_dev = np.std(variation_from_avg)
std_dev_round = round(std_dev, 2)
print("σ: One standard deviation of variation from average equity:", std_dev_round)


# plot
plt.title("Monte Carlo Simulation")
plt.ylabel("$$$$$")
plt.xlabel("Num of simulations")
plt.show()


# Time needed for the whole MC simulation
elapsed_time = time.time() - start_time
rounded_time = round(elapsed_time, 2)/60
print("Time elapsed: ", rounded_time, "minutes")

exit()



