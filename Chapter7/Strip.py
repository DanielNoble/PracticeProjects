#  Strip.py - removes the whitespace or specified set of characters around a string

import re

userString = input('The String you\'d like to strip: ')
toStrip = input('The characters you\'d like to strip')


def strip(string, remove):
    if remove == '':
        print(re.compile(r'[^\s][\w]+[^\s]').search(string).group())
    else:
        print(re.compile(r'[' + remove + ']').sub('', string))


strip(userString, toStrip)
