from paver.easy import *


@task
def unit_test():
    sh('python manage.py test')

@task
def flake8():
    sh('flake8 apps')

@task
def test_and_code_style():
    call_task('unit_test')
    call_task('flake8')
