from flask import Flask, render_template, request, redirect, url_for, session
import rns as kero
import os

nomeBanco = "TPSD.db"


app = Flask(__name__)
app.secret_key = "sd"


@app.route('/')
def home():
    return render_template("index.html")

@app.route('/home')
def home_page():
    cervejas = kero.listagemDeitensTroca()
    return render_template('home.html', cervejas=cervejas)

@app.route('/login', methods = ["POST", "GET"])
def login_page():
    resposta=""
    if request.method == 'POST':
        usuario = request.form.get('usuario')
        senha = request.form.get('senha')
        logado = kero.autenticacao(usuario)     
        if (logado == "T"):
            session["usuario"] = usuario
            return redirect(url_for("bar_page"))                     
        else: 
            resposta = "Faça o cadastro!"
            return render_template('login.html', resposta=resposta)                       
    else:
        return render_template('login.html', resposta=resposta)

@app.route('/usuario', methods = ["POST", "GET"])
def bar_page():
    if "usuario" in session:
        usuario = session["usuario"]
        cervejas = kero.listagemDeitensTroca()
        return render_template('bar.html', cervejas=cervejas, usuario=usuario)
    else:
        return render_template('login.html', resposta="Não está logado!")

@app.route('/geladeira')
def geladeira_page():
    cervejas = kero.listagemMeusItens("claudio")
    print(cervejas)
    return render_template('geladeira.html', cervejas=cervejas)

if __name__ == '__main__':
    app.run(debug=True)
