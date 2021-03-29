# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     wsgi
   Description :
   Author :       ybw
   date：          2021/3/27
-------------------------------------------------
   Change Activity:
                   2021/3/27:
-------------------------------------------------
"""

from src import create_app  # noqa

app = create_app()

if __name__ == '__main__':
    app.run()