def perform_operation(num1, num2, operation):
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
    # Ensure operation is lowercase for comparison
    operation = operation.strip().lower()
    
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            # Handle division by zero
            return "Error: Cannot divide by zero."
        return num1 / num2
    else:
        # Handle cases where the operation string is invalid
        return "Error: Invalid operation specified."
