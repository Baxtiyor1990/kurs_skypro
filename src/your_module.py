import json

def read_operations(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

def get_last_executed_operations(operations):
    executed_operations = [operation for operation in operations if 'state' in operation and operation['state'] == 'EXECUTED']
    last_executed_operations = sorted(executed_operations, key=lambda x: x.get('date', ''), reverse=True)[:5]
    return last_executed_operations


def display_operations(operations):
    for operation in operations:
        print(f"{operation.get('date', '')} {operation.get('description', '')}")
        print(f"{operation.get('from', '')} -> {operation.get('to', '')}")
        print(f"{operation.get('operationAmount', '')}")
        print()



def main():
    file_path = 'venv/operations/operations.json'
    operations_data = read_operations(file_path)
    last_executed_operations = get_last_executed_operations(operations_data)
    display_operations(last_executed_operations)

if __name__ == "__main__":
    main()
