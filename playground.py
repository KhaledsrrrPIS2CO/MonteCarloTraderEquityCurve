import numpy as np
import matplotlib.pyplot as plt

# Define the parameters
initial_equity = 3000  # initial equity amount of the options trader
loss_pct = 0.01  # the percentage loss when a trade is not successful
win_pct = 0.02  # the percentage gain when a trade is successful
max_trade_size = 20000  # max trade size of the options trader
win_rate = 0.6  # the win rate of the trader's trades
n_simulations = 400  # number of trades to be simulated
sudden_error_interval = 40  # the sudden error occurs every 40 trades
sudden_error_rate = 0.05  # the sudden loss rate for every 40 trades
convex_payoff_interval = int(n_simulations * 0.2)  # convex payoff occurs every 20% of the simulations number


# Define the simulation function to calculate the equity curve of the options trader
def simulate_equity_curve(initial_equity, loss_pct, win_pct, win_rate, max_trade_size, n_simulations,
                          sudden_error_interval, sudden_error_rate, convex_payoff_interval):
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

        # If the equity counter is bigger than max trade size, use max trade size for future returns
        if equity_counter > max_trade_size:
            equity_counter = max_trade_size

        # Store the equity counter value in the equity array
        equity[i] = equity_counter

        # Introduce the sudden loss with desired any % or any desired %, with any desired frequency
        if i % sudden_error_interval == 0:
            # Calculate the sudden loss
            sudden_loss = -equity_counter * sudden_error_rate
            # Add the sudden loss to the equity counter
            equity_counter += sudden_loss
            print("|||||||||||||||||||||||||||||||||||||||||||||Sudden Loss of ", "{:.2f}".format(sudden_loss),
                  " at trade ", i)

         # Introduce a convex payoff every 20% of the simulations number
        if i % (n_simulations // 5) == 0:
            # Define the convex payoff rate
            convex_payoff = 0.03 * (i / n_simulations)
            # Calculate the convex payoff
            convex_return = equity_counter * convex_payoff
            # Add the convex return to the equity counter
            equity_counter += convex_return
            print("|||||||||||||||||||||||||||||||||||||||||||||Convex Payoff of ", "{:.2f}".format(convex_return),
                  " at trade ", i)

            # Store the equity counter value in the equity array
        equity[i] = equity_counter

        # If the equity counter is greater than the maximum trade size, return it to the maximum trade size
        if equity_counter > max_trade_size:
            equity_counter = max_trade_size

        # Store the equity counter value in the equity array
        equity[i] = equity_counter

        # Introduce randomly a convex payoff
        if np.random.binomial(1, 0.5, 1):
            equity_counter = equity_counter * (1 + 0.01 * np.random.uniform(0.05, 0.1))
        else:
            equity_counter = equity_counter * (1 - 0.01 * np.random.uniform(0.05, 0.1))

        print("||Daily PnL:", "{:.2f}".format(daily_return), "||   Equity:", "{:.2f}".format(equity_counter))
    # Return the final equity array
    return equity

# Run the simulation by calling the simulate_equity_curve function
equity = simulate_equity_curve(initial_equity, loss_pct, win_pct, win_rate, n_simulations, sudden_error_rate,sudden_error_interval,convex_payoff_interval)

# Plot the results using matplotlib
plt.plot(equity)
plt.xlabel("number of trades")
plt.ylabel("Equity")
plt.show()

