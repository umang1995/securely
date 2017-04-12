from flask import make_response, jsonify
from flask import request
from flask import url_for
from werkzeug.utils import redirect
import json
from securely.helper import profile_helper


class ProfileHandler(object):
    def display_user_profile(self,username):
        try:
            user_details = profile_helper.ProfileHelper().get_user_details(username)
            return jsonify(user_details)
        except KeyError as ke:
            print ke.message
            response = make_response(redirect(url_for('login')))
            return response
        except Exception as e:
            print e.message
            return jsonify({'data': None,'status': "failure"})
