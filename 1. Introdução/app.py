from flask import Flask, render_template

app = Flask(__name__)

# 127.0.0.1:5000/
@app.route('/')
def principal():
    return render_template("index.html")

@app.route('/sobre')
def sobre():
    return render_template("sobre.html")