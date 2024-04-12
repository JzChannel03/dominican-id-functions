import random
from typing import List

init_numbers = ["4", "0", "2"]


def generate_random_id_number(init_numbers: List[str] = init_numbers) -> str:
    """
    Generates a random Ecuadorian identification number (Cédula) starting with predefined initial numbers.

    Args:
        init_numbers (List[str], optional): An array of strings representing the initial numbers. Defaults to ["4", "0", "2"].

    Returns:
        str: The randomly generated identification number.
    """
    id_number: List[str] = init_numbers.copy()  # Copy the initial numbers
    for _ in range(11 - len(init_numbers)):
        random_number = random.randint(0, 9)
        id_number.append(str(random_number))
    return "".join(id_number)
