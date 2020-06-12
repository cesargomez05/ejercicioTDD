# Ejercicio final: TDD

## Integrantes
* Laura Alejandra Campos - 20201099028
* Steven Fabián Gómez - 20201099030
* César Augusto Gómez - 20201099031
* Edna Nayibe Palma - 20201099041

## Objetivo de la solución
Elaboración de un entorno de pruebas de comportamiento para 4 microservicios encargados de sumar, restar, multiplicar y dividir dos números.

## Recursos utilizados
- Python 3.x
- Flask
- pytest==5.1.2
- behave

## Configuración .feature

A continuación se realiza una breve descripción que resume cada uno de los escenarios contemplados en cada una de las operaciones (suma,resta,multiplicación,división)

```feature
Scenario Outline: Obtener la (suma,resta,multiplicación,división) de dos números
  Given Los valores <num1> y <num2> a (sumar,restar,multiplicar,dividir)
  When El microservicio realice la (suma,resta,multiplicación,división) de los valores
  Then El <total> de la (suma,resta,multiplicación,división) es correcto

  Examples: values
  | num1 | num2 | total |
  | 1    | 2    | 3     |
  | 5    | 3    | 8     |
  | 15   | 33   | 48    |
```

## Configuración archivo steps.py

A continuación se presenta 

```py
@given('Los valores {num1} y {num2} a (sumar,restar,multiplicar,dividir)')
def step_impl(context, num1, num2):
    context.api_url = 'URL_MICROSERVICIO?num1='+num1+'&num2='+num2

@when('El microservicio realice la (suma,resta,multiplicación,división) de los valores')
def step_impl(context):
    # Se ejecuta el llamado al microservicio
    response = requests.post(url = context.api_url, headers = {'content-type': 'application/json'})
    response = response.json();

    # Se valida si el objeto JSON retornó el resultado de la operación
    if 'result' in response:
        context.result = response['result']
    elif 'message' in response:
        # Si el llamado al Web Service retornó un mensaje de error
        context.message = response['message']
    else:
        context.message = 'Error'

@then('El {total:d} de la (suma,resta,multiplicación,división) es correcto')
def step_impl(context, total):
    if 'result' in context:
        assert (context.result == total)
    else:
        print(content.message)
        assert False
```