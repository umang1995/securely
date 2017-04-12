from securely.database.dao import securely_queries
from securely.database.dal import dbcondao
from sqlalchemy.sql import text
from sqlalchemy import exc

from securely.vo import file_vo
from securely.vo import user_basic_info_vo


class SecurelyDao(dbcondao.DbConDao):
    def get_file(self,filename, username):
        try:
            query = text(securely_queries.SecurelyQueries.get_file_details)
            conn = super(SecurelyDao, self).getconnection()
            filename = "%"+filename+"%"
            values = {'filename': str(filename),'username': str(username)}
            result = conn.execute(query, values)
            for row in result:
                result_vo = file_vo.FileVo()
                result_vo.username = row['username']
                result_vo.id = row['ID']
                result_vo.latitude = row['latitude']
                result_vo.longitude = row['longitude']
                result_vo.location = row['location']
                result_vo.password = row['password']
                result_vo.ss = row['SS']
                result_vo.IV = row['IV']
                result_vo.key = row['hash_key_for_encryption']
                return result_vo
        except exc.SQLAlchemyError as e:
            print e.message
            raise
        except:
            raise

    def get_file_count(self,username):
        
        file_count = None
        try:
            query = text(securely_queries.SecurelyQueries.get_user_file_count)
            conn = super(SecurelyDao, self).getconnection()
            values = {'username': str(username)}
            result = conn.execute(query, values)
            for count in result:
                file_count = count['file_count']
            return file_count
        except exc.SQLAlchemyError:
            raise
        except:
            raise
      
    def get_basic_info(self,username):
        result_info = user_basic_info_vo.UserBasicInfoVo()
        try:
            query = text(securely_queries.SecurelyQueries.get_basic_details)
            conn = super(SecurelyDao, self).getconnection()
            values = {'username': str(username)}
            result = conn.execute(query, values)
            for user in result:
                username = user['username']
                name = user['name']
                email = user['email']
                result_info.username = username
                result_info.name = name
                result_info.email = email
            file_count = self.get_file_count(username)
            result_info.file_uploaded = file_count
            return result_info
        except exc.SQLAlchemyError:
            raise
        except:
            raise
 

    def login_user(self,username,password):
        try:
            query = text(securely_queries.SecurelyQueries.login_user)
            conn = super(SecurelyDao, self).getconnection()
            values = {'username':str(username)}
            result = conn.execute(query, values)
            for user in result:
                password_for_user = user['password']
                if password == password_for_user:
                    return True
                else:
                    return False
        except exc.SQLAlchemyError as e:
            print e.message
            raise
        except:
            raise


    def register_user(self, username, password, name, email):
        
        try:
            query = text(securely_queries.SecurelyQueries.insert_into_user)
            conn = super(SecurelyDao, self).getconnection()
            values = {'username':str(username),'name':str(name),'password':str(password),'email':str(email)}
            conn.execute(query, values)
        except exc.SQLAlchemyError as e:
            print e.message
            raise
        except:
            raise

    def check_availability(self,username):

        try:
            query = text(securely_queries.SecurelyQueries.get_all_users)
            conn = super(SecurelyDao, self).getconnection()
            result = conn.execute(query)
            is_avail = True
            for prev_username in result:
                user = prev_username['username']
                if username == user:
                    is_avail = False
                    break
            return is_avail
        except exc.SQLAlchemyError:
            raise
        except:
            raise
    

    def save_file(self, file_location, salt_hashed_password, salt, iv, latitude, longitude, username,key):
        
        try:
            query = text(securely_queries.SecurelyQueries.insert_into_password)
            conn = super(SecurelyDao, self).getconnection()
            values = {'file_location': str(file_location), 'salt': str(salt),'password':str(salt_hashed_password),'longitude':str(longitude),'latitude':str(latitude),
                         'iv':str(iv),'username':username,'key':str(key)}
            conn.execute(query, values)

        except exc.SQLAlchemyError:
            raise
        except:
            raise


    def get_files_for_user(self,user_id):
        result_info_list = []

        try:
            query = text(securely_queries.SecurelyQueries.get_files_for_user)
            conn = super(SecurelyDao,self).getconnection()
            values = {'user_id': str(user_id)}
            result = conn.execute(query,values)
            for row in result:
                result_vo = file_vo.FileVo()
                result_vo.username = row['username']
                result_vo.id = row['ID']
                result_vo.latitude = row['latitude']
                result_vo.longitude = row['longitude']
                result_vo.location = row['location']
                result_vo.password = row['password']
                result_vo.ss = row['SS']
                result_vo.IV = row['IV']
                result_vo.key = row['hash_key_for_encryption']
                result_info_list.append(result_vo)
            return result_info_list
        except exc.SQLAlchemyError as e:
            print e.message
            raise
        except Exception as e:
            print e.message
            raise
    

