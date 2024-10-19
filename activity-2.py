import sqlite3
database = 'activity-2.sqlite'
conn = sqlite3.connect(database)
import pandas as pd
tables = pd.read_sql("""SELECT * FROM sqlite_master WHERE type='table';""",conn)
tables.info()
teams = pd.read_sql("""SELECT * FROM TEAM;""", conn)
teams.info()
matches = pd.read_sql("""SELECT * FROM Match;""", conn)
matches.info()
MI_wins = pd.read_sql("""SELECT * FROM Match WHERE Match_Winner==7; """, conn)
MI_wins.info()
MI_S8_S9 = pd.read_sql("""SELECT * FROM Match WHERE Match_Winner == 7 and Season_Id IN (8,9);""",conn)
MI_S8_S9.info()
new_teams = pd.read_sql("""SELECT * FROM Team WHERE Team_Name LIKE 'De%';""", conn)
new_teams.info()
min_max_margin = pd.read_sql("""SELECT MIN(Win_Margin), MAX(Win_Margin) FROM Match;""", conn)
min_max_margin.info()