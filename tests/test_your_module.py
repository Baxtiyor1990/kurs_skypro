import pytest
from src.your_module import read_operations, get_last_executed_operations, display_operations

def test_read_operations():
    operations_data = read_operations('venv/operations/operations.json')
    assert isinstance(operations_data, list)
    assert len(operations_data) > 0

def test_get_last_executed_operations():
    # Можно использовать фикстуры для загрузки данных и передачи их в тестовую функцию
    # Для примера, просто загрузим данные из файла
    operations_data = read_operations('venv/operations/operations.json')
    last_executed_operations = get_last_executed_operations(operations_data)
    assert isinstance(last_executed_operations, list)
    assert len(last_executed_operations) <= 5

def test_display_operations(capsys):
    # Тест вывода на экран
    operations_data = read_operations('venv/operations/operations.json')
    last_executed_operations = get_last_executed_operations(operations_data)
    display_operations(last_executed_operations)

    captured = capsys.readouterr()
    assert len(captured.out) > 0
