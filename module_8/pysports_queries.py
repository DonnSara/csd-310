import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="pysports_user",
    password="MySQL8IsGreat!",
    database = "pysports"
)

cursor = db.cursor()

cursor.execute("SELECT team_id, team_name, mascot FROM team")

teams = cursor.fetchall()

print("- - DISPLAYING TEAM RECORDS - -")

for team in teams:
    print("Team ID: {}".format(team[0]))
    print("Team Name: {}".format(team[1]).title())  
    print("Mascot: {}".format(team[2]).title())   
    print("")


cursor.execute("SELECT player_id, first_name, last_name, team_id FROM player")

players = cursor.fetchall()

print("\n- - DISPLAYING PLAYER RECORDS - -")

for player in players:
    print("Player ID: {}".format(player[0]))
    print("First Name: {}".format(player[1]).title())
    print("Last Name: {}".format(player[2]).title())
    print("Team ID: {}".format(player[3]))
    print("")
    
input("\n\nPress any key to continue... ")
