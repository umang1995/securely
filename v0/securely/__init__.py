from flask import Flask,render_template,jsonify,request,redirect,url_for,make_response
import Cookie

from flask import Response

from securely.handler import download_handler
from securely.handler import handle_login
from securely.handler import profile_handler
from securely.handler import upload_handler
app = Flask(__name__)

@app.route("/test")
def test():
    return render_template("test.html")

@app.route("/")
def homepage():
    return render_template("home_page.html")

@app.route("/login",methods=['GET','POST'])
def login(errors=None):
    try:
        if request.method == "POST":
            username = request.form['username']
            password = request.form['password']
            response = handle_login.LoginHandler().handler_homepage(1,username,password)
            if response == "invalid credentials":
                error = "Incorrect credentials. Please Try Again."
            elif response == "failure":
                error = "server error. Try again later"
            else:
                res = make_response(redirect(url_for('upload')))
                res.set_cookie('user_id',username)
                return res

        return render_template("login.html", errors=errors)
    except Exception as e:
        return str(e)

@app.route("/register", methods=['GET','POST'])
def register():
    error = None
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        name = request.form['name']
        email = request.form['email']
        response = handle_login.LoginHandler().handler_homepage(2,username,password,name,email)
        if response == "success":
            return redirect(url_for('login'))
        elif response == "failure":
            error = "Some server error. try again later"
        elif response == "not a valid username":
            error = "username already taken. please choose another username"
    return render_template("register.html", error=error)

@app.route("/error",methods =['GET', 'POST'])
def error():
    message = None
    try:
        error_type = int(request.form['type'])
        if error_type == 1:
            message = "please select a file"
        elif error_type == 2:
            message = "please enter password"
        elif error_type == 3:
            message = "atleast one coordinate needed"
        return message
    except Exception as e:
        return e.message


@app.route("/upload",methods =['GET', 'POST'])
def upload():
    message = None
    username = None
    try:
        username = request.cookies['user_id']
        if request.method == "POST":
            message = "some error at server"
            file_obj = request.files['file']
            password = request.form['password']
            lat_lon_result = request.form['result_coords']
            if lat_lon_result == "":
                return "atleast one co-ordinate is required"
            else:
                response = upload_handler.upload_file(file_obj,password,lat_lon_result,username)
                if response == "success":
                    message = "file uploaded"
                else:
                    message = response
    except KeyError as e:
        response = make_response(redirect(url_for('login')))
        return response
    except Exception as e:
        print e.message
        message = e.message
    finally:
        return render_template("upload.html", message=message)
@app.route("/maps")
def maps():
    return render_template("maps.html")

@app.route("/profile",methods=['GET','POST'])
def profile():
    try:
        username = request.cookies['user_id']
        if request.method == "POST":
            return profile_handler.ProfileHandler().display_user_profile(username)
        return render_template("profile.html")
    except KeyError as e:
        return make_response(redirect(url_for('login'),"please login"))
    except Exception as j:
        return str(j)

@app.route("/download", methods=['GET','POST'])
def download():
    try:
        username = request.cookies['user_id']
        if request.method == "POST":
            lat_lon_list = request.form['result_coords']
            file_list = download_handler.DownloadHandler().get_file_for_trusted_area(lat_lon_list,username)
            return file_list
        return render_template("download.html")
    except KeyError as e:
        return make_response(redirect(url_for('login'),"please login"))
    except Exception as j:
        return str(j)


@app.route("/get_file",methods=['POST'])
def get_file():
    try:
        username = request.cookies['user_id']
        if request.method == "POST":
            filename = request.form['file_name']
            password = request.form['password']
            response = download_handler.DownloadHandler().get_file(filename, username, password)
            return jsonify(response)
        return render_template("download.html")
    except KeyError as e:
        return make_response(redirect(url_for('login'), "please login"))
    except Exception as j:
        return str(j)

@app.route("/logout", methods=['GET'])
def logout():
    try:
        c = Cookie.SimpleCookie()
        c['user_id'] = ''
        headers = {
            'Location': url_for('homepage')
        }

        return Response(url_for('homepage'), status=302, headers=headers)
        # return redirect(url_for('homepage'),200)
    except KeyError as ke:
        print ke
        redirect("/login",302,"not logged in. please log in to continue")
    except Exception as e:
        print e