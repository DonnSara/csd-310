import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="pysports_user",
    password="MySQL8IsGreat!",
    database = "pysports"
)

cursor = db.cursor()

cursor.execute("INSERT INTO player (first_name, last_name, team_id) VALUES('Smeagol', 'Shire Folk', 1)");

cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id=team.team_id");

teams = cursor.fetchall()

print("\n- - DISPLAYING PLAYERS AFTER INSERT - -")

for team in teams:
    print("Player ID: {}".format(team[0]))
    print("First Name: {}".format(team[1]).title())  
    print("Last Name: {}".format(team[2]).title())   
    print("Team Name: {}".format(team[3]).title())   
    print("")
    
cursor.execute("UPDATE player SET team_id = 2, first_name = 'Gollum', last_name = 'Ring Stealer' WHERE first_name = 'Smeagol'");

cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id=team.team_id");

teams = cursor.fetchall()

print("\n- - DISPLAYING PLAYERS AFTER UPDATE - -")

for team in teams:
    print("Player ID: {}".format(team[0]))
    print("First Name: {}".format(team[1]).title())  
    print("Last Name: {}".format(team[2]).title())   
    print("Team Name: {}".format(team[3]).title())   
    print("")
    
cursor.execute("DELETE FROM player WHERE first_name = 'Gollum'");

print("\n- - DISPLAYING PLAYERS AFTER DELETE - -")

cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id=team.team_id");

teams = cursor.fetchall()

for team in teams:
    print("Player ID: {}".format(team[0]))
    print("First Name: {}".format(team[1]).title())  
    print("Last Name: {}".format(team[2]).title())   
    print("Team Name: {}".format(team[3]).title())   
    print("")
    
input("\nPress any key to continue... ")
