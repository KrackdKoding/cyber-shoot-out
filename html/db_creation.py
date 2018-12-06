"""
#sqlite3 "CREATE TABLE Scores( id INT(8) UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
          name VARCHAR(30) NOT NULL DEFAULT 'Anonymous',
          score INT(5) NOT NULL DEFAULT '0',
          ts TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
          device VARCHAR(10) NOT NULL);"
"""
import sqlite3

# create connection variable to database,
# since no database exists, it will create one
conn = sqlite3.connect('score.db')

# creates a cursor to interact with the db
c = conn.cursor()

# using the cursor to create the table
# this table will have record number,
# position, and date columns
c.execute("""CREATE TABLE Scores(
                id INTEGER PRIMARY KEY AUTOINCREMENT, 
                name VARCHAR(30) NOT NULL DEFAULT 'Anonymous', 
                score integer NOT NULL DEFAULT '0', 
                ts DATETIME NOT NULL DEFAULT (DATETIME('now', 'localtime')), 
                device VARCHAR(10) NOT NULL)""")

# this sends the commands to the db
# and saves the table
conn.commit()

# closes connection
conn.close()