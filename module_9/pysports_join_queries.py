

# Jeffrey Martinez
# Module 9.2 Assignment
# April 27, 2022


# Import Statements

import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "pysports_user",
    "password": "MySQL8IsGreat",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}

# db = mysql.connector.connect(**config)

try:
    db = mysql.connector.connect(**config)
    
    print("\nDatabase user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))
    input("\n\nPress any key to continue...\n\n")
    
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("The supplied username or password are invalid")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("The specified database does not exist")
    else:
        print(err)
        
cursor = db.cursor()

# Using the output I have provided and the sample queries, create an INNER JOIN query to connect the player and team tables by team_id and display the results.

#Inner Join
print("\n- -DISPLAYING PLAYER RECORDS - -\n")
# cursor.execute("SELECT player_id, first_name, last_name, team_id FROM player")
cursor.execute("SELECT Player.player_id, Player.first_name, Player.last_name, Player.team_id, Team.team_name FROM player INNER JOIN Team ON Player.team_id = Team.team_id")
players = cursor.fetchall()
# print(players)
for player in players:
    print(f"Player ID: {player[0]}")
    print(f"First Name: {player[1]}")
    print(f"Last Name: {player[2]}")
    print(f"Team Name: {player[4]}\n")  
input("\n\nPress any key to continue...\n\n")
