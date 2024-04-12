# Dominican ID Functions

Python functions to generate and validate Dominican identification numbers (Cédula).

## Description

This Python package provides convenient functions for working with Dominican identification numbers (Cédula). It includes functions to generate random identification numbers with predefined initial numbers and to validate whether a given identification number is valid and real by querying a government API.

<!--
## Installation

You can install the package via pip:

```bash
pip install Dominican-id-functions
```
-->


## Usage

Here's an example of how to use the functions provided by this package:

```python
from id_functions import generate_random_id_number, validate_by_number, is_real_id

vericed = False
id_number = ""
while vericed == False:
    id_number = generate_random_id_number(["0", "2", "3", "0", "0"])
    is_valid = validate_by_number(id_number)
    if is_valid:
        vericed = True

print(f"Cédula válida generada exitosamente, con número: {id_number}")

is_real = is_real_id(id_number)

if is_real:
    print("Además, es una cédula válida y real (Perteneciente a alguien)")
else:
    print("Aunque, es una cédula válida pero irreal (Aún no está registrada o no se ha asignado a alguien)")

```

## License

This project is licensed under the MIT License - see the LICENSE file for details.
