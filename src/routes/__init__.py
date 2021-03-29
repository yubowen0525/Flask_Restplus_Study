# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     __init__.py
   Description :
   Author :       ybw
   date：          2021/3/27
-------------------------------------------------
   Change Activity:
                   2021/3/27:
-------------------------------------------------
"""

from ..extensions import api
from .namespace1 import api as ns1
from .namespace2 import api as ns2


@api.errorhandler
@api.header('My-Header', 'Some description')
def handle_fake_exception_with_header(error):
    '''This is a custom error'''
    return {'message': error.message, 'code':400}, 400, {'My-Header': 'Value'}


api.add_namespace(ns1, path='/ns1')
api.add_namespace(ns2, path='/ns2')
