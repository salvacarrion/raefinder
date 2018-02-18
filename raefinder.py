#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re, sys, os

FILE = os.path.join(os.path.dirname(__file__), 'rae.txt')
vowels = '[a,e,i,o,u]*'
mnemotecnic = {1: ['d', 't'],
               2: ['n', 'ñ'],
               3: ['m', 'w'],
               4: ['c', 'h', 'k', 'q'],
               5: ['l', 'v'],  # Includes 'll'
               6: ['s', 'z'],
               7: ['f', 'j'],
               8: ['g', 'x'],
               9: ['b', 'p'],
               0: ['r']}  # Includes 'rr'
# Excluded: y

arg1 = str(sys.argv[1])
total_found = 0
try:

    if arg1.isdigit():
        number = arg1
        regex = vowels
        for c in number:
            regex += '[' + ''.join(mnemotecnic[int(c)]) + ']' + vowels

        for line in open(FILE, 'r', encoding='utf8'):
            if re.search('^' + regex + '$', line):
                total_found += 1
                print(line.strip())

        if total_found:
            print('\n-------------------------------')
            print('Total results: ' + str(total_found))
        else:
            print('No words matched the expression')
    else:
        if arg1 == '-h':
            print('(number)\tTo retrive matching words from DRAE\n'
                  '-h\t\tTo list all available options\n'
                  '-m\t\tTo see mnemotecnics used')
        elif arg1 == '-m':
            print(mnemotecnic)
        else:
            print("The number is not numeric")

except Exception as e:
    print("There's been a problem!\nError: " + str(e))
