__author__ = 'Manish'



import mysqldbconnection

class ConnectionFactory(object):

    @staticmethod
    def create():

        #TODO :  Make sqlalchemy as plugin so that it can be replaced with another framework anytime
        # Note that sqlalchemy is analogous to DataSource in java
        conn = mysqldbconnection.MySqlDbConnection()
        conn.open()
        return conn



    # def create (self, dbtype):
    #     engine = create_engine('sqlite:///:memory:', echo=True)
    #     conn = engine.connect()
    #     return conn


