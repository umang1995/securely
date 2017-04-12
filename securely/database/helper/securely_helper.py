from securely.database.dal import connection_factory
from securely.database.dao import securely_dao


class SecurelyHelper(object):
    def get_file(self, filename, username):
        conn = None
        try:
            conn = self.get_connection(None)
            dao = securely_dao.SecurelyDao(conn)
            file_details = dao.get_file(filename,username)
            return file_details
        except Exception as e :
            print e.message
            return "failure"
        finally:
            conn.close()


    def get_connection(self,existing_conn=None):
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


    def get_user_basic_info(self,username):
        conn = None
        try:
            conn = self.get_connection(None)
            dao = securely_dao.SecurelyDao(conn)
            user_basic_info = dao.get_basic_info(username)
            return user_basic_info.serialize()
        except Exception as e :
            print e.message
            return "failure"
        finally:
            conn.close()

    def register_user_in_db(self,username,name,password,email):
        conn = None
        try:
            conn = self.get_connection(None)
            dao = securely_dao.SecurelyDao(conn)
            is_avail = dao.check_availability(username)
            if is_avail is True:
                conn = self.get_connection(None)
                dao = securely_dao.SecurelyDao(conn)
                dao.register_user(username, password, name, email)
            else:
                return "not a valid username"
            return "success"
        except:
            return "failure"
        finally:
            conn.close()
    def login_user(self,username,password):
        conn = None
        try:
            conn = self.get_connection(None)
            dao = securely_dao.SecurelyDao(conn)
            is_valid = dao.login_user(username,password)
            if is_valid is True:
                return "sucess"
            else:
                return "invalid credentials"
        except:
            return "failure"
        finally:
            conn.close()
    def save_file(self,file_location,salt_hashed_password,salt,iv,latitude,longitude,username,key):
        conn = None
        try:
            conn = self.get_connection(None)
            dao = securely_dao.SecurelyDao(conn)
            dao.save_file(file_location,salt_hashed_password,salt,iv,latitude,longitude,username,key)
            return "success"
        except Exception as e:
            print e.message
            return "failure"
        finally:
            conn.close()

    def get_files_for_user(self,user_id):
        conn = None
        try:
            conn = self.get_connection(None)
            dao = securely_dao.SecurelyDao(conn)
            file_details_for_user = dao.get_files_for_user(user_id)
            return file_details_for_user
        except:
            raise
        finally:
            conn.close()
