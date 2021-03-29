# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     ns_test1
   Description :
   Author :       ybw
   date：          2021/3/27
-------------------------------------------------
   Change Activity:
                   2021/3/27:
-------------------------------------------------
"""
from src.extensions import ma
from marshmallow import fields
from src.models.user import User


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        # Fields to expose
        model = User
        fields = ("email", "date_created", "author")
        # id = ma.auto_field()
        # email = ma.auto_field()
        # date_created = ma.auto_field()

    # Smart hyperlinking
    _links = ma.Hyperlinks(
        {
            "self": ma.URLFor("ns1_users_api", id="<id>"),
            "collection": ma.URLFor("ns1_users_all_api"),
        }
    )
