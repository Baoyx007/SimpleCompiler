# -*- coding:utf-8 -*-

"""
Created by haven on 16/7/30
"""

import re

NUMBERS = '\d'
LETTERS = '\w'
WHITESPACE = '\s'
PAREN = '[\(\)]'


def tokenizer(input):
    tokens = []
    idx = 0
    while idx < len(input):
        c = input[idx]
        if re.match(NUMBERS, c):
            value = ''
            while re.match(NUMBERS, input[idx]):
                value += input[idx]
                idx += 1
            tokens.append({'type': 'number', 'value': value})
        elif re.match(LETTERS, c):
            value = ''
            while re.match(LETTERS, input[idx]):
                value += input[idx]
                idx += 1
            tokens.append({'type': 'name', 'value': value})
        elif re.match(WHITESPACE, c):
            idx += 1
            pass
        elif re.match(PAREN, c):
            tokens.append({'type': 'paren', 'value': c})
            idx += 1
        else:
            raise Exception('not support token!')
    return tokens
