from numeroMenor import menor

def test_menorArreglo():
    assert menor([4,5,6,2]) == 2
    assert menor([0,1,8,-1,2]) == -1