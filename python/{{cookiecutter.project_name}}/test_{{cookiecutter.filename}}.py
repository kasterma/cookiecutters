## test_{{ cookiecutter.filename }}.py

from {{ cookiecutter.filename }} import f

def test_f():
    assert f() == 4  # failing b/c f() returns 5
