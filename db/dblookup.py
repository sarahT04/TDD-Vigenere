import sqlite3
from CRYPT.cipher_vigenere import cipher_text
from DATA.data import key, key2, database_path

conn = sqlite3.connect(database_path)
cursor = conn.cursor()


def look_username(username: str) -> bool:
    """
    :param username: username to be checked
    :return: True if username is in database
    """
    cursor.execute(f"SELECT * from users where username = '{username}';")
    if cursor.fetchone() is None:
        return False
    return True


def look_password(username: str, password: str) -> bool:
    """
    :param username: username to be checked
    :param password: password to be checked
    :return: returns True if username and password matches
    """
    encrypted_pass = cipher_text(password, key)
    encrypted_pass_2 = cipher_text(encrypted_pass, key2)
    cursor.execute(f"SELECT * from users where username = '{username}'"
                   f"AND pass = '{encrypted_pass_2}';")
    if cursor.fetchone() is None:
        return False
    return True


def insert_list_to_sql(user_pass_list: list) -> None:
    """
    :param user_pass_list: [['username', 'password]] format.
    :return: the list inserted into database
    """
    try:
        for i in user_pass_list:
            user, passw = i
            conn.execute(f"INSERT INTO users (username, pass) VALUES ('{user}', '{passw}');")
            conn.commit()
    except Exception as e:
        print("ERROR" + str(e))
    conn.close()
