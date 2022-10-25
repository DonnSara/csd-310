import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="pysports_user",
    password="MySQL8IsGreat!",
    database = "pysports"
)

cursor = db.cursor()

cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id=team.team_id")

teams = cursor.fetchall()

print("\n- - DISPLAYING PLAYER RECORDS - -")

for team in teams:
    print("Player ID: {}".format(team[0]))
    print("First Name: {}".format(team[1]).title())  
    print("Last Name: {}".format(team[2]).title())   
    print("Team Name: {}".format(team[3]).title())   
    print("")
    
input("\nPress any key to continue... ")
