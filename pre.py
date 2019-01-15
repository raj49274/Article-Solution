import cs50
import flask
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("hello.html")
    
    

    
if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=8080)