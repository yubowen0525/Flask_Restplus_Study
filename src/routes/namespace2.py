# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     namespace2
   Description :
   Author :       ybw
   date：          2021/3/29
-------------------------------------------------
   Change Activity:
                   2021/3/29:
-------------------------------------------------
"""
from flask import request
from flask_restplus import Namespace, Resource, abort, reqparse, inputs
from werkzeug.exceptions import BadRequest

from src import db
from src.models.user import User
from src.schme.ns1_test1 import UserSchema
import typing

from src.schme.ns1_test1_mytype import my_type

api = Namespace('ns2', description="namespace2 test error")




@api.route('/test/')
class TestResource(Resource):
    def get(self):
        '''
        Do something

        :raises CustomException: In case of something
        '''
        raise BadRequest()
        pass
