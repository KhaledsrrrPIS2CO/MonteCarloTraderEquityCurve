import requests

api_key = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc' \
          '3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjY3ZDdiYTA1LWY1MWMtNDk4Zi05NTgyLTAxNjI4' \
          'YzI5ZjJhOSIsImlhdCI6MTY3NzYxMjc2NSwic3ViIjoiZGV2ZWxvcGVyLzc3YWQ4NGY3LTFjNzItNjMwOC0yY2Y3LTliOGRkN2E3OTYw' \
          'ZCIsInNjb3BlcyI6WyJyb3lhbGUiXSwibGltaXRzIjpbeyJ0aWVyIjoiZGV2ZWxvcGVyL3NpbHZlciIsInR5cGUiOiJ0aHJvdHRsaW5n' \
          'In0seyJjaWRycyI6WyIyLjIwNS4xMS4yNDUiXSwidHlwZSI6ImNsaWVudCJ9XX0.7DuDrCFsJj-6gGj15I0hW6CsT2XX7tN5GVbphfT' \
          'YwldBk7aDqs9c-JZHDVcWSfivZt9TJ9AaPGSHegDDrj68nw'



url = 'https://api.clashroyale.com/v1/leaderboards/global/players'

headers = {
    'Authorization': f'Bearer {api_key}',
    'Accept': 'application/json'
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    rankings = data['items']
    for rank in rankings:
        player_name = rank['name']
        player_trophies = rank['trophies']
        print(f'Rank {rank["rank"]}: {player_name} - {player_trophies} trophies')
else:
    print('Error retrieving leaderboard:', response.status_code)
