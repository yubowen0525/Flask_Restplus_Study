import datetime as dt


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.created_at = dt.datetime.now()

    def __repr__(self):
        return "<User(name={self.name!r})>".format(self=self)


from marshmallow import Schema, fields, post_load


class UserSchema(Schema):
    name = fields.Str()
    email = fields.Email()
    created_at = fields.DateTime()

    @post_load
    def make_user(self, data, **kwargs):
        return User(**data)

# UserSchema = Schema.from_dict(
#     {"name": fields.Str(), "email": fields.Email(), "created_at": fields.DateTime()}
# )

from pprint import pprint

# 序列化
user = User(name="Monty", email="monty@python.org")
schema = UserSchema()
result = schema.dump(user)
pprint(result)

# 反序列化
# user_data = {
#     "created_at": "2014-08-11T05:26:03.869245",
#     "email": "ken@yahoo.com",
#     "name": "Ken",
# }

user_data = {"name": "Ronnie", "email": "ronnie@stones.com"}
schema = UserSchema()

# 由于加了 post_load 直接返回实例对象
result = schema.load(user_data)
pprint(result)