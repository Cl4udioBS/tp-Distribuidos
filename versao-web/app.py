from flask import Flask, render_template, request, redirect, url_for, session
import rns as kero
import os
from datetime import timedelta
import database as db

nomeBanco = "TPSD.db"

db.InicializaBD()  

app = Flask(__name__)
'''todos os dados de sessao sao encriptados no lado do servidor, para isso a key'''
app.secret_key = "sd"
app.permanent_session_lifetime = timedelta(minutes=5)

@app.route('/', methods = ["POST", "GET"])
def login_page():
    resposta=""
    if request.method == 'POST':
        usuario = request.form.get('usuario')
        senha = request.form.get('senha')
        logado = kero.autenticacao(usuario)     
        if (logado == "T"):
            session.permanent = True
            session["usuario"] = usuario
            return redirect(url_for("bar_page"))                     
        else: 
            resposta = "Faça o cadastro!"
            return render_template('login.html', resposta=resposta)                       
    else:
        if "usuario" in session:
           return  redirect(url_for("bar_page"))
        return render_template('login.html', resposta=resposta)

@app.route("/logout")
def logout():
    session.pop("usuario", None)
    return redirect(url_for("login_page"))

@app.route('/bar', methods = ["GET"])
def bar_page():
    if "usuario" in session:
        usuario = session["usuario"]
        cervejas = kero.listagemDeitensTroca()
        return render_template('bar.html', cervejas=cervejas, usuario=usuario)
    else:
        return render_template('login.html', resposta="Não está logado!")

@app.route('/geladeira', methods = ["GET"])
def geladeira_page():
    cervejas = kero.listagemMeusItens("claudio")
    return render_template('geladeira.html', cervejas=cervejas)

@app.route('/trocas', methods = ["POST", "GET"])
def trocas_page():
    if "usuario" in session:
            usuario = session["usuario"]
            #listagens
            cervejas = kero.listagemDeitensTroca()
            trocasDisponiveis = kero.listarTrocasPendentes(usuario)
            if request.method == 'POST':
                #resposta
                indice = request.form.get('indice')
                if  request.form.get('btn') == "Kero":
                    kero.responderSolicitacao('k',int(indice))
                    return render_template('trocas.html', cervejas=cervejas, usuario=usuario, trocasDisponiveis = trocasDisponiveis)
                else:
                    kero.responderSolicitacao('nao',request.form["indice"])
                    return render_template('trocas.html', cervejas=cervejas, usuario=usuario, trocasDisponiveis = trocasDisponiveis)
            else:
                return render_template('trocas.html', cervejas=cervejas, usuario=usuario, trocasDisponiveis = trocasDisponiveis)

            
    else:
        return render_template('login.html', resposta="Não está logado!")


if __name__ == '__main__':
    app.run(debug=True)
