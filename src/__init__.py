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
import click

from src.extensions import api, db, ma
from src.fakes import fake_user
from src.settings import config
import os
from flask import Flask, render_template, request
from src.routes import *


def create_app(config_name=None):
    if config_name is None:
        config_name = os.getenv('FLASK_CONFIG', 'development')

    app = Flask('src')
    app.config.from_object(config[config_name])

    register_extensions(app)
    # register_errors(app)
    register_commands(app)
    return app


def register_extensions(app):
    db.init_app(app)
    api.init_app(app, add_specs=app.config['SPECS'])
    ma.init_app(app)


# def register_errors(app):
#     @app.errorhandler(400)
#     def bad_request(e):
#         return render_template('errors/400.html'), 400
#
#     @app.errorhandler(404)
#     def page_not_found(e):
#         return render_template('errors/404.html'), 404
#
#     @app.errorhandler(500)
#     def internal_server_error(e):
#         return render_template('errors/500.html'), 500


def register_commands(app):
    @app.cli.command()
    @click.option('--drop', is_flag=True, help='Create after drop.')
    def initdb(drop):
        """Initialize the database."""
        if drop:
            click.confirm('This operation will delete the database, do you want to continue?', abort=True)
            db.drop_all()
            click.echo('Drop tables.')
        db.create_all()
        click.echo('Initialized database.')

    @app.cli.command()
    @click.option('--user', default=10, help='Quantity of users, default is 10.')
    def forge(user):
        click.echo('Generating %d users...' % user)
        fake_user(user)
# def register_request_handlers(app):
#     @app.after_request
#     def query_profiler(response):
#         for q in get_debug_queries():
#             if q.duration >= app.config['BLUELOG_SLOW_QUERY_THRESHOLD']:
#                 app.logger.warning(
#                     'Slow query: Duration: %fs\n Context: %s\nQuery: %s\n '
#                     % (q.duration, q.context, q.statement)
#                 )
#         return response
