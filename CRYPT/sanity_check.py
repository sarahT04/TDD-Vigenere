from CRYPT.cipher_vigenere import *
from PASS.password_check import check_password
from DATA.data import key, key2, filename_pass, filename_uname


def check_vigenere(text: str, key: str, printf: bool = False) -> bool:
    """
    :param text: text to be encrypted
    :param key: key of encryption
    :param printf: if True, will print result
    :return: bool whether is correct or not
    """
    cipher = cipher_text(text, key)
    if printf: print("Encrypted", cipher)
    try:
        decrypt = decrypt_cipher(cipher, key)
        if printf: print("Decrypted", decrypt)
        return True if decrypt == text else False
    except ValueError as e:
        if printf: print("Error:", e)
        return False


def extract_file(filename: str, n: int = 10) -> list:
    """
    :param filename: filename
    :param n: until what line want to be extracted
    :return: list of extracted string, also made sure to be in ascii format
    """
    with open(filename, 'r', encoding='utf-8') as f:
        new_list = []
        f = f.readlines()[:n]
        for i in f:
            try:
                i.encode('ascii')
                new_list.append(i.strip())
            except UnicodeEncodeError as e:
                pass
                # print('Unicode error for', i)
    return new_list


def check_correctness(passwords: list, key: str, key2: str, printf: bool = False) -> list:
    """
    :param passwords: list of passwords
    :param key: key to be checked
    :param key2: second key
    :param printf: will print result if true
    :return: a list of things that are wrong
    """
    point = 0
    wrong_list = []
    for i in passwords:
        truth = check_double_vigenere(i, key, key2)
        if printf: print("Password:", i, "Condition:", truth)
        if truth is True:
            point += 1
        else:
            wrong_list.append(i)
    if printf: print(f"Correct: {point}/{len(passwords)}: {int(point / len(passwords) * 100)}")
    return wrong_list


def write_txt(filename: str, wrongs: list) -> None:
    """
    :param filename: filename
    :param wrongs: list of thing to be written, format ['username', 'password']
    :return: nothing, but it will make a txt
    """
    with open(filename, 'w') as f:
        for i in wrongs:
            f.write(' '.join(i) + '\n')
    print('TXT Finished.')


def check_double_vigenere(text: str, key1: str, key2: str, printf: bool = False) -> bool:
    """
    :param text: text to be encrypted
    :param key1: first key
    :param key2: second key
    :param printf: should it print the result
    :return: bool, True if double vigenere same
    """
    try:
        first_enc = cipher_text(text, key1)
        second_enc = cipher_text(first_enc, key2)
        if printf:
            print(f"Encrypted, 1. {first_enc}, 2. {second_enc}")
        first_dec = decrypt_cipher(second_enc, key2)
        second_dec = decrypt_cipher(first_dec, key1)
        if printf:
            print(f"Decrypted, 1. {first_dec}, {second_dec}")
        if first_dec != first_enc:
            if printf:
                print("False")
            return False
        if second_dec == text:
            if printf:
                print("True")
            return True
        return False
    except (ValueError, IndexError) as e:
        if printf:
            print("Error:", e)
        return False


def extract_correct_users(usernames: list, passwords: list, key: str, key2: str) -> list:
    """
    :param usernames: list of usernames
    :param passwords: list of passwords
    :param key: key1
    :param key2: key2
    :return: list of correct username and password, encrypted
    """
    user_pass_l = []
    for user, passw in zip(usernames, passwords):
        if check_password(passw) is True:
            _ = check_double_vigenere(passw, key, key2)
            if _:
                encrypted_pass = cipher_text(passw, key)
                encrypted_pass_2 = cipher_text(encrypted_pass, key2)
                user_pass_l.append([user, encrypted_pass_2])
    return user_pass_l


# len = 38560, 703

passwords = (extract_file(filename_pass, 38560))
usernames = (extract_file(filename_uname, 38560))
print("Incorrectly encrypted passwords:", check_correctness(passwords, key, key2, True))
# print(extract_correct_users(usernames, passwords, key, key2))
