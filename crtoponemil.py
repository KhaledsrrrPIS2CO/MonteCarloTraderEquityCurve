import requests

# Obtain an API key from the Clash Royale Developer Portal
api_key = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc' \
          '3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjY3ZDdiYTA1LWY1MWMtNDk4Zi05NTgyLTAxNjI4' \
          'YzI5ZjJhOSIsImlhdCI6MTY3NzYxMjc2NSwic3ViIjoiZGV2ZWxvcGVyLzc3YWQ4NGY3LTFjNzItNjMwOC0yY2Y3LTliOGRkN2E3OTYw' \
          'ZCIsInNjb3BlcyI6WyJyb3lhbGUiXSwibGltaXRzIjpbeyJ0aWVyIjoiZGV2ZWxvcGVyL3NpbHZlciIsInR5cGUiOiJ0aHJvdHRsaW5n' \
          'In0seyJjaWRycyI6WyIyLjIwNS4xMS4yNDUiXSwidHlwZSI6ImNsaWVudCJ9XX0.7DuDrCFsJj-6gGj15I0hW6CsT2XX7tN5GVbphfT' \
          'YwldBk7aDqs9c-JZHDVcWSfivZt9TJ9AaPGSHegDDrj68nw'
#     print("The available variables of", endpoint_url, "is: ", data, "\n")
# Print the Item variable for curiosity
# print(data["items"][0])


import requests


def get_best_clan_tags():
    """
    Retrieves the tags of the best 200 clans from the Clash Royale API and stores them in an array.

    Returns:
    tags (list): A list of clan tags.
    """
    endpoint_url = 'https://api.clashroyale.com/v1/clans'

    headers = {
        'Accept': 'application/json',
        'Authorization': 'Bearer <API_TOKEN>'
    }

    params = {
        'limit': 200,
        'locationId': 57000249,  # Set the location ID to United States
        'orderBy': 'clanScore'  # Order by clan score (highest first)
    }

    response = requests.get(endpoint_url, headers=headers, params=params)

    tags = []

    if response.status_code == 200:
        data = response.json()
        print("The available variables of", endpoint_url, "is: ", data, "\n")

        for clan in data['items']:
            tags.append(clan['tag'])
    else:
        print("Error: Request returned status code", response.status_code)

    return tags



def get_all_locations(api_key):
    # Endpoint URL for retrieving all locations
    endpoint_url = 'https://api.clashroyale.com/v1/locations'

    # Headers with API key authorization
    headers = {'Authorization': f'Bearer {api_key}'}

    # Send GET request to the endpoint URL to retrieve all locations
    response = requests.get(endpoint_url, headers=headers)

    # Retrieve the JSON data from the response
    data = response.json()
    print("The available variables of", endpoint_url, "is: ", data, "\n")

    # Initialise locations array to store tags
    locations_tag = []

    # Print the name and ID of each location
    for location in data['items']:
        print(f'{location["name"]}: {location["id"]}, is a country: {location["isCountry"]}.')
        locations_tag.append({"name": location["name"], "id": location["id"]})

    # Print the Item variable for curiosity
    print(data["items"][0])

    return locations_tag


# Call get_best_clan_tags func
tags = get_best_clan_tags()
print("Best clans tags: ", tags)  # Print the list of clan tags
print("\n")

# Call get_all_locations func
locations = get_all_locations(api_key)
print(locations)
exit()
