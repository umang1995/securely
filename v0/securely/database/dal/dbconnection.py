__author__ = 'Manish'

from sqlalchemy import exc

class DBConnection(object):
    def __init__(self, conn, engine):
        self.conn = None
        self.engine = None

    def setdatasource(self, engine):
        self.engine = engine

    def open(self):
        '''
        Creates a connection from the database pool. This connection is not part of a transaction.
        If a connection was made by a previous call to this function , it will not create a new one.
        '''
        try:
            if self.conn is not None and not self.conn.closed:
                return
            self.conn = self.engine.connect()
        except exc.SQLAlchemyError:
            raise
        except:
            raise

    def close(self):
        '''
        Returns the connection to database pool. This connection is not part of a transaction.
        If a connection was made by a previous call to this function , it will not create a new one.
        '''
        try:
            if self.conn is not None and not self.conn.closed:
                self.conn.close()
        except exc.SQLAlchemyError:
            raise
        except:
            raise

    def getconnection(self):
        '''
        Creates a connection from the database pool. This connection is not part of a transaction.
        If a connection was made by a previous call to this function , it will not create a new one.
        '''
        try:
            if self.conn is None or self.conn.closed:
                raise exc.SQLAlchemyError("Connection is already closed.")

        except exc.SQLAlchemyError:
            raise
        except:
            raise

        return self.conn
