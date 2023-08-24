#!/usr/bin/python3
def uppercase(str):
    uppstr = ""
    for char in str:
        if 'a' <= char <= 'z':
            uppercase = chr(ord(char) - ord('a') + ord('A'))
        else:
            uppercase = char
        uppstr += uppercase
    print(uppstr)
