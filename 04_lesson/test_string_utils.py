import pytest
from string_utils import StringUtils


utils = StringUtils()


# Тесты для capitalize
@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
    ("SkyPro", "Skypro"),
])
def test_capitalize_positive(input_str, expected):
    assert utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
    ("!hello", "!hello"),
])
def test_capitalize_negative(input_str, expected):
    assert utils.capitalize(input_str) == expected


# Тесты для trim
@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("   skypro", "skypro"),
    ("skypro", "skypro"),
    ("   sky pro   ", "sky pro   "),
])
def test_trim_positive(input_str, expected):
    assert utils.trim(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("", ""),
    ("   ", ""),
    ("skypro   ", "skypro   "),
])
def test_trim_negative(input_str, expected):
    assert utils.trim(input_str) == expected


# Тесты для contains
@pytest.mark.positive
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "S", True),
    ("SkyPro", "Pro", True),
    ("abc", "abc", True),
])
def test_contains_positive(string, symbol, expected):
    assert utils.contains(string, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "U", False),
    ("", "a", False),
    ("abc", "", False),
    ("abc", "d", False),
    (None, "a", False),
])
def test_contains_negative(string, symbol, expected):
    assert utils.contains(string, symbol) == expected


# Тесты для delete_symbol
@pytest.mark.positive
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "k", "SyPro"),
    ("SkyPro", "Pro", "Sky"),
    ("abcabc", "b", "acac"),
])
def test_delete_symbol_positive(string, symbol, expected):
    assert utils.delete_symbol(string, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "x", "SkyPro"),
    ("", "a", ""),
    ("abc", "", "abc"),
    (None, "a", None),
])
def test_delete_symbol_negative(string, symbol, expected):
    assert utils.delete_symbol(string, symbol) == expected
