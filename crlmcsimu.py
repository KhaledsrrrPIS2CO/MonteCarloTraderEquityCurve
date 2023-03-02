import requests
import random
import matplotlib.pyplot as plt

#%23QCR929GGQ

player_tags = ["%23G9YV9GR8R", "%23R09228V"]
api_key = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc' \
           '3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjY3ZDdiYTA1LWY1MWMtNDk4Zi05NTgyLTAxNjI4' \
          'YzI5ZjJhOSIsImlhdCI6MTY3NzYxMjc2NSwic3ViIjoiZGV2ZWxvcGVyLzc3YWQ4NGY3LTFjNzItNjMwOC0yY2Y3LTliOGRkN2E3OTYw' \
          'ZCIsInNjb3BlcyI6WyJyb3lhbGUiXSwibGltaXRzIjpbeyJ0aWVyIjoiZGV2ZWxvcGVyL3NpbHZlciIsInR5cGUiOiJ0aHJvdHRsaW5n' \
          'In0seyJjaWRycyI6WyIyLjIwNS4xMS4yNDUiXSwidHlwZSI6ImNsaWVudCJ9XX0.7DuDrCFsJj-6gGj15I0hW6CsT2XX7tN5GVbphfT' \
          'YwldBk7aDqs9c-JZHDVcWSfivZt9TJ9AaPGSHegDDrj68nw'
players_names = [] # create an empty list to store player names
players_win_rate = []
num_games = 1000000


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
        trophies = data['trophies']
        wins = data['wins']
        battle_count = data['battleCount']
        win_rate = wins / battle_count * 100
        games_played = data['battleCount']
        print(f"Player Name: {player_name}")
        print(f"Player Trophies: {trophies}")
        print(f"Win Rate: {win_rate:.2f}%")
        print(f"The player has played {games_played} games.")
        print()
        players_names.append(player_name) # add player name to the list
        players_win_rate.append(win_rate)


    else:
        print(f"Error Code for Player {tag}:", response.status_code)



# Player 1 data
p1_name = players_names[0]
p1_win_rate = players_win_rate[0] / 100

# Player 2 data
p2_name = players_names[1]
p2_win_rate = players_win_rate[1] / 100

# Simulation
p1_wins = 0
p2_wins = 0
results = []
for i in range(num_games):
    # Simulate a game
    if random.random() < p1_win_rate:
        p1_wins += 1
        results.append(p1_wins/(p1_wins+p2_wins))
    else:
        p2_wins += 1
        results.append(p1_wins/(p1_wins+p2_wins))

# Results
print(f"Simulated {num_games} games between {p1_name} and {p2_name}.")
print(f"{p1_name} won {p1_wins} games ({p1_wins/num_games*100:.2f}%).")
print(f"{p2_name} won {p2_wins} games ({p2_wins/num_games*100:.2f}%).")


plt.plot(range(len(results)), results)
plt.title("Simulation Results")
plt.xlabel("Number of Games")
plt.ylabel("Win Probability")
plt.ylim([0, 1])
plt.show()

print(players_win_rate)
exit()

# player_tags = ["%23QCR929GGQ", "%23L9V99GQLL", "%23QQCJPVVU0", "%23LYJ0VJ2YC", "%23G9YV9GR8R", "%232QLLYRUQ"]
#
# api_key = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc' \
#           '3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjY3ZDdiYTA1LWY1MWMtNDk4Zi05NTgyLTAxNjI4' \
#           'YzI5ZjJhOSIsImlhdCI6MTY3NzYxMjc2NSwic3ViIjoiZGV2ZWxvcGVyLzc3YWQ4NGY3LTFjNzItNjMwOC0yY2Y3LTliOGRkN2E3OTYw' \
#           'ZCIsInNjb3BlcyI6WyJyb3lhbGUiXSwibGltaXRzIjpbeyJ0aWVyIjoiZGV2ZWxvcGVyL3NpbHZlciIsInR5cGUiOiJ0aHJvdHRsaW5n' \
#           'In0seyJjaWRycyI6WyIyLjIwNS4xMS4yNDUiXSwidHlwZSI6ImNsaWVudCJ9XX0.7DuDrCFsJj-6gGj15I0hW6CsT2XX7tN5GVbphfT' \
#           'YwldBk7aDqs9c-JZHDVcWSfivZt9TJ9AaPGSHegDDrj68nw'
