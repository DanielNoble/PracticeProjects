#  Strong password: 8+ characters, upper + lower letters, 1+ num

import re


def strengthDetection(password):
    try:
        length = re.compile(r'\S{8,20}')
        if length.search(password).group() is not None:
            lower = re.compile(r'[a-z]+')
            upper = re.compile(r'[A-Z]+')
            if lower.search(password).group() and upper.search(password).group() is not None:
                num = re.compile(r'\d')
                if num.search(password).group() is not None:
                    return True
    except Exception as exc:
        return False


password = input('Input password: ')
if strengthDetection(password):
    print(password + ' is a strong password')
else:
    print(password + ' is not a strong password')