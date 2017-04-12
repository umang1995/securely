__author__ = 'Manish'

import dbconnection
from sqlalchemy import create_engine
from flask import current_app
from securely.config import config


class MySqlDbConnection (dbconnection.DBConnection):
    def __init__(self):
        super(MySqlDbConnection, self).__init__(conn=None, engine=None)
        #TODO : Pick connection string from config file
        #engine = create_engine('mysql+mysqldb://<user>:<password>@<host>[:<port>]/<dbname>')
        mysql_url = config.Config.MYSQL_DATABASE_URI
        #mysql_url = 'mysql+pymysql://root:root@localhost:3306/ck'
        engine = create_engine(mysql_url, pool_recycle=3600)

        super(MySqlDbConnection, self).setdatasource(engine)







