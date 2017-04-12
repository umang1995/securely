import json
from securely.helper import download_helper
from flask import jsonify
class DownloadHandler(object):
    def get_file_for_trusted_area(self,lat_lon_list,user_id):
        try:
            lat_lon_list_dict = json.loads(lat_lon_list)
            result_of_files = download_helper.DownloadHelper().fetch_files_for_user_in_trusted_area(lat_lon_list_dict,user_id)
            return jsonify({'data':result_of_files})
        except Exception as e:
            print e.message
            print "oops error"

    def get_file(self,filename,username,password):
        try:
            response = dict()
            (authentication, files) = download_helper.DownloadHelper().get_file(filename,username,password)

            response['authentication'] = authentication
            if authentication is True:
                files = files.replace("\n","<br>")
                response['file'] = files
            else:
                response['file'] = "incorrect password. go back and try again."
            return response
        except Exception as e:
            print e.message
            print "oops error"