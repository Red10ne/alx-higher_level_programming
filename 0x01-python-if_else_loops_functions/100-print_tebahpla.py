#!/usr/bin/python3
for i in range(25, -1, -1):
    if i % 2 == 0:
        print(chr(i + ord('a')).upper(), end='')
    else:
        print(chr(i + ord('a')).lower(), end='')
