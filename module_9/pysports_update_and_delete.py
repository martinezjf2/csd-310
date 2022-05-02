

# Jeffrey Martinez
# Module 9.3 Assignment
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

        
# Insert Statements for Player Table
sql = "INSERT INTO player (player_id, first_name, last_name, team_id) VALUES (%s, %s, %s, %s)"
val = (21, "Smeagol", "Shire Folk", 1)
cursor.execute("SET FOREIGN_KEY_CHECKS=0")
cursor.execute(sql, val)
db.commit()
# print("Player succesfully inserted.\n")
        
        
# Selecting Statements for the player
print("\n- -DISPLAYING PLAYER AFTER INSERT - -\n\n")
cursor.execute("SELECT Player.player_id, Player.first_name, Player.last_name, Team.team_name FROM player INNER JOIN Team ON Player.team_id = Team.team_id")
players = cursor.fetchall()
for player in players:
    print(f"Player ID: {player[0]}")
    print(f"First Name: {player[1]}")
    print(f"Last Name: {player[2]}")
    print(f"Team ID: {player[3]}\n\n")
    
    
    
# Update Statments for the player
# Resource: https://www.w3schools.com/sql/sql_update.asp
sql = "UPDATE player SET team_id = 2 WHERE player_id = 21"
cursor.execute(sql)
db.commit()
# print("Player succesfully updated.\n")


# Displaying Statements for the Updated player
print("\n- -DISPLAYING PLAYER AFTER UPDATE - -\n\n")
cursor.execute("SELECT Player.player_id, Player.first_name, Player.last_name, Team.team_name FROM player INNER JOIN Team ON Player.team_id = Team.team_id")
players = cursor.fetchall()
for player in players:
    print(f"Player ID: {player[0]}")
    print(f"First Name: {player[1]}")
    print(f"Last Name: {player[2]}")
    print(f"Team ID: {player[3]}\n\n")
    
    
    
    
# Delete Specific Player from Player Table: https://www.w3schools.com/python/python_mysql_delete.asp
cursor.execute("DELETE FROM player WHERE player_id = 21")
db.commit()


# Displaying Statements Adter the Deletion
print("\n- -DISPLAYING PLAYER AFTER DELETE - -\n\n")
cursor.execute("SELECT Player.player_id, Player.first_name, Player.last_name, Team.team_name FROM player INNER JOIN Team ON Player.team_id = Team.team_id")
players = cursor.fetchall()
for player in players:
    print(f"Player ID: {player[0]}")
    print(f"First Name: {player[1]}")
    print(f"Last Name: {player[2]}")
    print(f"Team ID: {player[3]}\n")

