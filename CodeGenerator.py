# -*- coding:utf-8 -*-

"""
Created by haven on 16/8/1.
"""


def code_generator(node):
    switch_map = {
        'Program': lambda: '\n'.join(list(map(code_generator, node['body']))),
        'ExpressionStatement': lambda: code_generator(node['expression']) + ';',
        'CallExpression': lambda: code_generator(node['callee'])
                                  + '('
                                  + ', '.join(list(map(code_generator, node['arguments'])))
                                  + ')'
        ,
        'Identifier': lambda: node['name'],
        'NumberLiteral': lambda: node['value']
    }
    if node['type'] in switch_map:
        return switch_map[node['type']]()
    else:
        raise TypeError('not support type in switch map')
