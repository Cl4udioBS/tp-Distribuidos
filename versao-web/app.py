from flask import Flask, render_template
import database as db 
from liveserver import LiveServer

nomeBanco = "TPSD.db"

app = Flask(__name__)
ls = LiveServer (app)

@app.route('/')
@app.route('/home')
def home_page():
    cervejas = db.SelectTodasCervejas()
    return render_template('home.html', cervejas=cervejas)

@app.route('/login')
def login_page():
    return render_template('login.html')

@app.route('/bar')
def bar_page():
    cervejas = db.SelectTodasCervejas()
    return render_template('bar.html', cervejas=cervejas)

@app.route('/geladeira')
def geladeira_page():
    cervejas = db.SelectCervejaByUsuario("claudio")
    print(cervejas)
    return render_template('geladeira.html', cervejas=cervejas)


ls.run("0.0.0.0", 8080)
'''
if __name__ == '__main__':
    app.run()
'''