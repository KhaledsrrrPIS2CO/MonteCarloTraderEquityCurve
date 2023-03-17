import requests

# Obtain an API key from the Clash Royale Developer Portal
api_key = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc' \
          '3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjY3ZDdiYTA1LWY1MWMtNDk4Zi05NTgyLTAxNjI4' \
          'YzI5ZjJhOSIsImlhdCI6MTY3NzYxMjc2NSwic3ViIjoiZGV2ZWxvcGVyLzc3YWQ4NGY3LTFjNzItNjMwOC0yY2Y3LTliOGRkN2E3OTYw' \
          'ZCIsInNjb3BlcyI6WyJyb3lhbGUiXSwibGltaXRzIjpbeyJ0aWVyIjoiZGV2ZWxvcGVyL3NpbHZlciIsInR5cGUiOiJ0aHJvdHRsaW5n' \
          'In0seyJjaWRycyI6WyIyLjIwNS4xMS4yNDUiXSwidHlwZSI6ImNsaWVudCJ9XX0.7DuDrCFsJj-6gGj15I0hW6CsT2XX7tN5GVbphfT' \
          'YwldBk7aDqs9c-JZHDVcWSfivZt9TJ9AaPGSHegDDrj68nw'


def get_clan_tags_with_score_above(api_key, score, location_id, limit):
    url = f"https://api.clashroyale.com/v1/clans?score={score}&locationId={location_id}&limit={limit}"
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


score = 72000
location_id = 57000010
limit = 1000
clan_tags_with_score_above = get_clan_tags_with_score_above(api_key, score, location_id, limit)
print("Clan tags: ", clan_tags_with_score_above)


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
