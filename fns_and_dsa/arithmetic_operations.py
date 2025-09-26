def perform_operation(num1: float, num2: float, operation: str):
    """
    Performs basic arithmetic operations (add, subtract, multiply, divide).

    Args:
        num1 (float): The first operand.
        num2 (float): The second operand.
        operation (str): The operation to perform ('add', 'subtract', 'multiply', 'divide').

    Returns:
        float or str: The result of the operation, or a string error message
                      for division by zero or an invalid operation.
    """
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            # Handle division by zero by returning a specific string message
            return "Error: Cannot divide by zero."
        return num1 / num2
    else:
        # Handle cases where the operation string is invalid
        return "Error: Invalid operation specified."

# Example of how the provided main.py would use this function:
# from arithmetic_operations import perform_operation
# result = perform_operation(5, 6, 'add')
# print(result) # Output: 11.0
# result_div_zero = perform_operation(10, 0, 'divide')
# print(result_div_zero) # Output: Error: Cannot divide by zero.
