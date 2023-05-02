from flask import Flask, request, render_template
from funciones.dni import dni
from funciones.bisiesto import bisiesto
from funciones.primo import primo

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
        pass
    if int(request.form["opcion"]) == 5:
        pass
    if int(request.form["opcion"]) == 6:
        pass
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

if __name__ == '__main__':
   app.run(debug=True)