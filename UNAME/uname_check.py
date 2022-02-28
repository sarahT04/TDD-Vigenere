from PASS.password_check import check_num_in_char, check_upper


def check_if_spec_char_dangerous(char: str) -> bool:
    spec_char = " \\|?[]{}<>()\'\""
    return char in spec_char


def check_len(username: str) -> bool:
    return len(username) > 5


def check_requirement_uname(username: str) -> bool:
    truth = [False, False, False]
    for char in sorted(set(username)):
        if False not in truth:
            return True
        if truth[0] is False:
            if check_num_in_char(char):
                truth[0] = True
        if truth[1] is False:
            if not check_if_spec_char_dangerous(char):
                truth[1] = True
        if truth[2] is False:
            if check_upper(char):
                truth[2] = True
    return True if False not in truth else False


def check_username(username: str) -> bool:
    if not check_len(username):
        print('Please enter username of len above 6')
        return False  # len not 6
    if not check_requirement_uname(username):
        print('Please use at least 1 uppercase, number, and not dangerous special character')
        return False  # requirements not met
    return True
