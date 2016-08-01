# -*- coding:utf-8 -*-

"""
Created by haven on 16/8/1.
"""


def traverser(ast, visitor):
    def traverse_list(arr, parent):
        for _ in arr:
            traverse_node(_, parent)

    def traverse_node(node, parent):
        visitor_method = visitor[node['type']] if node['type'] in visitor else None
        if visitor_method:
            visitor_method(node, parent)

        method_map = {
            'Program': lambda: traverse_list(node['body'], node),
            'CallExpression': lambda: traverse_list(node['params'], node),
            'NumberLiteral': lambda: 0
        }
        method = method_map[node['type']]
        if method:
            method()
        else:
            raise TypeError('not supported')

    traverse_node(ast, None)


def transformer(ast):
    newAst = {
        'type': 'Program',
        'body': []
    }
    ast['_context'] = newAst['body']

    def visitor_call(node, parent):
        expression = {
            'type': 'CallExpression',
            'callee': {
                'type': 'Identifier',
                'name': node['name']
            },
            'arguments': []
        }
        node['_context'] = expression['arguments']

        # top parent
        if parent['type'] != 'CallExpression':
            expression = {
                'type': 'ExpressionStatement',
                'expression': expression
            }
        parent['_context'].append(expression)

    traverser(ast, {
        'NumberLiteral': lambda node, parent: parent['_context'].append({
            'type': 'NumberLiteral',
            'value': node['value']
        }),
        'CallExpression': visitor_call
    })

    return newAst
