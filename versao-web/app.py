from flask import Flask, render_template, request, redirect, url_for, session
import rns as kero
import os
from datetime import timedelta
import database as db

nomeBanco = "TPSD.db"



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
            return redirect(url_for('login.html', resposta=resposta))                      
    else:
        if "usuario" in session:
           return  redirect(url_for("bar_page"))
        return render_template('login.html', resposta=resposta)

@app.route("/logout", methods = ["GET"])
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
    if "usuario" in session:
        usuario = session["usuario"]
        cervejas = kero.listagemMeusItens(usuario)
        return render_template('geladeira.html', cervejas=cervejas)
    else:
        return render_template('login.html', resposta="Não está logado!")
        
@app.route('/trocas', methods = ["POST", "GET", "PUT"])
def trocas_page():
    flag = False
    if "usuario" in session:
            usuario = session["usuario"]
            #listagens
            possuiCervejas = kero.listagemMeusItens(usuario)
            cervejas = kero.listagemDeitensTroca()
            trocasDisponiveis = kero.listarTrocasPendentes(usuario)
            if possuiCervejas != 400:
                flag = True
            if request.method == 'POST':
                #resposta
                if request.form.get('btn') == "Kero Trocar":
                    indiceindiceCervejaExec = request.form.get('indiceindiceCervejaExec')
                    indiceCervejaSolicit    = request.form.get('indiceCervejaSolicit')
                    kero.solicitaTroca(indiceCervejaSolicit,indiceindiceCervejaExec)
                    return redirect(url_for("trocas_page"))
                elif  request.form.get('btn') == "Kero":
                    indice = request.form.get('indice')
                    kero.responderSolicitacao('k',int(indice))
                    return redirect(url_for("trocas_page"))
                else:
                    kero.responderSolicitacao('nao',request.form["indice"])
                    return redirect(url_for("trocas_page"))
            else:
                return render_template('trocas.html',flag = flag, cervejas=cervejas, trocasDisponiveis = trocasDisponiveis)
    else:
        return render_template('login.html', resposta="Não está logado!")

@app.route('/cadastro', methods = ["GET","POST"])
def cadastro_page():
    if "usuario" in session:
            usuario = session["usuario"]
            #listagens
            if request.method == 'POST':
                #resposta
                cerveja = request.form.get('cerveja')
                abv     = request.form.get('abv')
                ibu     = request.form.get('ibu')
                estilo  = request.form.get('estilo')
                kero.cadastrarCerveja(cerveja, abv, ibu, estilo, usuario)
                return redirect(url_for("geladeira_page"))
            else:
                return render_template('cadastro.html', usuario = usuario)
    else:
        return redirect(url_for('login.html', resposta="Considere fazer Login"))


if __name__ == '__main__':
    db.InicializaBD()
    app.run(debug=True)
