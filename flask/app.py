from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return "Bienvenido a mi aplicación Flask!!"
@app.route('/saludo')
def saludo():
    nombre = request.args.get('nombre',' ')
    return f"<h1>Hola,{nombre}!</h1>"

@app.route('/sumar/<int:a>/<int:b>')
def sumar(a, b):
    resultado = a + b
    return f"<h1>La suma de {a} y {b} es {resultado}</h1>"
def operaciones(op, num1, num2):
    """ dependiendo de la operación mostrar la suma, resta, multiplicación o división """
    if op == "suma":
        resultado = num1 + num2
        operacion = "suma"
    elif op == "resta":
        resultado = num1 - num2
        operacion = "resta"
    elif op == "multiplicacion":
        resultado = num1 * num2
        operacion = "multiplicación"
    elif op == "division":
        if num2 == 0:
            return "<h1>Error: No se puede dividir entre cero</h1>"
        resultado = num1 / num2
        operacion = "división"
    else:
        return "<h1>Operación no válida. Usa: suma, resta, multiplicacion o division</h1>"

    return f"<h1>La {operacion} de {num1} y {num2} es {resultado}</h1>"

app.run(debug=True)