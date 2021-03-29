# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     fakes
   Description :
   Author :       ybw
   date：          2021/3/27
-------------------------------------------------
   Change Activity:
                   2021/3/27:
-------------------------------------------------
"""
from faker import Faker
from sqlite3 import IntegrityError

from src.extensions import db
from src.models.user import User

fake = Faker()


def fake_user(count=10):
    for i in range(count):
        user = User(email=fake.email(),
                    password=fake.word(), )
        db.session.add(user)
        try:
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
