def by_number(id_number: str) -> bool:
    """
    Validates an Dominican identification number (Cédula) using the modulus 10 algorithm.

    Args:
        id_number (str): The identification number to validate.

    Returns:
        bool: True if the identification number is valid, False otherwise.
    """
    digits = [
        int(digit) for digit in id_number
    ]  # Convert the string to a list of integers
    total_sum = 0

    for index, _ in enumerate(digits):
        if index % 2 == 1:
            digits[index] *= 2

        if digits[index] > 9:
            digits[index] -= 9

        if index <= 9:
            total_sum += digits[index]

    check_digit = 0 if total_sum % 10 == 0 else 10 - (total_sum % 10)

    return check_digit == digits[10]
