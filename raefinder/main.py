#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re, sys, os, time
from unidecode import unidecode
from .mnemo import MNEMOTECNIC_2 as MNEMOTECNIC

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DEFAULT_DICT = BASE_DIR+ '/dictionaries/rae.txt'
VOWELS = '[aeiou]*'


def safe_number(number):
    number = str(number)
    if not number.isdigit():
        raise ValueError('The number must be numeric')
    else:
        return number


def build_regex(number, mnemo=False):
    number = safe_number(number)

    # Set default mnemo
    if not mnemo:
        mnemo = MNEMOTECNIC

    # Build regex
    regex = VOWELS
    for c in number:
        # Prep regex for chars and strings
        list_c = []
        list_d = []
        for val in mnemo[int(c)]:
            if len(val) == 1:
                list_c.append(val)
            else:
                list_d.append(val)

        # Build regex
        prep_c = '[' + ''.join(list_c) + ']' if list_c else ''
        prep_d = '|' + '|'.join(list_d) if list_d else ''
        regex += '(' + prep_c + prep_d + ')' + VOWELS
    return '^' + regex + '$'


def get_words(number, mnemo=False, file=None, print_w=False):
    if not file:
        file = os.path.join(os.path.dirname(__file__), DEFAULT_DICT)

    try:
        # Create specific regex
        regex = build_regex(number, mnemo)

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
    words_matched, total_lines, regex = get_words(number, file=file, print_w=True)
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

