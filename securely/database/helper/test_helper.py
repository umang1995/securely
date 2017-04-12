from securely.database.dal import connection_factory
from securely.database.dao import test_dao

def get_connection(existing_conn=None):
    is_new_connection = False
    conn = None
    try:
        if existing_conn is None:
            myconn = connection_factory.ConnectionFactory.create()
            conn = myconn.getconnection()
            is_new_connection = True
        else:
            conn = existing_conn
        return conn
    except:
        raise

conn = get_connection(None)
dao = test_dao.PortfolioDao(conn)
dao.test_insert()
