import sqlite3
from DATA.data import database_path

# this was used to insert the data into sql


def create_table():
    conn = sqlite3.connect(database_path)
    create_users_table = """
    CREATE TABLE IF NOT EXISTS users (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      username TEXT NOT NULL,
      pass TEXT NOT NULL
    );
    """
    create_users = """
    INSERT INTO
      users (username, pass)
    VALUES
      (?, ?);
    """

    conn.execute(create_users_table)
    conn.commit()
    conn.close()

# insert_list_to_sql([['Paimon', 'Wysd73_dsjab']])
