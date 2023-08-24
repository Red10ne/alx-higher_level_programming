#!/usr/bin/python3
def remove_char_at(str, n):
    for char in str:
        remchar = str[:n] + str[n + 1:]
    return (remchar)
