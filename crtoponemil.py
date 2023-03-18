import requests
import re


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
    api_key (str): Clash Royale API key.
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


def decoding_clan_tags(clan_tags):
    decoded_clan_tags = []

    for tag in clan_tags:
        decoded_clan_tag = re.sub(r'#', '%23', tag)
        decoded_clan_tags.append(decoded_clan_tag)

    return decoded_clan_tags


# Call decoding_clan_tags
decoded_clan_tags = decoding_clan_tags(clan_tags_with_score_above)
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

exit()
