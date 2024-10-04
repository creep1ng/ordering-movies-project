from parse_csv import deserialize_movies_from_csv
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from movie import Movie
import matplotlib
from heapq import nlargest


def create_animated_plot(movie_list: list[Movie], n: int, field: str):
    years = sorted(set(movie.year for movie in movie_list))
    fig, ax = plt.subplots(figsize=(10, 6))

    top_movies = nlargest(
        n, movie_list, key=lambda movie: getattr(movie, field))
    bars = ax.barh([movie.movie for movie in top_movies], [getattr(
        movie, field) for movie in top_movies], color="skyblue")

    ax.set_xlabel(field.capitalize())
    ax.set_title(f"Top {n} películas por {field.capitalize()} in {years[0]}")

    slider_ax = plt.axes([0.2, 0.01, 0.65, 0.03])
    slider = Slider(slider_ax, 'Year', min(years), max(
        years), valinit=min(years), valstep=1)

    def update(year):
        # Get top n movies for the current year
        filtered_movies = [movie for movie in movie_list if movie.year == year]
        top_movies = nlargest(n, filtered_movies,
                              key=lambda movie: getattr(movie, field))

        # Update the bar chart
        for bar, movie in zip(bars, top_movies):
            bar.set_height(movie.movie)
            bar.set_width(getattr(movie, field))

        ax.set_title(f'Top {n} Movies by {field.capitalize()} in {year}')

    def on_slider_change(val):
        year = int(val)
        update(year)

    slider.on_changed(on_slider_change)

    plt.show()


def main():
    CSV_FILENAME = "final_dataset.csv"

    try:
        movies_list = deserialize_movies_from_csv(CSV_FILENAME)
    except Exception as e:
        print(f"Hubo un problema al deserializar el CSV: {e}")
        raise e

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
        '11': 'release_date'
    }

    print("Selecciona el campo numérico para ordenar:")
    for key, value in numeric_fields.items():
        print(f"{key}: {value}")

    field_choice = input("Introduce el número del campo que quieres usar: ")
    if field_choice not in numeric_fields:
        print("Opción no válida.")
        return

    n = int(input("¿Cuántas películas quieres ver en el top N? "))

    field_name = numeric_fields[field_choice]

    top_n = nlargest(
        n, movies_list, key=lambda movie: getattr(movie, field_name))

    print(f"Top {n} películas según {field_name}:")
    for movie in top_n:
        if field_name == 'release_date':
            print(f"{movie.movie} - {movie.release_date:%B %d, %Y}")
        else:
            print(f"{movie.movie} ({movie.year}) - {getattr(movie, field_name):,}")

    create_animated_plot(movies_list, n, field_name)


if __name__ == "__main__":
    matplotlib.use('GTK4Agg')
    main()
