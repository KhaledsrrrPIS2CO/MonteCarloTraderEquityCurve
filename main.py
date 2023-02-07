import numpy as np
import matplotlib.pyplot as plt

# Define the parameters
initial_equity = 3000  # initial equity amount of the options trader
loss_pct = 0.01  # the percentage loss when a trade is not successful
win_pct = 0.02  # the percentage gain when a trade is successful
win_rate = 0.5  # the win rate of the trader's trades
n_simulations = 400  # number of trades to be simulated
sudden_error = 0.3  # the sudden loss rate for every 75 trades


# Define the simulation function to calculate the equity curve of the options trader
def simulate_equity_curve(initial_equity, loss_pct, win_pct, win_rate, n_simulations, sudden_error):
    # Initialize an array to store the equity value at each trade
    equity = np.zeros((n_simulations,))
    # Set the initial equity value
    equity[0] = initial_equity
    # Set the initial value for the equity counter
    equity_counter = initial_equity
    # Set the fixed value for commissions
    commissions = -4

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

        # Introduce the sudden loss of 5% or any desired %, with any desired frequency
        if i % 300 == 0:
            # Calculate the sudden loss
            sudden_loss = -equity_counter * sudden_error
            # Add the sudden loss to the equity counter
            equity_counter += sudden_loss
            print("|||||||||||||||||||||||||||||||||||||||||||||Sudden Loss of ", "{:.2f}".format(sudden_loss), " at trade ", i)

        print("||Daily PnL:", "{:.2f}".format(daily_return), "||   Equity:", "{:.2f}".format(equity_counter))
    # Return the final equity array
    return equity

# Run the simulation by calling the simulate_equity_curve function
equity = simulate_equity_curve(initial_equity, loss_pct, win_pct, win_rate, n_simulations, sudden_error)

# Plot the results using matplotlib
plt.plot(equity)
plt.xlabel("number of trades")
plt.ylabel("Equity")
plt.show()
