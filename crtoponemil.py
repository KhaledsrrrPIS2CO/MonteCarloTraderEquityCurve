import requests
import re
import time
import mysql.connector

start_time = time.time()
cnx = mysql.connector.connect(
    user='root',
    password='2020$2020$ABC',
    host='127.0.0.1',
    database='clash_royale_database'
)
cursor = cnx.cursor()

# Obtained API key from the Clash Royale Developer Portal
api_key = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc' \
          '3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjY3ZDdiYTA1LWY1MWMtNDk4Zi05NTgyLTAxNjI4' \
          'YzI5ZjJhOSIsImlhdCI6MTY3NzYxMjc2NSwic3ViIjoiZGV2ZWxvcGVyLzc3YWQ4NGY3LTFjNzItNjMwOC0yY2Y3LTliOGRkN2E3OTYw' \
          'ZCIsInNjb3BlcyI6WyJyb3lhbGUiXSwibGltaXRzIjpbeyJ0aWVyIjoiZGV2ZWxvcGVyL3NpbHZlciIsInR5cGUiOiJ0aHJvdHRsaW5n' \
          'In0seyJjaWRycyI6WyIyLjIwNS4xMS4yNDUiXSwidHlwZSI6ImNsaWVudCJ9XX0.7DuDrCFsJj-6gGj15I0hW6CsT2XX7tN5GVbphfT' \
          'YwldBk7aDqs9c-JZHDVcWSfivZt9TJ9AaPGSHegDDrj68nw'


def get_clans_tags_above_score(api_key: str, min_score: int) -> list:
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
clan_tags_with_score_above = get_clans_tags_above_score(api_key, min_score)
print(f"Retrieved {len(clan_tags_with_score_above)} Clan tags with score above {min_score}")
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
decoded_players_tags_list = decoding_players_tags(player_tags)
print(f"Decoded {len(decoded_players_tags_list)} players tags.")
print("_____")


def get_player_stats(tag: str, api_key: str) -> dict:
    url = f"https://api.clashroyale.com/v1/players/{tag}/"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Accept": "application/json"
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        player_tag = data['tag']
        player_name = data['name']
        wins = data['wins']
        losses = data['losses']
        battle_count = data['battleCount']
        sum_wins_losses = wins + losses
        net_win_rate = round(wins / sum_wins_losses * 100, 2)
        net_loss_rate = round(100 - net_win_rate, 2)
        win_rate_with_discrepancy = round((wins / battle_count) * 100, 2)
        loss_rate_with_discrepancy = round(100 - win_rate_with_discrepancy, 2)
        discrepancy_games = battle_count - sum_wins_losses
        discrepancy_pct = round(((battle_count - sum_wins_losses) / battle_count) * 100, 2)

        return {
            'player_tag': player_tag,
            'name': player_name,
            'battle_count': battle_count,
            'net_win_rate': net_win_rate,
            'net_loss_rate': net_loss_rate,
            'win_rate_with_discrepancy': win_rate_with_discrepancy,
            'loss_rate_with_discrepancy': loss_rate_with_discrepancy,
            'discrepancy_games': discrepancy_games,
            'discrepancy_pct': discrepancy_pct
        }

    else:
        raise ValueError(f"Error Code for Player {tag}: {response.status_code}")


player_tags = decoded_players_tags_list
player_stats_dict = []
for tag in player_tags:
    player_stats = get_player_stats(tag, api_key)
    player_stats_dict.append(player_stats)

# for player in player_stats_dict:
#     print(f"Player tag: {player['player_tag']}")
#     print(f"Player name: {player['name']}")
#     print(f"Battle count: {player['battle_count']}")
#     print(f"Discrepancy : {player['discrepancy_pct']}%")
#     print(f"Net win rate: {player['net_win_rate']:.2f}%")
#     print(f"Net loss rate: {player['net_loss_rate']:.2f}%")
#     print("\n_______________________")
# print("player_stats_dict: ", player_stats_dict)
# print("_____")
print("Now insert to MySQL")


def insert_player_stats_to_mysql(player_stats_list: list) -> None:
    try:
        # establish a connection to the MySQL database
        cnx = mysql.connector.connect(
            user='root',
            password='2020$2020$ABC',
            host='127.0.0.1',
            database='clash_royale_database'
        )

        print("Connection to MySQL database successful!")
        cursor = cnx.cursor()

        # iterate over the list of player stats and insert each player's data into the table
        for player_data_sql in player_stats_list:
            # construct the SQL statement to insert the data
            add_player = ("INSERT INTO player_stats "
                          "(player_tag, name, battle_count, net_win_rate, net_loss_rate, "
                          "win_rate_with_discrepancy, loss_rate_with_discrepancy, "
                          "discrepancy_games, discrepancy_pct) "
                          "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)")

            # execute the SQL statement with the data for the current player
            data = (player_data_sql['player_tag'], player_data_sql['name'], player_data_sql['battle_count'],
                    player_data_sql['net_win_rate'], player_data_sql['net_loss_rate'],
                    player_data_sql['win_rate_with_discrepancy'],
                    player_data_sql['loss_rate_with_discrepancy'], player_data_sql['discrepancy_games'],
                    player_data_sql['discrepancy_pct'])
            cursor.execute(add_player, data)

        # commit the changes to the database and close the cursor and connection
        cnx.commit()
        cursor.close()
        cnx.close()

    except mysql.connector.Error as error:
        print("Connection to MySQL database failed! Error code: {}".format(error.errno))


insert_player_stats_to_mysql(player_stats_dict)
print("_____")


print("Done!")
end_time = time.time()
elapsed_time_min = (end_time - start_time)/60
print(f"Elapsed time: {elapsed_time_min:.2f} minutes")


exit()
