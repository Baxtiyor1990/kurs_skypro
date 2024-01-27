from your_module import read_operations, get_last_executed_operations, display_operations

def main():
    operations_data = read_operations('venv/operations/operations.json')
    last_executed_operations = get_last_executed_operations(operations_data)
    display_operations(last_executed_operations)

if __name__ == "__main__":
    main()

