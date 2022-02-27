from PASS.password_check import check_spec_char, check_num_in_char


def key_repeater(text_len: int, key: str) -> str:
    """
    :param text_len: Length of times it want to repeat itself
    :param key: The word that wants to be repeated
    :return: A word that's repeated of length text_len (KEYKEYKEYKEYKEY)
    """
    key_str = (key * (text_len // len(key))) + key[: (text_len % len(key))]
    return key_str


def cipher_text(text: str, key: str) -> str:
    """
    :param text: The plaintext that wants to be ciphered 
    :param key: The key for the cipher
    :return: Vigenere Ciphered plaintext
    """
    new_text = text.upper()
    new_key = key_repeater(len(new_text), key)
    ciphered_text = []
    for i in range(len(text)):
        # Ciphering process
        x = (ord(new_text[i]) + ord(new_key[i])) % 26
        x += ord('A')
        # If is spec char, it's going to make the encryption more complex. So we are not decrypting it.
        # But numbers are decrypted.
        if check_spec_char(text[i]) or check_num_in_char(text[i]):
            try:
                # Cipher the num
                ciphered_text.append(encrypt_num(int(text[i])))
            except ValueError:
                # Else clause, must be spec character, append the plain character
                ciphered_text.append(text[i])
            # If it was a number or spec character, it has been decrypted so we pass the loop.
            continue
        elif text[i].isupper():
            ciphered_text.append(chr(x).upper())
        else:
            ciphered_text.append(chr(x).lower())
    return ''.join(ciphered_text)


def decrypt_cipher(text: str, key: str) -> str:
    """
    :param text: text to be decrypted
    :param key: key for decryption
    :return: decrypted Vigenere text
    """
    new_text = text.upper()
    new_key = key_repeater(len(new_text) * 3 + 1, key)
    deciphered_text = []
    # Some additional variables
    skipped_loop = None
    real_index = 0
    for i in range(len(text)):
        if i == skipped_loop:
            real_index += len(key)
            continue
        x = (ord(new_text[i]) - ord(new_key[real_index]) + 26) % 26
        x += ord('A')
        real_index += 1
        # If special character, then append plain character.
        if check_spec_char(text[i]):
            deciphered_text.append(text[i])
            continue
        elif check_num_in_char(text[i]):
            try:
                # If it's 0 or 7 means it's gonna result 0 or 1 -> 1 digit num, also checks if next char is num
                if text[i] == '0' or text[i] == '7' or not check_num_in_char(text[i + 1]):
                    deciphered_text.append(decrypt_num(int(text[i])))
                elif check_num_in_char(text[i + 1]):
                    deciphered_text.append(decrypt_num(int(text[i:i + 2])))
                    skipped_loop = i + 1
            # We are at the end of encryption, the last digit of the password yknow.
            except IndexError:
                return ''.join(deciphered_text)
            continue
        elif text[i].isupper():
            deciphered_text.append(chr(x).upper())
        else:
            deciphered_text.append(chr(x).lower())
    return ''.join(deciphered_text)


def encrypt_num(number: int) -> str:
    return str(number * 7) if number != 0 else '0'


def decrypt_num(number: int) -> str:
    return str(int(number / 7)) if number != 0 else '0'
