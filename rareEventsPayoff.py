# rare events prices are usually undervalued because of psychological bias Fact: that 90% of options buyer lose money
# This fact does not mean those who buy options do not make  a killing If an options buyer make 50x with only 10% win
# rate she/he will be ahead of most people in a nutshell frequency does not matter what matter is the asymmetry of the
# reward Let us say profitable restaurant  makes on average 10% ROI a year. COVID 19 and many previously profitable
# restaurant went bust.


import numpy as np
import matplotlib.pyplot as plt

# Define the parameters
initial_equity = 3000
loss_pct = 0.01
win_pct = 0.5
win_rate = 0.05
n_simulations = 400
sudden_error = 0.05


# Write the simulation function
def simulate_equity_curve(initial_equity, loss_pct, win_pct, win_rate, n_simulations, sudden_error):
    equity = np.zeros((n_simulations,))
    equity[0] = initial_equity
    equity_counter = initial_equity
    commissions = -4

    for i in range(1, n_simulations):
        win = np.random.binomial(1, win_rate, 1)
        if win:
            daily_return = equity_counter * win_pct
            equity_counter += daily_return
            equity_counter += commissions
        else:
            daily_return = -equity_counter * loss_pct
            equity_counter += daily_return
            equity_counter += commissions

        equity[i] = equity_counter

        # Introduce the sudden loss of 5% or any desired %
        if i % 40 == 0:
        #if i == 700:
            sudden_loss = -equity_counter * sudden_error
            equity_counter += sudden_loss
            print("|||||||||||||||||||||||||||||||||||||||||||||Sudden Loss of ", "{:.2f}".format(sudden_loss), " at trade ", i)

        print("||Daily PnL:", "{:.2f}".format(daily_return), "||   Equity:", "{:.2f}".format(equity_counter))
    return equity


# Run the simulation
equity = simulate_equity_curve(initial_equity, loss_pct, win_pct, win_rate, n_simulations, sudden_error)

# Plot the results
plt.plot(equity)
plt.xlabel("number of trades")
plt.ylabel("Equity")
plt.show()



