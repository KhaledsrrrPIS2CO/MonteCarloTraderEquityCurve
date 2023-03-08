import requests

# Obtain an API key from the Clash Royale Developer Portal
api_key = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc' \
           '3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjY3ZDdiYTA1LWY1MWMtNDk4Zi05NTgyLTAxNjI4' \
           'YzI5ZjJhOSIsImlhdCI6MTY3NzYxMjc2NSwic3ViIjoiZGV2ZWxvcGVyLzc3YWQ4NGY3LTFjNzItNjMwOC0yY2Y3LTliOGRkN2E3OTYw' \
           'ZCIsInNjb3BlcyI6WyJyb3lhbGUiXSwibGltaXRzIjpbeyJ0aWVyIjoiZGV2ZWxvcGVyL3NpbHZlciIsInR5cGUiOiJ0aHJvdHRsaW5n' \
           'In0seyJjaWRycyI6WyIyLjIwNS4xMS4yNDUiXSwidHlwZSI6ImNsaWVudCJ9XX0.7DuDrCFsJj-6gGj15I0hW6CsT2XX7tN5GVbphfT' \
           'YwldBk7aDqs9c-JZHDVcWSfivZt9TJ9AaPGSHegDDrj68nw'


def get_clan_tags(clan_tag, api_token):
    # API endpoint
    api_url = 'https://api.clashroyale.com/v1/clans/{}/members'
    api_url_1 = 'https://api.clashroyale.com/v1/clans/{}/'

    # Request headers with your API token
    headers = {'Authorization': f'Bearer {api_token}'}

    # Send a request to get all members of the clan
    url = api_url.format(clan_tag)
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        # Extract the tags of each member
        members = response.json()['items']
        print("The available variables of dictionary: ", api_url, "is: ", members, "\n")
        print("The available variables of dictionary: ", api_url_1, "is: ", members, "\n")


        tags = [member['tag'] for member in members]
        return tags
    else:
        print(f'Error retrieving clan members for tag {clan_tag}: {response.status_code}')
        return []



def get_all_locations(api_key):
    # Endpoint URL for retrieving all locations
    endpoint_url = 'https://api.clashroyale.com/v1/locations'

    # Headers with API key authorization
    headers = {'Authorization': f'Bearer {api_key}'}

    # Send GET request to the endpoint URL to retrieve all locations
    response = requests.get(endpoint_url, headers=headers)

    # Retrieve the JSON data from the response
    data = response.json()
    print("The available variables of dictionary: ", endpoint_url, "is: ", data, "\n")

    # Initialise locations array to store tags
    locations_tag = []

    # Print the name and ID of each location
    for location in data['items']:
        print(f'{location["name"]}: {location["id"]}, is a country: {location["isCountry"]}.')
        locations_tag.append({"name": location["name"], "id": location["id"]})

    # Print the Item variable for curiosity
    print("Item variable: ", data["items"][0])

    return locations_tag

# call the ge_clan_id
api_token = api_key
clan_tag = "%239PG00RUU"
tags = get_clan_tags(clan_tag, api_token)
print("taaaags: ", tags)
# 'tag': '#9PG00RUU'



print("\n")

# Call get_all_locations func
locations = get_all_locations(api_key)
print(locations)
exit()
