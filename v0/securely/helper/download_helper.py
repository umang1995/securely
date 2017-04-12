from Crypto.Cipher import AES
from Crypto.Hash import SHA512

from securely.database.helper import securely_helper
from geopy.distance import vincenty
class DownloadHelper(object):
    def fetch_files_for_user(self,user_id):
        try:
            return securely_helper.SecurelyHelper().get_files_for_user(user_id)
        except:
            raise

    def decrypt_coords(self,coord,iv,key):
        try:
            decryptor = AES.new(key, AES.MODE_CFB, iv)
            plain = decryptor.decrypt(coord)
            return plain
        except Exception as e:
            print e.message
            raise

    def match_password(self,given_password,file_password):
        # get details about filename match with password
        is_valid = False
        try:
            if given_password == file_password:
                is_valid = True
            return is_valid
        except:
            raise

    def decrypt_file(self,hash_key,iv,filename):
        chunk_size = 128
        plain_text = None
        with open(filename,'rb') as infile:
            decryptor = AES.new(hash_key,AES.MODE_CFB,iv)
            while True:
                chunk = infile.read(chunk_size)
                if len(chunk) == 0:
                    break
                chunk_plain_text = decryptor.decrypt(chunk)
                if plain_text is None:
                    plain_text = chunk_plain_text
                else:
                    plain_text = plain_text + chunk_plain_text
        return plain_text

    def hash_password(self, password, salt):
        cipher = SHA512.new(password).digest()
        length_of_cipher = str(len(cipher))
        cipher += salt
        return cipher


    def get_file(self,filename, username, password):

        #TODO authenticate the password and get the file

        try:
            #todo get the file details
            file_details = securely_helper.SecurelyHelper().get_file(filename,username)

            #todo hash the given password using hash salt algorithm
            hash_given_password = self.hash_password(password,file_details._ss)


            #todo authenticate the password
            is_auth = self.match_password(hash_given_password, file_details._password)


            #todo if password authenticated decrypt the file
            if is_auth is True:
                user_file = self.decrypt_file(file_details._key,file_details._IV,file_details._location)
                return is_auth, user_file
            else:
                return is_auth, None
        except:
            raise

    def fetch_files_for_user_in_trusted_area(self,lat_lon_list_dict,user_id):
        try:
            list_of_files_by_user = self.fetch_files_for_user(user_id)
            result_of_files = []
            for lat_lon in lat_lon_list_dict:
                for file_details in list_of_files_by_user:
                    latitude = self.decrypt_coords(file_details._latitude, file_details._IV, file_details._key)
                    longitude = self.decrypt_coords(file_details._longitude, file_details._IV, file_details._key)
                    file_loc_dict = dict()
                    file_loc_dict['latitude'] = latitude
                    file_loc_dict['longitude'] = longitude
                    distance = self.calculate_distance(lat_lon,file_loc_dict)
                    if distance <= 3:
                        rest_dict = dict()
                        location = file_details._location
                        location = location.replace("\\","/")
                        filename = location.split('/')[-1]
                        filename = filename.split('_')[0]
                        rest_dict['file_name'] = filename

                        result_of_files.append(rest_dict)

            return result_of_files
        except Exception as e:
            print e.message
            raise


    def calculate_distance(self,pos1,pos2):
        position_one = (pos1.get('latitude'),pos1.get('longitude'))
        position_two = (pos2.get('latitude'),pos2.get('longitude'))
        distance = vincenty(position_one,position_two).kilometers
        return distance


