import os
import click
import shutil
import pathlib
from flask import current_app
from flask.cli import with_appcontext
import mysql.connector
from time import sleep

from core.config import (
    mysql_db,
    mysql_host,
    mysql_pass,
    mysql_user
)

db = mysql.connector.connect(
    host=mysql_host,
    user=mysql_user,
    passwd=mysql_pass
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
        mysql_cursor.execute("DROP DATABASE {}".format(mysql_db))
        click.echo('Database {} has been deleted..!!!'.format(mysql_db))
    except:
        click.echo('Database "{}" is not exist, so "delete action" is not running'.format(mysql_db))


@click.command('new')
@with_appcontext
def new_command():
    os.system("flask delete-db")
    for i in range(10):
        dots = "." * i
        click.echo("waiting for create new database {}".format(dots))
        sleep(0.5)
        print(u"{}[2J{}[;H".format(chr(27), chr(27)))
    mysql_cursor.execute("CREATE DATABASE {}".format(mysql_db))
    os.system("flask db init")
    os.system("flask db migrate")
    os.system("flask db upgrade")
    print(u"{}[2J{}[;H".format(chr(27), chr(27)))
    click.echo("Done.!! :)")


class CLI:
    @staticmethod
    def init_app(app):
        app.cli.add_command(reset)
        app.cli.add_command(new_command)

