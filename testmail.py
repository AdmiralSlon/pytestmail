import pytest


@pytest.mark.parametrize('k,v', [('1', 2)])
def test_dict_add(k: str, v: int):
    a = {}
    a[k] = v
    assert a['1'] == 2


def test_dict_get():
    a = {'a': 'b'}
    b = a.get('c', '')
    assert b == ''


def test_dict_pop():
    a = {'1': '2'}
    a.pop('1')
    assert a != {'1': '2'}


def test_float_zero():
    a = float(1.2)
    assert a * 0 == 0


@pytest.mark.parametrize('f,s,r', [(1.2, 2.0, 3.2), (1.0, 2.0, 3.0)])
def test_float_add(f, s, r):
    assert f + s == r


def test_float_mult():
    assert 1.2 * 3.0 != 3.6