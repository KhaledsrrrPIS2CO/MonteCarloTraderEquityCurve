import numpy as np
import matplotlib.pyplot as plt

# Define the parameters
initial_equity = 1000  # initial equity amount of the options trader
loss_pct = 0.01  # the percentage loss when a trade is not successful
win_pct = 0.015  # the percentage gain when a trade is successful
win_rate = 0.6  # the win rate of the trader's trades
n_simulations = 50  # number of trades to be simulated
sudden_error = 0.1  # the sudden loss rate
sudden_loss_interval = 40  # the sudden loss interval
convex_payoff_lower = 1.5  # lower bound for the random convex payoff
convex_payoff_upper = 1.0  # upper bound for the random convex payoff
frequency_lower = 0.2  # lower bound for the random frequency of the convex payoff
frequency_upper = 0.4  # upper bound for the random frequency of the convex payoff

# Define the simulation function to calculate the equity curve of the options trader
def simulate_equity_curve(initial_equity, loss_pct, win_pct, win_rate, n_simulations, sudden_error, convex_payoff_lower, convex_payoff_upper, frequency_lower, frequency_upper):
    # Initialize an array to store the equity value at each trade
    equity = np.zeros((n_simulations,))
    # Set the initial equity value
    equity[0] = initial_equity
    # Set the initial value for the equity counter
    equity_counter = initial_equity
    # Set the fixed value for commissions
    commissions = -4

    # Generate a random convex payoff rate and frequency
    convex_payoff = np.random.uniform(convex_payoff_lower, convex_payoff_upper)
    frequency = np.random.uniform(frequency_lower, frequency_upper)

    # Loop through the number of trades to be simulated
    for i in range(1, n_simulations):
        # Check if the trade was successful
        win = np.random.binomial(1, win_rate, 1)
        if win:
            # If the trade was successful, calculate the daily return
            daily_return = equity_counter * win_pct
            # Add the daily return and commissions to the equity counter
            equity_counter += daily_return
            equity_counter += commissions
        else:
            # If the trade was not successful, calculate the daily loss
            daily_return = -equity_counter * loss_pct
            # Add the daily loss and commissions to the equity counter
            equity_counter += daily_return
            equity_counter += commissions

        # Store the equity counter value in the equity array
        equity[i] = equity_counter

        # Introduce a random convex payoff with a random frequency
        if np.random.uniform(0, 1) <= frequency:
            # Calculate the convex payoff
            convex_payoff_dollar = equity_counter * convex_payoff
            equity_counter += convex_payoff_dollar ### DOUBKE chexek

            print("XXXXXXXXXXXXXXXXXXXXX|| Random convex payoff ", "{:.2f}".format(convex_payoff_dollar),
                  " ({:.2f}%)".format(convex_payoff * 100), " at trade ", i)

        # Introduce the sudden loss of a random percentage between 5% and 10% with any desired frequency
        if i % sudden_loss_interval == 0:
            # Generate a random percentage loss between 5% and 10%
            sudden_loss_pct = np.random.uniform(0.05, 0.10)
            # Calculate the sudden loss
            sudden_loss = -equity_counter * sudden_loss_pct
            # Add the sudden loss to the equity counter
            equity_counter += sudden_loss
            print("|||||||||||||||||||||||||||||||||||||||||||||Sudden Loss of ", "{:.2f}".format(sudden_loss),
                  " ({:.2f}%)".format(sudden_loss_pct * 100), " at trade ", i)

        print("||Daily PnL:", "{:.2f}".format(daily_return), "||   Equity:", "{:.2f}".format(equity_counter))
    # Return the final equity array
    return equity

#  Run the simulation by calling the simulate_equity_curve function
equity = simulate_equity_curve(initial_equity, loss_pct, win_pct, win_rate, n_simulations, sudden_error, convex_payoff_lower, convex_payoff_upper, frequency_lower, frequency_upper)

#  Plot the equity curve
plt.plot(equity)
plt.title("Equity Curve")
plt.xlabel("Trade Number")
plt.ylabel("Equity")
plt.show()



