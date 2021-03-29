# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     ns1_test1_mytype
   Description :
   Author :       ybw
   date：          2021/3/29
-------------------------------------------------
   Change Activity:
                   2021/3/29:
-------------------------------------------------
"""


def my_type(value):
    """
    design your parse
    :param value:
    :return:
    """
    if type(value) != str:
        raise ValueError('This is not my type')
    return value


# Swagger documntation
my_type.__schema__ = {'type': 'string', 'format': 'my-custom-format'}
