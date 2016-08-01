# -*- coding:utf-8 -*-

"""
Created by haven on 16/7/31.
"""


def parser(tokens):
    cur = 0

    # add(2,sub(4,5))
    # cur 是个很不好的设计
    def walk():
        nonlocal cur
        token = tokens[cur]
        if token['type'] == 'number':
            cur += 1
            print('encount a number : %d' % (int(token['value'])))
            return {
                'type': 'NumberLiteral',
                'value': token['value']
            }
        if token['type'] == 'paren' and token['value'] == '(':
            cur += 1
            token=tokens[cur]
            # name like: add , sub
            node = {
                'type': 'CallExpression',
                'name': token['value'],
                'params': []
            }
            cur += 1
            token = tokens[cur]
            while token['type'] != 'paren' or token['value'] != ')':
                node['params'].append(walk())
                token = tokens[cur]
            cur += 1
            return node

        raise TypeError(tokens[cur]['type'])

    ast = {
        'type': 'program',
        'body': []
    }
    while cur < len(tokens):
        ast['body'].append(walk())

    return ast
