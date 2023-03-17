import requests
import re


# Obtain an API key from the Clash Royale Developer Portal
api_key = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc' \
          '3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjY3ZDdiYTA1LWY1MWMtNDk4Zi05NTgyLTAxNjI4' \
          'YzI5ZjJhOSIsImlhdCI6MTY3NzYxMjc2NSwic3ViIjoiZGV2ZWxvcGVyLzc3YWQ4NGY3LTFjNzItNjMwOC0yY2Y3LTliOGRkN2E3OTYw' \
          'ZCIsInNjb3BlcyI6WyJyb3lhbGUiXSwibGltaXRzIjpbeyJ0aWVyIjoiZGV2ZWxvcGVyL3NpbHZlciIsInR5cGUiOiJ0aHJvdHRsaW5n' \
          'In0seyJjaWRycyI6WyIyLjIwNS4xMS4yNDUiXSwidHlwZSI6ImNsaWVudCJ9XX0.7DuDrCFsJj-6gGj15I0hW6CsT2XX7tN5GVbphfT' \
          'YwldBk7aDqs9c-JZHDVcWSfivZt9TJ9AaPGSHegDDrj68nw'


def get_clan_tags_with_score_above(api_key):
    url = "https://api.clashroyale.com/v1/clans?score=72000&locationId=57000010&limit=1000"
    headers = {"Authorization": f"Bearer {api_key}"}

    response = requests.get(url, headers=headers)
    data = response.json()

    if "items" not in data:
        print("Error: API response does not contain 'items' key")
        print(response.content)
        return []

    tags = []
    for clan in data["items"]:
        tags.append(clan["tag"])

    return tags


# Call get_top_clan_tags
top_clans_tags = get_clan_tags_with_score_above(api_key)
top_clans_tags_len = len(top_clans_tags)
print(f"Retrieved {top_clans_tags_len} clans tags with score over 72000.")
print("_____")


def decoding_clan_tags(clan_tags):
    decoded_clan_tags = []

    for tag in clan_tags:
        decoded_clan_tag = re.sub(r'#', '%23', tag)
        decoded_clan_tags.append(decoded_clan_tag)

    return decoded_clan_tags


# Call decoding_clan_tags
decoded_clan_tags = decoding_clan_tags(top_clans_tags)
print(f"Decoded {len(decoded_clan_tags)} clan tags.")
print("_____")


def get_player_tags(api_key, clan_tags):
    player_tags = []

    for tag in clan_tags:
        url = f"https://api.clashroyale.com/v1/clans/{tag}/members"
        headers = {"Authorization": f"Bearer {api_key}"}

        response = requests.get(url, headers=headers)
        data = response.json()

        if "items" not in data:
            print(f"Error: API response for clan tag {tag} does not contain 'items' key")
            continue

        for member in data["items"]:
            player_tags.append(member["tag"])

    return player_tags


# Call get_player_tags
player_tags = get_player_tags(api_key, decoded_clan_tags)
print(f"Retrieved {len(player_tags)} players tags.")
print("_____")


def decoding_players_tags(player_tags):
    decoded_players_tags = []

    for tag in player_tags:
        decoded_player_tag = re.sub(r'#', '%23', tag)
        decoded_players_tags.append(decoded_player_tag)

    return decoded_players_tags


# Call decoding_players_tags
decoded_players_tags = decoding_players_tags(player_tags)
print(f"Decoded {len(decoded_players_tags)} players tags.")
print("_____")


import requests


def get_clan_details(api_key, clan_tag):
    url = f"https://api.clashroyale.com/v1/clans/{clan_tag}"
    headers = {"Authorization": f"Bearer {api_key}"}

    response = requests.get(url, headers=headers)
    data = response.json()

    if "name" not in data:
        print(f"Error: API response for clan tag {clan_tag} does not contain 'name' key")
        return None

    clan_details = {
        "name": data["name"],
        "tag": data["tag"],
        "description": data.get("description", ""),
        "type": data.get("type", ""),
        "location": {
            "name": data.get("location", {}).get("name", ""),
            "code": data.get("location", {}).get("id", "")
        },
        "members": data.get("members", 0),
        "score": data.get("score", 0),
        "donations": data.get("donations", 0),
        "clan_war_trophies": data.get("clanWarTrophies", 0),
        "required_trophies": data.get("requiredTrophies", 0),
        "clan_chest_level": data.get("clanChestLevel", 0),
        "clan_chest_max_level": data.get("clanChestMaxLevel", 0)
    }

    return clan_details


clan_tag = "%239YLRLG09"
clan_details = get_clan_details(api_key, clan_tag)
print("Clan details:", clan_details)
exit()
