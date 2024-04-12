import json
import requests as req


def is_real_id(cedula: str) -> bool:
    """
    Checks if a Dominican identification number (Cédula) is valid by querying a government API.

    Args:
        cedula (str): The identification number to check.

    Returns:
        bool: True if the identification number is valid, False otherwise.
    """
    response = req.get(f"https://api.digital.gob.do/v3/cedulas/{cedula}/validate")
    data = json.loads(response.text)
    return data["valid"]
