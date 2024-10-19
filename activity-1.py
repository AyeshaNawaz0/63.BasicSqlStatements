import sqlite3
conn = sqlite3.connect("activity-1.sqlite")
import pandas as pd 
tables = pd.read_sql("""SELECT * 
                     FROM sqlite_master WHERE type='table';""",conn )
matches = pd.read_sql("""SELECT * FROM Match;""", conn)
matches.info()
