# -*- coding:utf-8 -*-

"""
Created by haven on 16/7/30.
"""

import Tokenizer
from Parser import parser


def pretty_print(tokens):
    print('[')
    for token in tokens:
        print(token)
    print(']')


def pretty_print_ast(ast, space=0):
    for key, val in ast.items():
        if isinstance(val, list):
            for _ in val:
                pretty_print_ast(_, space + 2)
                continue
        else:
            for _ in range(space):
                print(' ',end='')
            print(key + ":" + str(val))


def a():
    parm = 10

    def b():
        # parm=parm+1
        print(parm)

    return b


if __name__ == '__main__':
    # print(a().__closure__)
    tokens = Tokenizer.tokenizer('(add 2 (subtract 4 2))')
    pretty_print(tokens)
    ast = parser(tokens)
    pretty_print_ast(ast)
