from app import soma

def test_soma():
    assert soma(2, 2) == 4

def test_falha_proposital():
    assert soma(2, 2) == 5