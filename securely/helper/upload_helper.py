import datetime

import itertools
import json

from securely.config.config import Config
import os
from securely.config import config
from Crypto.Cipher import AES
from Crypto.Hash import SHA512, SHA256
from Crypto import Random

from securely.database.helper import securely_helper


class UploadHelper(object):

    def check_extension(self,filename):
        (file_name,extension) = filename.split('.')
        allowed_extension = config.Config.allowed_extensions
        is_allowed = False
        for ext in allowed_extension:
            if ext == extension:
                is_allowed = True
                break
        return is_allowed

    def get_hashed_content(self, password, hasher):
        if hasher == "SHA512":
            salt = Random.get_random_bytes(64)
            cipher = SHA512.new(password).digest()
            length_of_cipher = str(len(cipher))
            cipher += salt
            return salt, cipher
        elif hasher == "SHA256":
            cipher = SHA256.new(password).digest()
            length_of_cipher = str(len(cipher))
            return cipher

    def upload_file(self,uploaded_file,password,lat_lon_list,username):

        is_ext_correct = self.check_extension(uploaded_file.filename)
        if is_ext_correct is True:
            # create a hashed salt password
            (salt,salt_hashed_password) = self.get_hashed_content(password, "SHA512")
            # encrypt the file with password as the key
            (iv,key,cipher_text) = self.encrypt_file_content(uploaded_file,password)
            # store the file with encrypted content
            (response,file_location) = self.store_file(uploaded_file.filename,cipher_text,username)

            lat_lon_dict_list = json.loads(lat_lon_list)
            for lat_lon in lat_lon_dict_list:
                latitude = lat_lon.get('latitude',None)
                longitude = lat_lon.get('longitude',None)
                encrypted_latitude = self.encrypt_coord(latitude,iv,key)
                encrypted_longitude = self.encrypt_coord(longitude, iv, key)
                print "len password " + str(len(salt_hashed_password))
                print "len salt " + str(len(salt))
                print "type iv " + str(type(iv))

                securely_helper.SecurelyHelper().save_file(file_location,salt_hashed_password,salt,iv,encrypted_latitude,encrypted_longitude,username,key)
            # save the entry in the table
            return response
        else:
            #FIXME add more doc types
            return "not a correct file type. Only txt files allowed"

    def store_file(self,filename,content,username):
        try:
            file_path = os.getcwd()
            (filen,ext) = filename.split(".")
            file_path += Config.save_path + filen + "_" + username + "." + ext
            stored_file = open(file_path,'wb')
            stored_file.write(content)
            return "success",file_path
        except:
            return "failure"

    def encrypt_coord(self,coord,iv,key):
        encryptor = AES.new(key, AES.MODE_CFB, iv)
        plain_text = str(coord).zfill(128)
        print str(len(plain_text))
        cipher = encryptor.encrypt(str(coord))
        return cipher

    def encrypt_file_content(self,infile,password):
        try:
            chunk_size = 128
            cipher = None
            key = self.get_hashed_content(password,"SHA256")
            iv = Random.new().read(16)
            encryptor = AES.new(key, AES.MODE_CFB, iv)
            while True:
                chunk = infile.read(chunk_size)
                if len(chunk) == 0:
                    break
                elif len(chunk) %16 !=0:
                    chunk += bytes(" ") * (16- (len(chunk) % 16))

                if cipher is None:
                    cipher = encryptor.encrypt(chunk)
                else:
                    cipher += encryptor.encrypt(chunk)

            return iv,key,cipher
        except Exception as e:
            print e.message
            return "failure"

