#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re, sys, os
from unidecode import unidecode

FILE = os.path.join(os.path.dirname(__file__), 'rae.txt')
vowels = '[aeiou]*'
mnemotecnic = {1: ['d', 't'],
               2: ['n', 'ñ'],
               3: ['m', 'w'],
               4: ['c', 'h', 'k', 'q'],
               5: ['l', 'v', 'll'],  # Includes 'll'
               6: ['s', 'z'],
               7: ['f', 'j'],
               8: ['g', 'x', 'ch'],
               9: ['b', 'p'],
               0: ['r', 'rr']}  # Includes 'rr'
# Excluded: y

arg1 = str(sys.argv[1])
total_found = 0
try:

    if arg1.isdigit():

        # Build regex
        number = arg1
        regex = vowels
        for c in number:
            list_c = ''
            list_d = []
            for val in mnemotecnic[int(c)]:
                if len(val) == 1: list_c += val
                else: list_d.append(val)

            prep_d = ''
            if list_d:
                prep_d = '|' + '|'.join(list_d)

            regex += '([' + list_c + ']' + prep_d + ')' + vowels

        # Find words
        for line in open(FILE, 'r', encoding='utf8'):
            unaccented_line = unidecode(line)  # Strip accents
            if re.search('^' + regex + '$', unaccented_line):
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
