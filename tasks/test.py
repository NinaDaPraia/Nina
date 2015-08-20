from paver.easy import *

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
