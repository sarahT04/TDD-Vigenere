def check_upper(char: str) -> bool:
    """
    return True if there's an uppercase -> has to be a char
    """
    return char.isupper()


def check_num_in_char(char: str) -> bool:
    """
    return True if theres num in char -> has to be a char
    """
    return char.isdigit()


def check_spec_char(char: str) -> bool:
    """
    returns True if special characters
    ~`! @#$%^&*()_+|}{:?><,./;[]\\=-'\""=
    -> has to be a char
    """
    spec_char = " ~`!@#$%^&*()_+|}{:?><,./;[]\\=-'\""
    return char in spec_char


def check_ascii(char: str) -> bool:
    """
    returns True if ascii -> has to be a char
    """
    try:
        char.encode('ascii')
        return True
    except UnicodeEncodeError as e:
        return False


# <--->


def check_len(password: str) -> bool:
    """
    returns True if len pass is above 7 -> has to be a string
    """
    return len(password) > 7


def check_chars(password: str) -> bool:
    """
    returns True if there's more than 3 alphabets and less than 6 nums -> has to be a string
    """
    is_alpha = sum(passw.isalpha() for passw in password)
    nums_amount = sum(check_num_in_char(passw) for passw in password)
    return True if (is_alpha > 3 and nums_amount < 5) else False


def check_requirement_pass(password: str) -> bool:
    truth = [False, False, False, False]
    for chars in sorted(set(password)):
        if False not in truth:
            return True
        if truth[0] is False:
            if check_num_in_char(chars):
                truth[0] = True
        if truth[1] is False:
            if check_spec_char(chars):
                truth[1] = True
        if truth[2] is False:
            if check_upper(chars):
                truth[2] = True
        if truth[3] is False:
            if check_ascii(chars):
                truth[3] = True
    return True if False not in truth else False


def check_password(password: str) -> bool:
    password_check_functions = [check_chars(password), check_len(password), check_requirement_pass(password)]
    if False in password_check_functions:
        if password_check_functions[1] is False:
            print('Please enter a password of len above 7')
            return False  # Len not 7
        if password_check_functions[0] is False:
            print('Please enter password with number less than 6 and has 4 alphabets.')
            return False  # Alphabets < 4, num > 6
        if password_check_functions[2] is False:
            print('Please use at least 1 uppercase, ascii, number, and special character in your password.')
            return False  # Requirements not met.
    return True
