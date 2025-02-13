from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    
    return "<h1>Ola mundo! </h1>"


app.run()