import os
import json
import click
import shutil
import pathlib
from flask import current_app
from flask.cli import with_appcontext
import mysql.connector
from time import sleep
from datetime import datetime

from core.config import (
    DATABASE_NAME,
    DATABASE_HOST,
    DATABASE_PASSWORD,
    DATABASE_USER
)

db = mysql.connector.connect(
    host=DATABASE_HOST,
    user=DATABASE_USER,
    passwd=DATABASE_PASSWORD
)

mysql_cursor = db.cursor()


@click.command('delete-db')
@with_appcontext
def reset():
    app_pyc = current_app.config['APPLICATION_ROOT'] + '/app.pyc'
    migration_folder = current_app.config['APPLICATION_ROOT'] + '/migrations'
    pycache = current_app.config['APPLICATION_ROOT'] + '/__pycache__'

    app_pyc_file = pathlib.Path(app_pyc)
    migration_folder_path = pathlib.Path(migration_folder)
    pycache_path = pathlib.Path(pycache)

    if app_pyc_file.is_file():
        app_pyc_file.unlink()
    if migration_folder_path.is_dir():
        shutil.rmtree(migration_folder_path)
    if pycache_path.is_dir():
        shutil.rmtree(pycache_path)

    try:
        mysql_cursor.execute("DROP DATABASE {}".format(DATABASE_NAME))
        click.echo('Database {} has been deleted..!!!'.format(DATABASE_NAME))
    except:
        click.echo('Database "{}" is not exist, so "delete action" is not running'.format(DATABASE_NAME))


@click.command('new')
@with_appcontext
def new_command():
    os.system("flask delete-db")
    for i in range(10):
        dots = "." * i
        click.echo("waiting for create new database {}".format(dots))
        sleep(0.2)
        print(u"{}[2J{}[;H".format(chr(27), chr(27)))
    mysql_cursor.execute("CREATE DATABASE {}".format(DATABASE_NAME))
    os.system("flask db init")
    os.system("flask db migrate")
    os.system("flask db upgrade")
    os.system("flask add-seek")
    print(u"{}[2J{}[;H".format(chr(27), chr(27)))
    click.echo("Done.!! :)")


@click.command('add-seek')
@with_appcontext
def add_seek():
    from apps.user.models import User, UserDetail
    seek_data = open('seek_data.json')
    seek_data = json.load(seek_data)

    detail = UserDetail(
        fullname=seek_data['user_data']['fullname'],
        address=seek_data['user_data']['address'],
        phone_number=seek_data['user_data']['phone_number'],
        work_start_time=datetime.strptime(seek_data['user_data']['work_start_time'], "%d-%m-%Y").date(),
        activate=seek_data['user_data']['activate'],
    )

    user = User(
        username=seek_data['user_data']['username'],
        email=seek_data['user_data']['email'],
        password=seek_data['user_data']['password'],
        user_detail=detail
    )
    user.commit()
    click.echo("Add Data Done.!! :)")


class CLI:
    @staticmethod
    def init_app(app):
        app.cli.add_command(reset)
        app.cli.add_command(add_seek)
        app.cli.add_command(new_command)

