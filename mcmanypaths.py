import numpy as np
import matplotlib.pyplot as plt
import random

# Define the parameters
initial_equity = 3000  # initial equity amount of the options trader
loss_pct = 0.01  # the percentage loss when a trade is not successful
win_pct = 0.0116  # the percentage gain when a trade is successful
win_rate = 0.5  # the win rate of the trader's trades
n_simulations = 400 + 1  # number of trades to be simulated

sudden_error_upper = 0.01  # the sudden loss upper rate
sudden_error_lower = 0.01  # the sudden loss  lower rate
sudden_loss_interval = random.randint(20, 40)  # the sudden loss interval

convex_payoff_upper = 0.01  # upper bound for the random convex payoff
convex_payoff_lower = 0.01  # lower bound for the random convex payoff
sudden_convex_interval = random.randint(30, 40)  # the sudden loss interval


# Define the simulation function to calculate the equity curve of the options trader
def simulate_equity_curve(initial_equity_loc, loss_pct_loc, win_pct_loc, win_rate_loc, n_simulations_loc):
    # Initialize an array to store the equity value at each trade
    equity_array = np.zeros((n_simulations_loc,))
    # Set the initial equity value
    equity_array[0] = initial_equity_loc
    # Set the initial value for the equity counter
    equity_counter = initial_equity_loc
    # Set the fixed value for commissions
    commissions = -4

    #  Loop through the number of trades to be simulated
    for i in range(1, n_simulations_loc):
        # Check if the trade was successful, using binomial distribution takes three arguments:
        # (n, p, size=None),
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

            print(i, ":", "CCCCCCCCCCCCCCCCC|| Random convex payoff ", "{:.2f}".format(convex_payoff_amount),
                  " ({:.2f}%)".format(convex_payoff * 100), " at trade ", i)

        # Introduce the sudden loss of a random percentage between 5% and 10% with any desired frequency
        if i % sudden_loss_interval == 0:
            # Generate a random percentage loss between 5% and 10%
            sudden_loss_pct = np.random.uniform(sudden_error_upper, sudden_error_lower)
            # Calculate the sudden loss
            sudden_loss = -equity_counter * sudden_loss_pct
            # Add the sudden loss to the equity counter
            equity_counter += sudden_loss

            print(i, ":", "LLLLLLLLLLLLLLLLLL||Sudden Loss of ", "{:.2f}".format(sudden_loss),
                  " ({:.2f}%)".format(sudden_loss_pct * 100), " at trade ", i)

        print(i, ":", "||Daily PnL:", "{:.2f}".format(daily_return), "||   Equity:", "{:.2f}".format(equity_counter))
        if equity_counter <= 0:
            print("GAME OVER,  U R bust in less than ", i, "trades")
            break
    # Return the final equity array
    return equity_array

n_runs = 10  # number of runs for simulations
simulation_results = []

for i in range(n_runs):
    result = simulate_equity_curve(initial_equity, loss_pct, win_pct, win_rate, n_simulations)
    simulation_results.append(result)

# Plot all the simulations on one graph
plt.figure(figsize=(10, 6))
for i in range(n_runs):
    plt.plot(simulation_results[i], color=plt.cm.cool(i / n_runs), label=f"Simulation {i + 1}")
plt.legend()
plt.show()


#  Run the simulation by calling the simulate_equity_curve function
equity = simulate_equity_curve(initial_equity, loss_pct, win_pct, win_rate, n_simulations)





