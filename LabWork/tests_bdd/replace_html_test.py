from pytest import fixture
from pytest_bdd import scenarios, given, when, then

import funcs


scenarios("./features/replace_html.feature")

# Переменные для хранения данных
@fixture
def context():
    return {}

# ======================================

@given('I have the HTML content "<p>1234 1234 1234 1234<p/>"')
def given_html(context):
    context["html"] = "<p>1234 1234 1234 1234<p/>"

@when("I remove HTML tags")
def when_html(context):
    context["result"] = funcs.replace_html(context["html"])

@then('The result should be "1234 1234 1234 1234"')
def then_result(context):
    assert context["result"] == "1234 1234 1234 1234"
