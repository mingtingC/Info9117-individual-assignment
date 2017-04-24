from behave import given, when, then, use_step_matcher
from hamcrest import assert_that, equal_to
import re
from login_utils import login

@given(u'a user visits the site')
def visit(ctx):
    ctx.browser.get(ctx.home)


@then(u'she should see Flaskr')
def see(ctx):
    flaskr_found = re.search("Flaskr", ctx.browser.page_source, re.IGNORECASE)
    assert flaskr_found


@given(u'she is not logged in')
def is_not_logged_in(ctx):
    # can't really test this except if one sees the Login link
    pass

@then(u'she should see the Login link')
def see_login(ctx):
    login_found = re.search("log in", ctx.browser.page_source, re.IGNORECASE)
    assert login_found


@when(u'she logs in')
def logs_in(ctx):
    login(ctx)

@when(u'she returns to the site')
def return_visit(ctx):
    ctx.browser.get(ctx.home)


@then(u'she should see the Logout link')
def step_impl(ctx):
    logout_found = re.search("log out", ctx.browser.page_source, re.IGNORECASE)
    assert logout_found
