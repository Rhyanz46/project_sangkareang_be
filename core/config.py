import os

mysql_user = 'rhyanz46'
mysql_pass = 'a'
mysql_host = 'localhost'
mysql_db = 'sangkareang'

config = {
    'SQLALCHEMY_DATABASE_URI': 'mysql://{}:{}@{}/{}'.
        format(mysql_user, mysql_pass, mysql_host, mysql_db),
    'SQLALCHEMY_TRACK_MODIFICATIONS': False,
    'SECRET_KEY': 'keren',
    'APPLICATION_ROOT': os.getcwd()
}
