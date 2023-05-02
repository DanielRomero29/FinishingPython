from flask import Flask, request, render_template
from funciones.dni import dni
from funciones.bisiesto import bisiesto
from funciones.primo import primo
from funciones.celsius import celsius as c
from funciones.parImpar import parImpar as pim
from funciones.factorial import fac

app = Flask(__name__,template_folder='html')
@app.route("/")
def home():
    return render_template('main.html')


@app.route("/validarOpcion", methods=['POST'])
def verificarOpcion():
    if int(request.form["opcion"]) == 1: 
        return render_template('dni.html')
    if int(request.form["opcion"]) == 2:
        return render_template('bisiesto.html')
    if int(request.form["opcion"]) == 3:
        return render_template('primo.html')
    if int(request.form["opcion"]) == 4:
        return render_template('celsius.html')
    if int(request.form["opcion"]) == 5:
        return render_template('parImpar.html')
    if int(request.form["opcion"]) == 6:
        return render_template('factorial.html')
    if int(request.form["opcion"]) == 0:
        return render_template('despedida.html', ejercicio="Menú")
    
@app.route("/validarOpcion/dni", methods=['POST'])
def verificacionDNI():
    dniPaginaWeb = request.form["dni"]
    resultado = dni(dniPaginaWeb)
    return render_template('resultado.html', ejercicio="Letra DNI", resultado=resultado, url="/validarOpcion/dni/continuar")

@app.route("/validarOpcion/dni/continuar", methods=['POST'])
def continuarDNI():
    continuarPaginaWeb = request.form["opcion"]
    if continuarPaginaWeb == "s":
        return render_template('main.html')
    else:
        return render_template('despedida.html', ejercicio="Letra DNI")

@app.route("/validarOpcion/bisiesto", methods=['POST'])
def verificacionBisiesto():
    añoPaginaWeb = request.form["año"]
    resultado = bisiesto(añoPaginaWeb)
    return render_template('resultado.html', ejercicio="Año bisiesto", resultado=resultado, url="/validarOpcion/bisiesto/continuar")

@app.route("/validarOpcion/bisiesto/continuar", methods=['POST'])
def continuarBisiesto():
    continuarPaginaWeb = request.form["opcion"]
    if continuarPaginaWeb == "s":
        return render_template('main.html')
    else:
        return render_template('despedida.html', ejercicio="Año bisiesto")

@app.route("/validarOpcion/primo", methods=['POST'])
def verificacionPrimo():
    primoPaginaWeb = request.form["numero"]
    resultado = primo(primoPaginaWeb)
    return render_template('resultado.html', ejercicio="Número primo", resultado=resultado, url="/validarOpcion/primo/continuar")

@app.route("/validarOpcion/primo/continuar", methods=['POST'])
def continuarPrimo():
    continuarPaginaWeb = request.form["opcion"]
    if continuarPaginaWeb == "s":
        return render_template('main.html')
    else:
        return render_template('despedida.html', ejercicio="Número primo")

@app.route("/validarOpcion/cambioAFarhenheit", methods=['POST'])
def cambioAFahrenheit():
    celsius = request.form["celsius"]
    resultado = c(celsius)
    return render_template("resultado.html",resultado=resultado, ejercicio="Pasar de Celsius a Fahrenheit", url="/validarOpcion/cambioAFarhenheit/continuar")

@app.route("/validarOpcion/cambioAFarhenheit/continuar", methods=['POST'])
def continuarCelsius():
    continuarPaginaWeb = request.form["opcion"]
    if continuarPaginaWeb == "s":
        return render_template('main.html')
    else:
        return render_template('despedida.html', ejercicio="Pasar de Celsius a Fahrenheit")
    
@app.route("/validarOpcion/parImpar", methods=['POST'])
def parImpar():
    numero = request.form["numero"]
    resultado = pim(numero)
    return render_template("resultado.html",resultado=resultado, ejercicio="Numero par o impar", url="/validarOpcion/parImpar/continuar")

@app.route("/validarOpcion/parImpar/continuar", methods=['POST'])
def continuarParImpar():
    continuarPaginaWeb = request.form["opcion"]
    if continuarPaginaWeb == "s":
        return render_template('main.html')
    else:
        return render_template('despedida.html', ejercicio="Numero par o impar")
    
@app.route("/validarOpcion/factorial", methods=['POST'])
def factorial():
    numero = request.form["numero"]
    resultado = fac(numero)
    return render_template("resultado.html",resultado=resultado, ejercicio="Factorial de un número", url="/validarOpcion/factorial/continuar")

@app.route("/validarOpcion/factorial/continuar", methods=['POST'])
def continuarFactorial():
    continuarPaginaWeb = request.form["opcion"]
    if continuarPaginaWeb == "s":
        return render_template('main.html')
    else:
        return render_template('despedida.html', ejercicio="Factorial de un número")

if __name__ == '__main__':
   app.run(debug=True)