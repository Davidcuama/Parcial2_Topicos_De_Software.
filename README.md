# Microservicio de Cálculo de Factorial

Este microservicio recibe un número por URL y devuelve una respuesta JSON con el número recibido, su factorial y una etiqueta indicando si el factorial es par o impar.

## Instalación y Ejecución

1. Instalar dependencias:
```bash
pip install -r requirements.txt
```

2. Ejecutar el servidor:
```bash
python app.py
```

El servidor se ejecutará en `http://localhost:5000`

## Uso

### 1. Verificar que el servicio esté funcionando
```
GET http://localhost:5000/
```

**Respuesta:**
```json
{
    "message": "Microservicio de Cálculo de Factorial",
    "endpoints": {
        "factorial": "/factorial/<numero>",
        "health": "/health"
    },
    "example": "/factorial/5"
}
```

### 2. Endpoint Principal
```
GET /factorial/<numero>
```

**Ejemplo:**
```
GET http://localhost:5000/factorial/5
```

**Respuesta:**
```json
{
    "numero_recibido": 5,
    "factorial": 120,
    "etiqueta": "par"
}
```

### 3. Health Check
```
GET http://localhost:5000/health
```

**Respuesta:**
```json
{
    "status": "OK",
    "message": "Servicio funcionando correctamente"
}
```

## Pasos para Probar

1. **Ejecutar el servidor:**
   ```bash
   python app.py
   ```

2. **Abrir navegador o usar curl:**
   - Primero prueba: `http://localhost:5000/`
   - Luego prueba: `http://localhost:5000/factorial/5`
   - También puedes probar: `http://localhost:5000/health`

3. **Usando curl desde terminal:**
   ```bash
   curl http://localhost:5000/
   curl http://localhost:5000/factorial/5
   curl http://localhost:5000/health
   ```

## Características

-  Recibe un número por URL
-  Calcula el factorial del número
-  Determina si el factorial es par o impar
-  Devuelve respuesta en formato JSON
-  Manejo de errores para números negativos
-  Endpoint de health check

## Notas

- El microservicio está diseñado para ser simple y funcional
- No incluye persistencia de datos
- Ideal para demostración y pruebas rápidas
