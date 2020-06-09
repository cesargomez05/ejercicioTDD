from behave import *
import requests

@given('a {values} to sum')
def step_impl(context, values):
    context.api_url = ''

    #context.calculadora = Calculadora()
    #context.values = values.split(',')

@when('the calculator sums the values')
def step_impl(context):
    pass
    #context.total = context.calculadora.sumar(int(context.values[0]),int(context.values[1]))

@then('the {total:d} of sum is correct')
def step_impl(context, total):
    pass
    #assert (context.total == total)