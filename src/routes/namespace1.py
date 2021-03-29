# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     namespace1
   Description :
   Author :       ybw
   date：          2021/3/27
-------------------------------------------------
   Change Activity:
                   2021/3/27:
-------------------------------------------------
"""
from flask import request
from flask_restplus import Namespace, Resource, abort, reqparse, inputs, fields

from src import db
from src.models.user import User
from src.schme.ns1_test1 import UserSchema
import typing

from src.schme.ns1_test1_mytype import my_type

api = Namespace('ns1', description="namespace1 test request params")


@api.route('/')
class Test1(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('ip', type=inputs.ipv4, location='json')
    parser.add_argument('name', type=my_type, required=True, location='args')

    @api.expect(parser)
    @api.header('X-Header', 'Some class header')
    @api.doc(id='get_something')
    def get(self):
        args = self.parser.parse_args()
        return args['name']

    def post(self):
        a = request
        args = self.parser.parse_args()
        return args['name']


model = api.model('Model', {
    'id': fields.Integer,
})


@api.route("/api/users/<id>")
@api.doc(params={'id': 'An ID'})
class UsersApi(Resource):
    users_schema = UserSchema(many=True)

    @api.doc(description='get user')
    @api.doc(responses={403: 'Not Authorized'})
    @api.doc(responses={200: 'return json user'})
    @api.marshal_with(model, code=201, description='Object created')
    def get(self, id):
        if id:
            users = User.query.limit(1).all()
        else:
            users = User.query.order_by(User.email).all()
        # return self.users_schema.dump(users)
        return users


@api.route("/api/users")
class UsersAllApi(Resource):
    users_schema = UserSchema(many=True)
    @api.doc(deprecated=True)
    def get(self):
        users = User.query.order_by(User.email).all()
        return self.users_schema.dump(users)
