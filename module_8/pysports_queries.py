

# Jeffrey Martinez
# April 21, 2022
# Module 8.3 Assignment


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
        
        
# Module 8.3 Assignment
# Assignment: PySports: Table Queries
# For this assignment, you will be learning how to query MySQL database tables through the terminal window and a Python program.

# In order to query I have to make sure to create a new table for player and insert some teams and players
# Resource: https://www.w3schools.com/python/python_mysql_insert.asp

cursor = db.cursor()

# Create Team Table
cursor.execute("CREATE TABLE team (team_id INT NOT NULL AUTO_INCREMENT, team_name VARCHAR(75) NOT NULL, mascot VARCHAR(75) NOT NULL, PRIMARY KEY(team_id))")
# print("Team Table Successfully Created\n")


# Create Player Table Resource: https://www.w3schools.com/python/python_mysql_create_table.asp
cursor.execute("CREATE TABLE player (player_id INT NOT NULL AUTO_INCREMENT, first_name VARCHAR(75) NOT NULL, last_name VARCHAR(75) NOT NULL, team_id INT NOT NULL, PRIMARY KEY(player_id), CONSTRAINT fk_team FOREIGN KEY(team_id) REFERENCES team(team_id))")
# print("Player Table Successfully Created \n")




# Insert Statements for Team Table
sql = "INSERT INTO team (team_name, mascot) VALUES (%s, %s)"
val = [
    ("Team Gandalf", "White Wizards"),
    ("Team Sauron", "Orcs")
]
cursor.executemany(sql, val)
db.commit()
# print("Teams succesfully inserted.\n")



# Insert Statements for Player Table
sql = "INSERT INTO player (player_id, first_name, last_name, team_id) VALUES (%s, %s, %s, %s)"
val = [
    (1, "Thorin", "Oakenshield", 1),
    (2, "Bilbo", "Baggins", 1),
    (3, "Frodo", "Baggins", 1),
    (4, "Saruman", "The White", 2),
    (5, "Angmar", "Witch-king", 2),
    (6, "Azog", "The Defiler", 2)
]
cursor.execute("SET FOREIGN_KEY_CHECKS=0")
cursor.executemany(sql, val)
db.commit()
# print("Players succesfully inserted.\n")
# Couldn't insert due to the CONSTRAINT and FOREIGN KEY, so I added check to be 0. Used this Resource: https://stackoverflow.com/questions/38898601/bypass-known-exception-of-mysql-in-python
    
    
    
    
    
# Delete Statements for Individual Team (Had Duplicates)
# sql = "DELETE FROM team WHERE team_name = 'Team Sauron'"
# cursor.execute(sql)
# db.commit()
# print("Successfully record(s) deleted")




# Selecting Statements for the team
print("\n- -DISPLAYING TEAM RECORDS - -\n")
cursor.execute("SELECT team_id, team_name, mascot FROM team")
teams = cursor.fetchall()
for team in teams:
    print(f"Team ID: {team[0]}")
    print(f"Team Name: {team[1]}")
    print(f"Mascot: {team[2]}\n")


# Selecting Statements for the player
print("\n- -DISPLAYING PLAYER RECORDS - -\n")
cursor.execute("SELECT player_id, first_name, last_name, team_id FROM player")
players = cursor.fetchall()
for player in players:
    print(f"Player ID: {player[0]}")
    print(f"First Name: {player[1]}")
    print(f"Last Name: {player[2]}")
    print(f"Team ID: {player[3]}\n")
    
    
    
# Delete Team and Player Tables
cursor.execute("DROP TABLE IF EXISTS player")
cursor.execute("DROP TABLE IF EXISTS team")
print("Both Tables have been successfully dropped!\n")
