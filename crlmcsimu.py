import requests
import random
import matplotlib.pyplot as plt

player_tags = ["%23L9V99GQLL", "%23QQCJPVVU0"]
api_key = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc' \
          '3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjY3ZDdiYTA1LWY1MWMtNDk4Zi05NTgyLTAxNjI4' \
          'YzI5ZjJhOSIsImlhdCI6MTY3NzYxMjc2NSwic3ViIjoiZGV2ZWxvcGVyLzc3YWQ4NGY3LTFjNzItNjMwOC0yY2Y3LTliOGRkN2E3OTYw' \
          'ZCIsInNjb3BlcyI6WyJyb3lhbGUiXSwibGltaXRzIjpbeyJ0aWVyIjoiZGV2ZWxvcGVyL3NpbHZlciIsInR5cGUiOiJ0aHJvdHRsaW5n' \
          'In0seyJjaWRycyI6WyIyLjIwNS4xMS4yNDUiXSwidHlwZSI6ImNsaWVudCJ9XX0.7DuDrCFsJj-6gGj15I0hW6CsT2XX7tN5GVbphfT' \
          'YwldBk7aDqs9c-JZHDVcWSfivZt9TJ9AaPGSHegDDrj68nw'
players_names = []
players_win_rate = []
players_loss_rate = []
num_games = 100000

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
        win_rate = wins / sum_wins_losses * 100
        sum_wins_losses = wins + losses
        print(f"Player name: {player_name}")
        print(f"Wins: {wins}")
        print(f"Losses: {losses}")
        print(f"Total games: {battle_count} ")
        print("Total games minus sum of wins & losses: ", battle_count - sum_wins_losses)
        print("Difference between total games &  sum of wins and losses: ",
              round((battle_count - sum_wins_losses) / battle_count, 2) * 100, "%")
        print(f"Win rate: {win_rate:.2f}%")
        print("Loss rate:", round(100-win_rate, 2), "%")
        real_win_rate = round(wins/sum_wins_losses * 100, 2)
        print("raw win rate:", round(wins/battle_count*100, 2))
        print("raw loss rate:", round(100-round(wins/battle_count*100, 2)))

        print()
        players_names.append(player_name)
        players_win_rate.append(win_rate / 100)
        players_loss_rate.append((100-win_rate) / 100)

    else:
        print(f"Error Code for Player {tag}:", response.status_code)

p1_name = players_names[0]
p1_win_rate = players_win_rate[0]
p1_loss_rate = players_loss_rate[0]

p2_name = players_names[1]
p2_win_rate = players_win_rate[1]
p2_loss_rate = players_loss_rate[1]

# Calculate player one's future potential win rate
# Adjusted future potential win probability of Team One = 75.7% / (75.7% + 58.1%) * 100% = 56.5%
p1_adjusted_future_win_rate = p1_win_rate / (p1_win_rate + p2_win_rate) * 100
p2_adjusted_future_win_rate = p2_win_rate / (p2_win_rate + p1_win_rate) * 100
print(f"Player one, {players_names[0]} adjusted future potential win rate: {p1_adjusted_future_win_rate:.2f}")
print(f"Player two, {players_names[1]} adjusted future potential win rate: {p2_adjusted_future_win_rate:.2f}")
# Simulation
p1_wins = 0
p2_wins = 0
results = []

for i in range(num_games):
    # Set the win probability for each game to 50/50
    p1_prob = p2_prob = 0.5

    # Increase player two's win probability by 0.1% after each game played
    p2_prob += i * 0.01

    # Simulate a game
    if random.random() < p1_prob:
        p1_wins += 1
        results.append(p1_wins / (p1_wins + p2_wins))
    else:
        p2_wins += 1
        results.append(p1_wins / (p1_wins + p2_wins))

# Results
#print(f"/nSimulated {num_games} games between {p1_name} and {p2_name}.")
#print(f"{p1_name} won {p1_wins} games ({p1_wins/num_games*100:.2f}%).")
#print(f"{p2_name} won {p2_wins} games ({p2_wins/num_games*100:.2f}%).")


plt.plot(range(len(results)), results)
plt.title("Simulation Results")
plt.xlabel("Number of Games")
plt.ylabel("Win Probability")
plt.ylim([0, 1])
plt.show()


exit()


# player_tags = ["%23QCR929GGQ", "%23L9V99GQLL", "%23QQCJPVVU0", "%23LYJ0VJ2YC", "%23G9YV9GR8R", "%232QLLYRUQ"]
#
# api_key = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc' \
#           '3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjY3ZDdiYTA1LWY1MWMtNDk4Zi05NTgyLTAxNjI4' \
#           'YzI5ZjJhOSIsImlhdCI6MTY3NzYxMjc2NSwic3ViIjoiZGV2ZWxvcGVyLzc3YWQ4NGY3LTFjNzItNjMwOC0yY2Y3LTliOGRkN2E3OTYw' \
#           'ZCIsInNjb3BlcyI6WyJyb3lhbGUiXSwibGltaXRzIjpbeyJ0aWVyIjoiZGV2ZWxvcGVyL3NpbHZlciIsInR5cGUiOiJ0aHJvdHRsaW5n' \
#           'In0seyJjaWRycyI6WyIyLjIwNS4xMS4yNDUiXSwidHlwZSI6ImNsaWVudCJ9XX0.7DuDrCFsJj-6gGj15I0hW6CsT2XX7tN5GVbphfT' \
#           'YwldBk7aDqs9c-JZHDVcWSfivZt9TJ9AaPGSHegDDrj68nw'
# Sha: L9V99GQLL
# ME: QCR929GGQ