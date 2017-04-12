import os
from securely.helper import upload_helper
from securely.config.config import Config
def upload_file(uploaded_file,password,lat_lon_result,username):
    response = upload_helper.UploadHelper().upload_file(uploaded_file,password,lat_lon_result,username) # username
    return response



