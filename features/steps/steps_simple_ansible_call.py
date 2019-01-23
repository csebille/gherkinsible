# -*- coding: UTF-8 -*-
"""
Based on ``behave tutorial``
"""

# @mark.steps
# ----------------------------------------------------------------------------
# STEPS:
# ----------------------------------------------------------------------------
from behave import given, when, then
from suitable import Api
from hamcrest import assert_that, equal_to, is_not

@given('I connect on {server_name}')
def step_impl(context, server_name):
    context.server_name = server_name
    context.api = Api(
        server_name,
        remote_user='root',
        remote_pass='centos7'
    )

@when('I ask who am I')
def step_impl(context):
   context.answer = context.api.command('whoami').stdout()

@then('the answer is {expected_answer}')
def step_impl(context, expected_answer):
    assert_that(context.answer, equal_to(expected_answer))
