def perform_operation(num1, num2, operation):
    """
    Performs basic arithmetic operations.
    :param num1: first number (float)
    :param num2: second number (float)
    :param operation: string ('add', 'subtract', 'multiply', 'divide')
    :return: result of the operation or error message
    """
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 == 0:
            return "Error: Division by zero"
        return num1 / num2
    else:
        return "Error: Invalid operation"



