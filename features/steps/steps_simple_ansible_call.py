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

@given('I connect on {server_name:S}')
def step_impl(context, server_name):
    context.server_name = server_name
    context.api = Api(
        server_name,
        remote_user='root',
        remote_pass='centos7'
    )

@given('I connect on {which_ones} in {group_name} group')
def step_impl(context, which_ones, group_name):
    servers = context.inventory.get_hosts(pattern=group_name, ignore_limits=False, ignore_restrictions=False, order=None)
    servers_names=[h.get_name() for h in servers]
    context.api = Api(
        servers_names,
        remote_user='root',
        remote_pass='centos7'
    )

@step('I copy the file {local_file} on {server_name} in {target_remote_dir}')
def step_impl(context, local_file, server_name, target_remote_dir):
    context.api = Api(
        server_name,
        remote_user='root',
        remote_pass='centos7'
    )
    context.answer = context.api.copy(src=local_file, dest=target_remote_dir)


@when('I ask who am I')
def step_impl(context):
    context.answer = context.api.command('whoami').stdout()

@then('the answer is {expected_answer}')
def step_impl(context, expected_answer):
    assert_that(context.answer, equal_to(expected_answer))

