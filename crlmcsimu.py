import requests
import numpy as np
import matplotlib.pyplot as plt

player_tags = ["%23QCR929GGQ", "%23G9YV9GR8R", ]
api_key = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc' \
           '3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjY3ZDdiYTA1LWY1MWMtNDk4Zi05NTgyLTAxNjI4' \
           'YzI5ZjJhOSIsImlhdCI6MTY3NzYxMjc2NSwic3ViIjoiZGV2ZWxvcGVyLzc3YWQ4NGY3LTFjNzItNjMwOC0yY2Y3LTliOGRkN2E3OTYw' \
           'ZCIsInNjb3BlcyI6WyJyb3lhbGUiXSwibGltaXRzIjpbeyJ0aWVyIjoiZGV2ZWxvcGVyL3NpbHZlciIsInR5cGUiOiJ0aHJvdHRsaW5n' \
           'In0seyJjaWRycyI6WyIyLjIwNS4xMS4yNDUiXSwidHlwZSI6ImNsaWVudCJ9XX0.7DuDrCFsJj-6gGj15I0hW6CsT2XX7tN5GVbphfT' \
           'YwldBk7aDqs9c-JZHDVcWSfivZt9TJ9AaPGSHegDDrj68nw'
players_names = []
players_net_win_rate = []
players_net_loss_rate = []

# Get player stats from API
for tag in player_tags:
    url = f"https://api.clashroyale.com/v1/players/{tag}/"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Accept": "application/json"
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        player_name = data['name']
        wins = data['wins']
        losses = data['losses']
        battle_count = data['battleCount']
        sum_wins_losses = wins + losses
        net_win_rate = wins / sum_wins_losses * 100
        net_loss_rate = 100 - net_win_rate
        win_rate_with_discrepancy = round((wins / battle_count) * 100, 2)
        loss_rate_with_discrepancy = round(100 - win_rate_with_discrepancy, 2)
        discrepancy_games = battle_count - sum_wins_losses
        discrepancy_pct = round(((battle_count - sum_wins_losses) / battle_count) * 100, 2)

        print(f"Player name: {player_name}")
        print(f"Wins: {wins}")
        print(f"Losses: {losses}")
        print(f"Battle count: {battle_count} ")
        print("Sum(Wins & losses):", sum_wins_losses)
        print("Discrepancy (games): ", discrepancy_games, "or discrepancy (percentage):", discrepancy_pct, "%")
        print(f"Net win rate: {net_win_rate:.2f}%")
        print(f"Net loss rate: {net_loss_rate:.2f}%")
        print(f"Win rate (with discrepancy):{win_rate_with_discrepancy}%")
        print(f"Loss rate (with discrepancy): {loss_rate_with_discrepancy}%")
        print("\n_______________________")
        players_names.append(player_name)
        players_net_win_rate.append(net_win_rate / 100)
        players_net_loss_rate.append(net_loss_rate / 100)

    else:
        print(f"Error Code for Player {tag}:", response.status_code)

# Get player names and win rates
p1_name = players_names[0]
p1_win_rate = players_net_win_rate[0]

p2_name = players_names[1]
p2_win_rate = players_net_win_rate[1]

# Adjusted future potential win probability
p1_adjusted_future_win_rate = p1_win_rate / (p1_win_rate + p2_win_rate) * 100
p2_adjusted_future_win_rate = p2_win_rate / (p2_win_rate + p1_win_rate) * 100
print(f"Future potential win rate of player one, {players_names[0]}: {p1_adjusted_future_win_rate:.2f}%")
print(f"Future potential win rate of player two, {players_names[1]}: {p2_adjusted_future_win_rate:.2f}%")
print("\n")

# Monte Carlo simulation
# Set the win probabilities for each player
p1_prob = p1_adjusted_future_win_rate / 100
p2_prob = p2_adjusted_future_win_rate / 100

# Set the number of games to simulate
num_games = 100000

# Initialize counters for each player's wins
p1_wins = 0
p2_wins = 0

# Play the games and update the win counters
for i in range(num_games):
    # Simulate the outcome of the game using np.random.binomial
    outcome = np.random.binomial(1, p1_prob)
    if outcome == 1:
        p1_wins += 1
    else:
        p2_wins += 1

# Plot the results

plt.bar([p1_name, p2_name], [p1_wins, p2_wins])
plt.ylabel('Number of Wins')
plt.title('Monte Carlo Simulation Results')
plt.show()

print(p1_name, "wins: ", p1_wins, "or", round((p1_wins/num_games)*100, 2), "%")
print(p2_name, "wins: ", p2_wins, "or", round((p2_wins/num_games)*100, 2), "%")


exit()
