from parse_csv import deserialize_movies_from_csv


def main():
    CSV_FILENAME = "final_dataset.csv"

    try:
        movies_list = deserialize_movies_from_csv(CSV_FILENAME)
    except Exception as e:
        print(f"Hubo un problema al deserializar el CSV: {e}")
        raise e

#    print("Mostrando las primeras 5 peliculas:\n\n")
#
#    for index in range(5):
#        for param, value in movies_list[index].__dict__.items():
#            print(f"{param}: {value}", end="\t")
#
#        print("\n"*2)
    numeric_fields = {
        '1': 'production_budget',
        '2': 'domestic_gross',
        '3': 'foreign_gross',
        '4': 'worldwide_gross',
        '5': 'profit',
        '6': 'profit_margin',
        '7': 'roi',
        '8': 'popularity',
        '9': 'vote_average',
        '10': 'vote_count',
        '11': 'release_date'  # Agregar opción de fecha
    }

    print("Selecciona el campo numérico para ordenar:")
    for key, value in numeric_fields.items():
        print(f"{key}: {value}")

    field_choice = input("Introduce el número del campo que quieres usar: ")
    if field_choice not in numeric_fields:
        print("Opción no válida.")
        return

    n = int(input("¿Cuántas películas quieres ver en el top N? "))

    # Obtener el campo correspondiente
    field_name = numeric_fields[field_choice]

    # Ordenar películas según el campo seleccionado
    sorted_movies = sorted(
        movies_list, key=lambda x: getattr(x, field_name), reverse=True)

    # Mostrar el top N
    print(f"Top {n} películas según {field_name}:")
    for movie in sorted_movies[:n]:
        if field_name == 'release_date':
            print(f"{movie.movie} - {movie.release_date}")
        else:
            print(f"{movie.movie} ({movie.year}) - {getattr(movie, field_name)}")


if __name__ == "__main__":
    main()
