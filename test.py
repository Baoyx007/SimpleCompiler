# -*- coding:utf-8 -*-

"""
Created by haven on 16/7/30.
"""

import Tokenizer


def pretty_print(tokens):
    print('[')
    for token in tokens:
        print(token)
    print(']')


if __name__ == '__main__':
    res = Tokenizer.tokenizer('(add 2 (subtract 4 2))')
    pretty_print(res)
