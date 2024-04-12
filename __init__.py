# main function (Use example) for the id_functions package
from id_functions.create_id import generate_random_id_number
from id_functions.validate_id import by_number as validate_by_number
from id_functions.get_id_data import is_real_id


def main():
    vericed = False
    id_number = ""
    while vericed == False:
        id_number = generate_random_id_number(["0", "2", "3", "0", "0"])
        is_valid = validate_by_number(id_number)
        if is_valid:
            vericed = True

    print(f"Cédula válida generada exitosamente, con número: {id_number}")

    is_real = is_real_id(id_number)

    match (is_real):
        case True:
            print("Además, es una cédula válida y real (Perteneciente a alguien)")
        case False:
            print(
                "Aunque, es una cédula válida pero irreal (Aún no está registrada o no se ha asignado a alguien)"
            )


main()
