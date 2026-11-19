from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    resultado = None
    promedio = None

    if request.method == 'POST':
        nota1 = float(request.form['nota1'])
        nota2 = float(request.form['nota2'])
        nota3 = float(request.form['nota3'])
        asistencia = float(request.form['asistencia'])

        promedio = round((nota1 + nota2 + nota3) / 3, 1)

        if promedio >= 40 and asistencia >= 75:
            resultado = "APROBADO"
        else:
            resultado = "REPROBADO"

    return render_template('ejercicio1.html', resultado=resultado, promedio=promedio)

@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    resultado = None
    cantidad = None

    if request.method == 'POST':
        nombre1 = request.form['nombre1']
        nombre2 = request.form['nombre2']
        nombre3 = request.form['nombre3']

        nombres = [nombre1, nombre2, nombre3]
        mayor = max(nombres, key=len)

        resultado = f"El nombre más largo es: {mayor}"
        cantidad = len(mayor)

    return render_template('ejercicio2.html', resultado=resultado, cantidad=cantidad)

if __name__ == '__main__':
    app.run(debug=True)