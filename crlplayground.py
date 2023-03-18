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


print_all_location_ids(api_key)



exit()



