from behave import *
import requests

# SUMA
@given('a {num1} and {num2} values to sum')
def step_impl(context, num1, num2):
    context.api_url = 'http://127.0.0.1:4001?num1='+num1+'&num2='+num2

@when('the calculator sums the values')
def step_impl(context):
    response = requests.post(url = context.api_url, headers = {'content-type': 'application/json'})
    response = response.json();

    if 'result' in response:
        context.result = response['result']
    elif 'message' in response:
        context.message = response['message']
    else:
        context.message = 'Error'

@then('the {total:d} of sum is correct')
def step_impl(context, total):
    if 'result' in context:
        assert (context.result == total)
    else:
        print(content.message)
        assert False

# RESTA
@given('a {num1} and {num2} values to substract')
def step_impl(context, num1, num2):
    context.api_url = 'http://127.0.0.1:4002?num1='+num1+'&num2='+num2

@when('the calculator substract the values')
def step_impl(context):
    response = requests.post(url = context.api_url, headers = {'content-type': 'application/json'})
    response = response.json();

    if 'result' in response:
        context.result = response['result']
    elif 'message' in response:
        context.message = response['message']
    else:
        context.message = 'Error'

@then('the {total:d} of substraction is correct')
def step_impl(context, total):
    if 'result' in context:
        assert (context.result == total)
    else:
        assert False

# MULTIPLICACIÓN
@given('a {num1} and {num2} values to multiply')
def step_impl(context, num1, num2):
    context.api_url = 'http://127.0.0.1:4003?num1='+num1+'&num2='+num2

@when('the calculator multiply the values')
def step_impl(context):
    response = requests.post(url = context.api_url, headers = {'content-type': 'application/json'})
    response = response.json();

    if 'result' in response:
        context.result = response['result']
    elif 'message' in response:
        context.message = response['message']
    else:
        context.message = 'Error'

@then('the {total:d} of multiply is correct')
def step_impl(context, total):
    if 'result' in context:
        assert (context.result == total)
    else:
        assert False

# DIVISIÓN
@given('a {num1} and {num2} values to divide')
def step_impl(context, num1, num2):
    context.api_url = 'http://127.0.0.1:4004?num1='+num1+'&num2='+num2

@when('the calculator divide the values')
def step_impl(context):
    response = requests.post(url = context.api_url, headers = {'content-type': 'application/json'})
    response = response.json();

    if 'result' in response:
        context.result = response['result']
    elif 'message' in response:
        context.message = response['message']
    else:
        context.message = 'Error'

@then('the {total:d} of divide is correct')
def step_impl(context, total):
    if 'result' in context:
        assert (context.result == total)
    else:
        assert False