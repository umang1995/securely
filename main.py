from flask import Flask,render_template
from securely import app
from securely.handler import upload_handler
current_app = app
if __name__ == "__main__":
    current_app.run(debug=True)
