# Configuración inicial

Antes de comenzar se debe aplicar migraciones

python manage.py makemigrations
python manage.py migrate


## Ejecucion del servidor en terminal

python manage.py runserver

## Descripción y uso de los Endpoints

## App Customer

### URL incial: http://127.0.0.1:8000/customer


### `/create_customer`

Endpoint usado para crear el customer nuevo (POST)

Estructura de la petición (JSON)

    ```json
    {
        "score": 150.00,
        "status": 1
    }
    ```

### `/customer_list`

Endpoint usado para consultar la lista de clientes existentes (GET)


### `/balance`

Endpoint usado para consultar la deuda total de un cliente existente

Para la consulta se debe enviar como parámetro el ID del cliente obtenido en el Endpoint anterior (external_id)


## App Loans

### URL incial: http://127.0.0.1:8000/loan


### `/create_loan`

Endpoint usado para crear el customer préstamo (POST)

Estructura de la petición (JSON)

    ```json
    {
        "customer_external_id": "bdb1d05a-3fe7-4645-bff4-d54fca1551ba",
        "amount": 1500.00,
        "outstanding": 2000.00,
        "status": 1
    }
    ```

### `/list_loans`

Endpoint usado para consultar todos los préstamos existentes


### `/get_loans_by_customer`

Endpoint usado para consultar todos los préstamos asignados por cliente

Para la consulta se debe enviar como parámetro el ID del cliente obtenido en el Endpoint anterior (customer_id)

