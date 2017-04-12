from securely.database.helper import securely_helper
from Crypto.Hash import SHA512
class LoginRegister(object):
    def login(self, username, password):
        cipher_text = self.hash_password(password)
        response = securely_helper.SecurelyHelper().login_user(username,cipher_text)
        return response


    def register(self, name, username, password, email):
        cipher_text = self.hash_password(password)
        response = securely_helper.SecurelyHelper().register_user_in_db(username,name,cipher_text,email)
        return response

    def hash_password(self,password):
        return SHA512.new(password).hexdigest()

