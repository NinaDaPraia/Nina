from paver.easy import *


@task
def unit_test():
    sh('python manage.py test --pattern="test_*"')

@task
def selenium_test():
    sh('python manage.py test --pattern="tests_selenium_*')

@task
def test_all():
    sh('python manage.py test')

@task
def flake8():
    sh('flake8 apps')

@task
def test_and_code_style():
    call_task('flake8')
    call_task('test_all')
