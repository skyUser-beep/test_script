from hello_jenkins import main

def test_jenkins_python():
    assert callable(main)
def test_basic_calculation():
    assert 2 + 2 == 4