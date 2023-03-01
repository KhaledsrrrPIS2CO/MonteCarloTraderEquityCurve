import requests

# Replace {your_api_token} with your actual API token
api_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjY3ZDdiYTA1LWY1MWMtNDk4Zi05NTgyLTAxNjI4YzI5ZjJhOSIsImlhdCI6MTY3NzYxMjc2NSwic3ViIjoiZGV2ZWxvcGVyLzc3YWQ4NGY3LTFjNzItNjMwOC0yY2Y3LTliOGRkN2E3OTYwZCIsInNjb3BlcyI6WyJyb3lhbGUiXSwibGltaXRzIjpbeyJ0aWVyIjoiZGV2ZWxvcGVyL3NpbHZlciIsInR5cGUiOiJ0aHJvdHRsaW5nIn0seyJjaWRycyI6WyIyLjIwNS4xMS4yNDUiXSwidHlwZSI6ImNsaWVudCJ9XX0.7DuDrCFsJj-6gGj15I0hW6CsT2XX7tN5GVbphfTYwldBk7aDqs9c-JZHDVcWSfivZt9TJ9AaPGSHegDDrj68nw"
player_tag = "QCR929GGQ"

url = f"https://api.clashroyale.com/v1/players/{player_tag}/battlelog"

headers = {
    "Authorization": f"Bearer {api_token}",
    "Accept": "application/json"
}

response = requests.get(url, headers=headers)

if response.ok:
    battles = response.json()
    wins = 0
    total = 0
    for battle in battles:
        if battle.get("type") == "PvP" and "winner" in battle:
            total += 1
            if battle["winner"] == "1":
                wins += 1
    if total > 0:
        win_rate = wins / total
        print(f"Win rate for {player_tag}: {win_rate:.2%}")
    else:
        print(f"No battles found for {player_tag}")
else:
    print(f"Error getting battle log for {player_tag}: {response.text}")
