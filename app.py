from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    projetos = ["App Mobile da Cantina", "API de Pagamentos"]
    return render_template("index.html", projetos=projetos)



