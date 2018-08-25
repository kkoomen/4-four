#! /usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Thanks to the wonderful mathematic explanation of Matt Parker in the video
https://www.youtube.com/watch?v=LYKn0yUTIU4 where he explained that the number
4 is the only number that has the same number of letters as its value in some
languages, such as DE, NL and EN. Because it is a fixed point, it doesn't go
anywhere because it maps to itself.

Matt explained that no matter what number you would take, it would always end
up at the number 4. So I wrote a script that uses his logic from the video in a
function that shows the output of the sequence to test wether it is true or
not.

Example run:

$ ./four.py 847193 en

[OUTPUT]
==============================
STARTING SEQUENCE
starting number => 847.193
==============================
847.193 => eight hundred and forty-seven thousand, one hundred and ninety-three => 57
57 => fifty-seven => 10
10 => ten => 3
3 => three => 5
5 => five => 4
==============================
"""

import sys
import re
from num2words import num2words


def format_number(n):
    return format(n, ',d').replace(',', '.')


def main(num, lang='en'):
    n = int(num)
    word = num2words(n, lang=lang)

    print('='*30)
    print('STARTING SEQUENCE')
    print('starting number => {}'.format(format_number(n)))
    print('='*30)

    while word != num2words(4, lang=lang):
        # Only count a-zA-Z chars.
        curNum = len(re.sub('[^a-zA-Z]+', '', word))
        newWord = num2words(curNum, lang=lang)
        newNum = len(newWord)
        print('{} => {} => {}'.format(format_number(n), word, curNum))
        word = newWord
        n = curNum
    print('='*30)
    print('\n')


def usage():
    print('''
Usage: ./four.py [num] [lang]

For a complete list of languages, visit the docs of 'num2words':
https://pypi.org/project/num2words/

Examples:
  ./four.py 11
  ./four.py 294 nl
  ./four.py 294 de
  ./four.py 294 es
''')


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Please specify a number.')
        usage()
        sys.exit(1)
    elif len(sys.argv) == 2:
        main(sys.argv[1])
    elif len(sys.argv) == 3:
        main(sys.argv[1], sys.argv[2])
