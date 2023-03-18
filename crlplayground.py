import requests

# Obtain an API key from the Clash Royale Developer Portal
api_key = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc' \
          '3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjY3ZDdiYTA1LWY1MWMtNDk4Zi05NTgyLTAxNjI4' \
          'YzI5ZjJhOSIsImlhdCI6MTY3NzYxMjc2NSwic3ViIjoiZGV2ZWxvcGVyLzc3YWQ4NGY3LTFjNzItNjMwOC0yY2Y3LTliOGRkN2E3OTYw' \
          'ZCIsInNjb3BlcyI6WyJyb3lhbGUiXSwibGltaXRzIjpbeyJ0aWVyIjoiZGV2ZWxvcGVyL3NpbHZlciIsInR5cGUiOiJ0aHJvdHRsaW5n' \
          'In0seyJjaWRycyI6WyIyLjIwNS4xMS4yNDUiXSwidHlwZSI6ImNsaWVudCJ9XX0.7DuDrCFsJj-6gGj15I0hW6CsT2XX7tN5GVbphfT' \
          'YwldBk7aDqs9c-JZHDVcWSfivZt9TJ9AaPGSHegDDrj68nw'


def get_clans_above_score(api_key: str, min_score: int) -> list:
    """
    Retrieve the tags of all Clash Royale clans with a `clanScore` above `min_score`.

    Parameters:
    api_key (str): Your Clash Royale API key.
    min_score (int): The minimum `clanScore` value that the returned clans should have.

    Returns:
    list: A list of clan tags (strings) for the clans with `clanScore` above `min_score`.

    Raises:
    ValueError: If the API returns an error status code.
    """

    # Construct the API request URL and headers
    url = f"https://api.clashroyale.com/v1/clans?minScore={min_score}"
    headers = {
        "Accept": "application/json",
        "authorization": f"Bearer {api_key}"
    }

    # Send the API request and handle the response
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        items = response.json()["items"]
        clan_tags = [item["tag"] for item in items]
        return clan_tags
    elif response.status_code == 400:
        raise ValueError("Invalid input parameter(s)")
    elif response.status_code == 401:
        raise ValueError("Unauthorized access, check API key")
    elif response.status_code == 403:
        raise ValueError("Access denied, insufficient privileges")
    elif response.status_code == 404:
        raise ValueError("Resource not found")
    else:
        raise ValueError("Unknown error occurred")



# Call get_clans_above_score
min_score = 74000
clan_tags_with_score_above = get_clans_above_score(api_key, min_score)
print(f"Retrieved {len(clan_tags_with_score_above)} Clan tags with score above {min_score}.")
print("____")

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
