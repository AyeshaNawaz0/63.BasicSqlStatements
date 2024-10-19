import sqlite3
database = 'project.sqlite'
con = sqlite3.connect(database)
import pandas as pd
tables = pd.read_sql("""SELECT * FROM sqlite_master WHERE type='table';""", con)
tables.info()
player= pd.read_sql("""SELECT* FROM Player;""",con)
player.info()
teams= pd.read_sql("""SELECT* FROM Team;""",con)
teams.info()
state= pd.read_sql("""SELECT* FROM Team WHERE state== 'California';""",con)
state.info()
state_year= pd.read_sql("""SELECT* FROM Team WHERE state=='California' and year_founded IN (1970,1948);""",con)
state_year.info()
min_max= pd.read_sql("""SELECT MIN(id), MAX(id) FROM Player;""",con)
min_max.info()