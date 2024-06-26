# Write your solution here
import json

def open_file():
    hockey_stats = input('File name: ')
    #hockey_stats = 'partial.json'
    with open (hockey_stats) as file:
        data = file.read()
    players = json.loads(data)
    print (f'read the data of {len(players)} players')
    return players

def instructions():
    print('commands:')
    print('0 quit')
    print('1 search for player')
    print('2 teams')
    print('3 countries')
    print('4 players in team')
    print('5 players from country')
    print('6 most points')
    print('7 most goals')

def list_by(search_parameter, player_db):
    players = find_players(search_parameter, player_db)
    players.sort(key= lambda x: x["goals"]+x["assists"], reverse=True)
    [print_stats(player) for player in players]

def teams(player_db):
    players_teams = set([player["team"] for player in player_db])
    [print(player) for player in sorted(players_teams)]

def countries(player_db):
    players_teams = set([player["nationality"] for player in player_db])
    [print(player) for player in sorted(players_teams)]

def most_points(player_db):
    amount = int(input("how many: "))
    player_db.sort(key= lambda x:(x["goals"]+x["assists"], x["goals"]), reverse=True)
    most_points_players = player_db[:amount]
    [print_stats(player) for player in most_points_players]

def most_goals(player_db):
    amount = int(input("how many: "))
    player_db.sort(key= lambda x:(x["goals"], -x["games"]), reverse=True)
    most_points_players = player_db[:amount]
    [print_stats(player) for player in most_points_players]

def main():
    player_db = open_file()
    instructions()
    while True:
        command = int(input('command: '))
        if command == 0:
            break

        elif command == 1:
            player = input('name: ')
            list_by(player, player_db)

        elif command ==2:
            teams(player_db)
        
        elif command == 3:
            countries(player_db)
        
        elif command == 4:
            team = input('team: ')
            list_by(team, player_db)
        
        elif command == 5:
            country = input('country: ')
            list_by(country, player_db)

        elif command == 6:
            most_points(player_db)
        
        elif command == 7:
            most_goals(player_db)

def find_players(looked_stat, file):
    return [player for player in file if (player['name'] == looked_stat or player['nationality'] == looked_stat or player['team'] == looked_stat)]

def print_stats(player: dict):
    name = player['name']
    team = player['team']
    goals = str(player['goals'])
    assists = str(player['assists'])
    total = str(int(goals) + int(assists))

    print(f'{name}{" "*(21 - len(name))}{team}{" " * (4 - len(goals))}{goals} +{" " * (3-len(assists))}{assists} ={" " * (4 - len(total))}{total}')

main()