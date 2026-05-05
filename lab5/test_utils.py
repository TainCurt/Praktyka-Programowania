import pytest
import utils


@pytest.mark.parametrize("a, b, expected", [(1, 2, 3), (2, 3, 5), (3, 4, 7), (4, 5, 9)])
def test_add(a, b, expected):
    result = utils.add(a, b)
    assert result == expected


@pytest.mark.parametrize(
    "a, b, expected", [(1, 2, -1), (2, 3, -1), (3, 4, -1), (4, 5, -1)]
)
def test_subtract(a, b, expected):
    result = utils.subtract(a, b)
    assert result == expected


@pytest.mark.parametrize(
    "a, b, expected", [(1, 2, 2), (2, 3, 6), (3, 4, 12), (4, 5, 20)]
)
def test_multiply(a, b, expected):
    result = utils.multiply(a, b)
    assert result == expected


@pytest.mark.parametrize("a, b, expected", [(1, 2, 0.5), (3, 4, 0.75), (4, 5, 0.8)])
def test_divide(a, b, expected):
    result = utils.divide(a, b)
    assert result == expected

@pytest.mark.parametrize("a, expected", [
    (9, '01001'),
    (4, '00100'),
    (0, '00000'),
    (15, '01111'),
])
def test_valid(a, expected):
    assert utils.binary(a) == expected


@pytest.mark.parametrize("a", [-1, 120])
def test_out_of_range(a):
    with pytest.raises(ValueError):
        utils.binary(a)


@pytest.mark.parametrize("a", [5.5, "10", None])
def test_not_integer(a):
    with pytest.raises(TypeError):
        utils.binary(a)