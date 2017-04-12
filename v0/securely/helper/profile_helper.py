from securely.database.helper import securely_helper


class ProfileHelper(object):
    def get_user_details(self,username):
        # get basic info as basic info vo and then serialize
        return securely_helper.SecurelyHelper().get_user_basic_info(username)
