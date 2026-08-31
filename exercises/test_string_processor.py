import pytest
from string_processor import StringProcessor

# Позитивные тесты
@pytest.mark.parametrize("input_text, expected", [
    ("hello world", "Hello world."),
    ("Hello.", "Hello."),
    ("", "."),  # пустая строка
])
def test_process_positive(input_text, expected):
    assert StringProcessor.process(input_text) == expected

# Негативные тесты (граничные случаи)
@pytest.mark.parametrize("input_text, expected", [
    ("   hello", "   hello."),   # пробелы в начале – первая буква – пробел
    ("123abc", "123abc."),       # цифры в начале
    ("  ", "  ."),               # только пробелы
])
def test_process_negative(input_text, expected):
    assert StringProcessor.process(input_text) == expected