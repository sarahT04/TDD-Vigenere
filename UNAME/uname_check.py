from PASS.password_check import check_num_in_char, check_upper


def check_if_spec_char_dangerous(char: str) -> bool:
    """
    return True if ' \|?[]{}<>()" in char -> has to be a char
    """
    spec_char = " \\|?[]{}<>()\'\""
    return char in spec_char


def check_len(password: str) -> bool:
    """
    return True if username len > 6  -> has to be a char
    """
    return len(password) > 5


def check_requirement_uname(password: str) -> bool:
    truth = [False, False, False]
    for chars in sorted(set(password)):
        if False not in truth:
            return True
        if truth[0] is False:
            if check_num_in_char(chars):
                truth[0] = True
        if truth[1] is False:
            if not check_if_spec_char_dangerous(chars):
                truth[1] = True
        if truth[2] is False:
            if check_upper(chars):
                truth[2] = True
    return True if False not in truth else False


def check_username(password: str) -> bool:
    password_check_functions = [check_len(password), check_requirement_uname(password)]
    if False in password_check_functions:
        if password_check_functions[0] is False:
            print('Please enter username of len above 6')
            return False  # len not 6
        else:
            print('Please use at least 1 uppercase, number, and not dangerous special character')
            return False  # requirements not met
    return True
