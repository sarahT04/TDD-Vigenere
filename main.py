from db.dblookup import *
from PASS.password_check import check_password
from UNAME.uname_check import check_username
from CRYPT.cipher_vigenere import cipher_text
from DATA.data import key, key2

# Get user's choice (Login or Register)
user_input = input('Login or register?\n> ').lower()
# If login,
if user_input.startswith('log') or user_input == '1':
    username = input('Enter your username\n> ')
    # Checks inserted username in database
    if look_username(username):
        password = input('Enter your password\n> ')
        # Checks inserted username + password in database
        if look_password(username, password):
            print("Welcome, you are logged in!")
        else:
            print("Invalid password.")
    else:
        print("Username doesn't exist.")
# If register,
elif user_input.startswith('reg') or user_input == '2':
    username = input('Enter your username\n> ')
    # If username doesn't exist
    if not look_username(username):
        if check_username(username):
            password = input('Enter your password\n> ')
            # Check whether password is valid or not
            if check_password(password):
                # Encrypts it twice
                encrypted_password = cipher_text(password, key)
                encrypted_password_2 = cipher_text(encrypted_password, key2)
                # Insert it to SQL.
                insert_list_to_sql([[username, encrypted_password_2]])
    else:
        print("Username exists. Please try another one.")
else:
    print("Invalid command.")
