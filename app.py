from flask import Flask, render_template
app = Flask(__name__)

@app.route('/index')
def index ():
    return render_template('index.html')
   
@app.route('/compras')
def compras ():
    #return '<ul><li>Arroz</li></ul>'
    return render_template('compras.html')

@app.route('/mercado')
def mercado ():
    return render_template('mercados.html')








