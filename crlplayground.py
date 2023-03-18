import requests


api_key = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc' \
           '3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjY3ZDdiYTA1LWY1MWMtNDk4Zi05NTgyLTAxNjI4' \
           'YzI5ZjJhOSIsImlhdCI6MTY3NzYxMjc2NSwic3ViIjoiZGV2ZWxvcGVyLzc3YWQ4NGY3LTFjNzItNjMwOC0yY2Y3LTliOGRkN2E3OTYw' \
           'ZCIsInNjb3BlcyI6WyJyb3lhbGUiXSwibGltaXRzIjpbeyJ0aWVyIjoiZGV2ZWxvcGVyL3NpbHZlciIsInR5cGUiOiJ0aHJvdHRsaW5n' \
           'In0seyJjaWRycyI6WyIyLjIwNS4xMS4yNDUiXSwidHlwZSI6ImNsaWVudCJ9XX0.7DuDrCFsJj-6gGj15I0hW6CsT2XX7tN5GVbphfT' \
           'YwldBk7aDqs9c-JZHDVcWSfivZt9TJ9AaPGSHegDDrj68nw'


def get_player_stats(tag: str, api_key: str) -> dict:
    url = f"https://api.clashroyale.com/v1/players/{tag}/"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Accept": "application/json"
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        player_tag = data['tag']
        player_name = data['name']
        wins = data['wins']
        losses = data['losses']
        battle_count = data['battleCount']
        sum_wins_losses = wins + losses
        net_win_rate = round(wins / sum_wins_losses * 100, 2)
        net_loss_rate = round(100 - net_win_rate, 2)
        win_rate_with_discrepancy = round((wins / battle_count) * 100, 2)
        loss_rate_with_discrepancy = round(100 - win_rate_with_discrepancy, 2)
        discrepancy_games = battle_count - sum_wins_losses
        discrepancy_pct = round(((battle_count - sum_wins_losses) / battle_count) * 100, 2)

        return {
            'player_tag': player_tag,
            'name': player_name,
            'net_win_rate': net_win_rate,
            'net_loss_rate': net_loss_rate,
            'win_rate_with_discrepancy': win_rate_with_discrepancy,
            'loss_rate_with_discrepancy': loss_rate_with_discrepancy,
            'discrepancy_games': discrepancy_games,
            'discrepancy_pct': discrepancy_pct
        }

    else:
        raise ValueError(f"Error Code for Player {tag}: {response.status_code}")


player_tags = ["%23QCR929GGQ", "%23G9YV9GR8R"]

player_stats_list = []
for tag in player_tags:
    player_stats = get_player_stats(tag, api_key)
    player_stats_list.append(player_stats)

for player in player_stats_list:
    print(f"Player tag: {player['player_tag']}")
    print(f"Net win rate: {player['net_win_rate']:.2f}%")
    print(f"Net loss rate: {player['net_loss_rate']:.2f}%")
    print("\n_______________________")




