from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    lista = ['Tetris','skyrim','crash']
    return render_template("listas.html", titulo="Jogos", jogos=lista)


app.run()