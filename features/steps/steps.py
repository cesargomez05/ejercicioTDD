from behave import *
import requests

@given('a {num1} and {num2} values to sum')
def step_impl(context, num1, num2):
    context.api_url = 'http://127.0.0.1:4001?num1='+num1+'&num2='+num2

@when('the calculator sums the values')
def step_impl(context):
    response = requests.post(url = context.api_url, headers = {'content-type': 'application/json'})
    response = response.json();

    if 'result' in response:
        context.result = response['result']

@then('the {total:d} of sum is correct')
def step_impl(context, total):
    if 'result' in context:
        assert (context.result == total)
    else:
        assert False
    