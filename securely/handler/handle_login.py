from securely.helper import login_helper
import Cookie
class LoginHandler(object):
    def handler_homepage(self,identifier,username,password,name=None,email=None):
        response = None
        if identifier == 1:
            response = login_helper.LoginRegister().login(username, password)
        else:
            response = login_helper.LoginRegister().register(name, username, password, email)
        return response

