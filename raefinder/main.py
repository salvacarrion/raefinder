#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re, sys, os, time
from unidecode import unidecode

DEFAULT_DICT = '../dictionaries/rae.txt'
VOWELS = '[aeiou]*'
MNEMOTECNIC = {1: ['d', 't'],
               2: ['n', 'ñ', 'y'],
               3: ['m', 'w'],
               4: ['c', 'h', 'k', 'q'],
               5: ['l', 'v', 'll'],
               6: ['s', 'z'],
               7: ['f', 'j'],
               8: ['g', 'x', 'ch'],
               9: ['b', 'p'],
               0: ['r', 'rr']}


def safe_number(number):
    number = str(number)
    if not number.isdigit():
        raise ValueError('The number must be numeric')
    else:
        return number


def build_regex(number):
    number = safe_number(number)

    # Build regex
    regex = VOWELS
    for c in number:
        # Prep regex for chars and strings
        list_c = ''
        list_d = []
        for val in MNEMOTECNIC[int(c)]:
            if len(val) == 1:
                list_c += val
            else:
                list_d.append(val)

        prep_d = ''
        if list_d: prep_d = '|' + '|'.join(list_d)

        regex += '([' + list_c + ']' + prep_d + ')' + VOWELS
    return '^' + regex + '$'


def get_words(number, file=None, print_w=False):
    if not file:
        file = os.path.join(os.path.dirname(__file__), DEFAULT_DICT)

    try:

        # Create specific regex
        regex = build_regex(number)

        # Find words
        total_lines = 0
        words_matched = []
        with open(file, 'r', encoding='utf8') as f:
            for line in f:
                total_lines += 1
                unaccented_line = unidecode(line)  # Strip accents
                # Match expression
                if re.search(regex, unaccented_line):
                    line_matched = line.strip()
                    words_matched.append(line_matched)
                    if print_w: print(line_matched)

        return words_matched, total_lines, regex
    except IOError as e:
        print(e)


def print_words(number, file=None):
    print('-----------------------------')
    print('--        RAEFINDER        --')
    print('-----------------------------')

    # Find words
    start_t = time.time()
    words_matched, total_lines, regex = get_words(number, file, print_w=True)
    end_t = time.time() - start_t

    # Print results
    if len(words_matched):
        print('\n-------------------------------')
        print('- Words matched: {:,}'.format(len(words_matched)))
        print('- Words analyzed: {:,}'.format(total_lines))
        print('- Elapsed time: %.5fs' % end_t)
        print('- Regex used: "%s"' % regex)
    else:
        print('No words matched the expression')


def main():
    try:
        arg1 = str(sys.argv[1])
        if arg1.isdigit():
            print_words(*sys.argv[1:])
        elif arg1 == '-m':
            print(MNEMOTECNIC)
        else:
            raise IndexError
    except IndexError as e:
        print('(number)\tTo retrive matching words from DRAE\n'
              '-h\t\tTo list all available options\n'
              '-m\t\tTo see mnemotecnics used')


if __name__ == '__main__':
    main()

