from flask import Flask, jsonify, request
import math

app = Flask(__name__)

def calcular_factorial(n):
    """Calcula el factorial de un número"""
    if n < 0:
        return None
    if n == 0 or n == 1:
        return 1
    return math.factorial(n)

def es_par(numero):
    """Determina si un número es par o impar"""
    return "par" if numero % 2 == 0 else "impar"

@app.route('/factorial/<int:numero>', methods=['GET'])
def obtener_factorial(numero):
    """
    Endpoint que recibe un número y devuelve:
    - El número recibido
    - Su factorial
    - Etiqueta "par" o "impar" para el factorial
    """
    try:
        # Calcular el factorial
        factorial = calcular_factorial(numero)
        
        if factorial is None:
            return jsonify({
                "error": "No se puede calcular el factorial de números negativos"
            }), 400
        
        # Determinar si el factorial es par o impar
        etiqueta = es_par(factorial)
        
        # Crear respuesta JSON
        respuesta = {
            "numero_recibido": numero,
            "factorial": factorial,
            "etiqueta": etiqueta
        }
        
        return jsonify(respuesta)
    
    except Exception as e:
        return jsonify({
            "error": f"Error interno del servidor: {str(e)}"
        }), 500

@app.route('/', methods=['GET'])
def index():
    """Endpoint raíz con información del servicio"""
    return jsonify({
        "message": "Microservicio de Cálculo de Factorial",
        "endpoints": {
            "factorial": "/factorial/<numero>",
            "health": "/health"
        },
        "example": "/factorial/5"
    })

@app.route('/health', methods=['GET'])
def health_check():
    """Endpoint para verificar que el servicio esté funcionando"""
    return jsonify({"status": "OK", "message": "Servicio funcionando correctamente"})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
