from flask import Flask, jsonify, request
from divec import administrador

app = Flask('inicio')
admin = administrador()

@app.route("/buscar_profesor_nombre", methods=['POST'])
def buscar_profesor_nombre():

    lista = admin.buscar_profesor_nombre(request.form['patron'])

    res = jsonify(lista)

    res.headers.add("Access-Control-Allow-Origin", "*")
    print(res)
    return res

@app.route("/buscar_materia_profesor", methods=['POST'])
def buscar_materia_profesor():

    lista = admin.buscar_materia_profesor(request.form['patron'],request.form['cicle'])

    res = jsonify(lista)

    res.headers.add("Access-Control-Allow-Origin", "*")
    print(res)
    return res

@app.route("/buscar_profesor_materia", methods=['POST'])
def buscar_profesor_materia():

    lista = admin.buscar_profesor_materia(request.form['patron'],request.form['cicle'])

    res = jsonify(lista)

    res.headers.add("Access-Control-Allow-Origin", "*")
    print(res)
    return res

@app.route("/buscar_profesor_puesto", methods=['POST'])
def buscar_profesor_puesto():

    lista = admin.buscar_profesor_puesto(request.form['patron'])

    res = jsonify(lista)

    res.headers.add("Access-Control-Allow-Origin", "*")
    print(res)
    return res

app.run()
