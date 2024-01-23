# Configuración inicial

Antes de comenzar se debe aplicar migraciones

python manage.py makemigrations
python manage.py migrate

# Descripción y uso de los Endpoints

## App Customer

- **Url incial**: http://127.0.0.1:8000/customer

    - ** Para realizar la creación de un nuevo cliente
    - Endpoint: create_customer
    - Método: POST
    - Estructura de la peticion en Json:
    ```json
    {
        "score": 150.00,
        "status": 1
    }
    
