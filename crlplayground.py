import requests


api_key = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc' \
           '3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjY3ZDdiYTA1LWY1MWMtNDk4Zi05NTgyLTAxNjI4' \
           'YzI5ZjJhOSIsImlhdCI6MTY3NzYxMjc2NSwic3ViIjoiZGV2ZWxvcGVyLzc3YWQ4NGY3LTFjNzItNjMwOC0yY2Y3LTliOGRkN2E3OTYw' \
           'ZCIsInNjb3BlcyI6WyJyb3lhbGUiXSwibGltaXRzIjpbeyJ0aWVyIjoiZGV2ZWxvcGVyL3NpbHZlciIsInR5cGUiOiJ0aHJvdHRsaW5n' \
           'In0seyJjaWRycyI6WyIyLjIwNS4xMS4yNDUiXSwidHlwZSI6ImNsaWVudCJ9XX0.7DuDrCFsJj-6gGj15I0hW6CsT2XX7tN5GVbphfT' \
           'YwldBk7aDqs9c-JZHDVcWSfivZt9TJ9AaPGSHegDDrj68nw'


def print_all_location_ids(api_key: str) -> None:
    """
    Print all the location IDs available in the Clash Royale API.

    Parameters:
    api_key (str): Clash Royale API key.
    """

    # Construct the API request URL and headers
    url = "https://api.clashroyale.com/v1/locations"
    headers = {
        "Accept": "application/json",
        "authorization": f"Bearer {api_key}"
    }

    # Send the API request and handle the response
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        locations = response.json()["items"]
        for location in locations:
            print(f"Location ID: {location['id']}, Name: {location['name']}")
    else:
        raise ValueError("Unknown error occurred")


def get_clans_tags_above_score(api_key: str, min_score: int) -> list:
    """
    Retrieve the tags of all Clash Royale clans with a `clanScore` above `min_score` and located in the given location.

    Parameters:
    api_key (str): Clash Royale API key.
    min_score (int): The minimum `clanScore` value that the returned clans should have.
    location_id (int): The ID of the location to retrieve clans from.

    Returns:
    list: A list of clan tags (strings) for the clans with `clanScore` above `min_score` and located in the given location.

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
clan_tags_with_score_above = get_clans_tags_above_score(api_key, min_score)
print(f"Retrieved {len(clan_tags_with_score_above)} Clan tags with score above {min_score}"
      f" in location ID:")
print("____")


print_all_location_ids(api_key)


exit()



