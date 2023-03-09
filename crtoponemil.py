import requests

# Obtain an API key from the Clash Royale Developer Portal
api_key = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc' \
          '3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjY3ZDdiYTA1LWY1MWMtNDk4Zi05NTgyLTAxNjI4' \
          'YzI5ZjJhOSIsImlhdCI6MTY3NzYxMjc2NSwic3ViIjoiZGV2ZWxvcGVyLzc3YWQ4NGY3LTFjNzItNjMwOC0yY2Y3LTliOGRkN2E3OTYw' \
          'ZCIsInNjb3BlcyI6WyJyb3lhbGUiXSwibGltaXRzIjpbeyJ0aWVyIjoiZGV2ZWxvcGVyL3NpbHZlciIsInR5cGUiOiJ0aHJvdHRsaW5n' \
          'In0seyJjaWRycyI6WyIyLjIwNS4xMS4yNDUiXSwidHlwZSI6ImNsaWVudCJ9XX0.7DuDrCFsJj-6gGj15I0hW6CsT2XX7tN5GVbphfT' \
          'YwldBk7aDqs9c-JZHDVcWSfivZt9TJ9AaPGSHegDDrj68nw'


def get_clan_player_tags(clan_tag, api_token):
    # API endpoint
    api_url = 'https://api.clashroyale.com/v1/clans/{}/members'

    # Request headers with your API token
    headers = {'Authorization': f'Bearer {api_token}'}

    # Send a request to get all members of the clan
    url = api_url.format(clan_tag)
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        # Extract the tags of each member
        members = response.json()['items']

        tags = [member['tag'] for member in members]
        return tags
    else:
        print(f'Error retrieving clan members for tag {clan_tag}: {response.status_code}')
        return []
# call the get_clan_player_tags fun
api_key = api_key
clan_tag = "%23QV9PGUJR"
tags = get_clan_player_tags(clan_tag, api_key)
print("Players tags: ", tags)
# 'tag': '#9PG00RUU'
# "tag": "#Q9RYUCJG",
# clan': Mo light {'tag': '#QV9PGUJR', 'name': 'GKR
print("_____")


def get_top_clan_tags(api_key):
    api_url = 'https://api.clashroyale.com/v1/clans?limit=2000'

    headers = {'Authorization': f'Bearer {api_key}'}

    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        clans = response.json()['items']
        tags = [clan['tag'] for clan in clans]
        return tags
    else:
        print(f'Error retrieving top clans tags: {response.status_code}')
        return []
# Call get_top_clan_tags fun
api_key = api_key
clan_tags = get_top_clan_tags(api_key)
print("Top 1000 clans tags: ", clan_tags)
print("_____")


def get_clan_details(clan_tag, api_key):
    # API endpoint
    api_url = 'https://api.clashroyale.com/v1/clans/{}'

    # Request headers with your API token
    headers = {'Authorization': f'Bearer {api_key}'}

    # Send a request to get the clan details
    url = api_url.format(clan_tag)
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        # Extract the clan details
        clan_details = response.json()
        return clan_details
    else:
        print(f'Error retrieving clan details for tag {clan_tag}: {response.status_code}')
        return None
# Call get_clan_details fun
api_key = api_key
clan_tag = '%23QV9PGUJR'
clan_details = get_clan_details(clan_tag, api_key)
clan_name = clan_details["name"]
print(f"Clan {clan_name} details:",  clan_details)
print("_____")



def get_player_details(player_tag, api_token):
    api_url = 'https://api.clashroyale.com/v1/players/{}'
    headers = {'Authorization': f'Bearer {api_token}'}
    url = api_url.format(player_tag)
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        print(f'Error retrieving player details for tag {player_tag}: {response.status_code}')
        return {}
# Call get_player_details fun
api_key = api_key
player_tag = "%23QCR929GGQ"
player_details = get_player_details(player_tag, api_key)
player_name = player_details["name"]
print(f"Player {player_name} details: ", player_details)
print("_____")
player_tag_1 = "%23G9YV9GR8R"
player_one_details = get_player_details(player_tag_1, api_key)
player_one_name = player_one_details["name"]
print(f"Player {player_one_name} details: ", player_one_details)






exit()

# print("The available variables of dictionary: ", api_url, "is: ", members, "\n")
