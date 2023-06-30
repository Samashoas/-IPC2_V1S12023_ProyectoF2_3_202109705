from flask import Flask, jsonify
from flask import request #pip install flask

app = Flask(__name__)

@app.route('/getUsuarios', methods=['GET'])
def getCliente():
    try:
        if request.method == 'GET':
            retorno = [
                        {
                        "rol": "cliente",
                        "nombre": "Alicia",
                        "apellido": "Martínez",
                        "telefono": "555555555",
                        "correo": "alicia.johnson@example.com",
                        "contrasena": "qwerty789"
                        },
                        {
                        "rol": "cliente",
                        "nombre": "Bob",
                        "apellido": "Williams",
                        "telefono": "999999999",
                        "correo": "bob.williams@example.com",
                        "contrasena": "securepassword123"
                        },
                        {
                        "rol": "cliente",
                        "nombre": "Elena",
                        "apellido": "García",
                        "telefono": "777777777",
                        "correo": "elena.garcia@example.com",
                        "contrasena": "abc123xyz"
                        }
                      ]
        else:
            retorno = {'mensaje': 'Error en la petición, método incorrecto'}
        return jsonify(retorno)
    except:
        return {"mensaje": "Error interno en el servidor", "status": 500}

@app.route('/getPelis', methods=['GET'])
def getPeliculas():
    try:
        if request.method == 'GET':
            retorno = [
                        {
                        "Categoria": "Ciencia ficcion",
                        "titulo": "Blade Runner",
                        "director": "Ridley Scott",
                        "anio": "2006",
                        "fecha": "29/06/2023",
                        "hora": "07:00",
                        "imagen": "qwerty789",
                        "precio": "42"
                        },
                        {
                        "Categoria": "Ciencia ficcion",
                        "titulo": "The Matrix",
                        "director": "Lana Wachowsk",
                        "anio": "2004",
                        "fecha": "15/07/2022",
                        "hora": "15:00",
                        "imagen": "qwerty789",
                        "precio": "42"
                        },
                        {
                        "Categoria": "Ciencia ficcion",
                        "titulo": "Interstellar",
                        "director": "Christopher Nolan",
                        "anio": "2002",
                        "fecha": "16/08/2002",
                        "hora": "17:00",
                        "imagen": "qwerty789",
                        "precio": "42"
                        }
                      ]
        else:
            retorno = {'mensaje': 'Error en la petición, método incorrecto'}
        return jsonify(retorno)
    except:
        return {"mensaje": "Error interno en el servidor", "status": 500}

@app.route('/getSalas', methods=['GET'])
def getSalas():
    try:
        if request.method == 'GET':
            retorno = [
                        {
                        "cine": "BCA",
                        "numero": "#USACIPC2_202212333_40",
                        "asientos": "150"
                        },
                        {
                        "cine": "BCA",
                        "numero": "#USACIPC2_202212333_42",
                        "asientos": "110"
                        },
                        {
                        "cine": "BCA",
                        "numero": "#USACIPC2_202212333_44",
                        "asientos": "120"
                        }
                      ]
        else:
            retorno = {'mensaje': 'Error en la petición, método incorrecto'}
        return jsonify(retorno)
    except:
        return {"mensaje": "Error interno en el servidor", "status": 500}

@app.route('/getTarjetas', methods=['GET'])
def getTarjetas():
    try:
        if request.method == 'GET':
            retorno = [
                        {
                        "tipo": "Credito",
                        "numero": "95848484717141",
                        "titular": "Jose",
                        "fecha": "09/2024"
                        },
                        {
                        "tipo": "Debito",
                        "numero": "556584911321512",
                        "titular": "Emilio",
                        "fecha": "09/2025"
                        },
                        {
                        "tipo": "Credito",
                        "numero": "1514714155165181",
                        "titular": "Gustavo",
                        "fecha": "09/2026"
                        }
                      ]
        else:
            retorno = {'mensaje': 'Error en la petición, método incorrecto'}
        return jsonify(retorno)
    except:
        return {"mensaje": "Error interno en el servidor", "status": 500}
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5007)