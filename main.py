# monte carlo simulation for an options trader possible equity path

import numpy as np
import matplotlib.pyplot as plt

#Compounding
# Define the parameters
initial_equity = 3000
loss_pct = 0.01
win_pct = 0.018
win_rate = 0.41
n_simulations = 400


# Write the simulation function
def simulate_equity_curve(initial_equity, loss_pct, win_pct, win_rate, n_simulations):
    """
       Simulates the equity curve of a day trader

       Parameters
       ----------
       initial_equity : float
           The initial amount of money in the trading account.
       loss_pct : float
           The percentage of initial_equity that is lost in case of a losing trade.
       win_pct : float
           The percentage of initial_equity that is won in case of a winning trade.
       win_rate : float
           The probability of winning a trade.
       n_simulations : int
           The number of trades to simulate.

       Returns
       -------
       equity : numpy.ndarray
           The equity curve of the day trader, where each element is the balance
           of the trading account after each trade.
       """
    equity = np.zeros((n_simulations,))
    equity[0] = initial_equity
    equity_counter = initial_equity

    for i in range(1, n_simulations):
        win = np.random.binomial(1, win_rate, 1)
        if win:
            daily_return = equity_counter * win_pct
            equity_counter += daily_return
        else:
            daily_return = -equity_counter * loss_pct
            equity_counter += daily_return
        equity[i] = equity_counter
        print("||Daily PnL:", "{:.2f}".format(daily_return), "||   Equity:", "{:.2f}".format(equity_counter))
    return equity

# Run the simulation
equity = simulate_equity_curve(initial_equity, loss_pct, win_pct, win_rate, n_simulations)

# Plot the results
plt.plot(equity)
plt.xlabel("number of trades")
plt.ylabel("Equity")
plt.show()




