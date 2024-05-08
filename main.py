from flask import Flask 
app = Flask(__name__) 
ECHO is on.
@app.route('/') 
def hello_world(): 
    return 'Hello, World!' 
