import requests
import time

# Obtain an API key from the Clash Royale Developer Portal
api_key = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc' \
           '3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjY3ZDdiYTA1LWY1MWMtNDk4Zi05NTgyLTAxNjI4' \
           'YzI5ZjJhOSIsImlhdCI6MTY3NzYxMjc2NSwic3ViIjoiZGV2ZWxvcGVyLzc3YWQ4NGY3LTFjNzItNjMwOC0yY2Y3LTliOGRkN2E3OTYw' \
           'ZCIsInNjb3BlcyI6WyJyb3lhbGUiXSwibGltaXRzIjpbeyJ0aWVyIjoiZGV2ZWxvcGVyL3NpbHZlciIsInR5cGUiOiJ0aHJvdHRsaW5n' \
           'In0seyJjaWRycyI6WyIyLjIwNS4xMS4yNDUiXSwidHlwZSI6ImNsaWVudCJ9XX0.7DuDrCFsJj-6gGj15I0hW6CsT2XX7tN5GVbphfT' \
           'YwldBk7aDqs9c-JZHDVcWSfivZt9TJ9AaPGSHegDDrj68nw'
# Endpoint URL for retrieving Path of Legends rankings
endpoint_url = 'https://api.clashroyale.com/v1/locations/57000061/rankings/players'

# Headers with API key authorization
headers = {'Authorization': f'Bearer {api_key}'}

# Store the player tags in a list
player_tags = []

# Loop over the API pagination to retrieve all players in the Path of Legends rankings
while endpoint_url:
    response = requests.get(endpoint_url, headers=headers)
    data = response.json()
    for item in data['items']:
        player_tags.append(item['tag'])
    # Check if there's a next page of results
    endpoint_url = data.get('next')
    # Handle API rate limits by pausing for 1 second between requests
    time.sleep(1)

# Print the number of player tags retrieved
print(f'{len(player_tags)} player tags retrieved')

# Print the player tags
print(player_tags)


exit()