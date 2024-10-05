# src/main.py
from parse_csv import deserialize_movies_from_csv
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from movie import Movie
import matplotlib
from heapq import nlargest


def create_animated_plot(movie_list: list[Movie], n: int, field: str):
    years = sorted(set(movie.year for movie in movie_list))

    # Debug: Print available years
    print(f"Available years: {years}")

    fig, ax = plt.subplots(figsize=(10, 6))

    # Filter movies for the first year at start
    current_year = years[0]
    filtered_movies = [
        movie for movie in movie_list if movie.year == current_year]

    # Debug: Print how many movies were found in the current year
    print(f"Movies in {current_year}: {len(filtered_movies)}")

    # Rank the movies by the given field for the initial plot
    top_movies = nlargest(n, filtered_movies,
                          key=lambda movie: getattr(movie, field))

    # Create initial bar chart with the actual number of bars
    bars = ax.barh([movie.movie for movie in top_movies],
                   [getattr(movie, field) for movie in top_movies],
                   color="skyblue")

    ax.set_xlabel(field.capitalize())
    ax.set_title(f"Top {n} películas por {
                 field.capitalize()} in {current_year}")

    # Create a slider control
    slider_ax = plt.axes([0.2, 0.01, 0.65, 0.03])
    slider = Slider(slider_ax, 'Year', valmin=min(years), valmax=max(years),
                    valinit=current_year, valstep=1)

    def update(year):
        """Update the chart when the year changes via the slider"""
        year = int(year)  # Ensure we're working with an integer year

        # Filter movies by selected year
        filtered_movies = [movie for movie in movie_list if movie.year == year]

        # If there are no movies, skip
        if not filtered_movies:
            print(f"No movies found for the year {year}.")
            return

        # Debug: Print count of movies in the current year
        print(f"Year: {year}, Movies found: {len(filtered_movies)}")

        # Get top-n movies sorted by the chosen field
        top_movies = nlargest(n, filtered_movies,
                              key=lambda movie: getattr(movie, field))

        # Clear the previous bars, and initialize new bars for the new data
        ax.clear()  # Clear the axes to avoid artifacts

        # Re-plot the top-n movies for the new year
        bars = ax.barh([movie.movie for movie in top_movies],
                       [getattr(movie, field) for movie in top_movies],
                       color="skyblue")

        ax.set_xlabel(field.capitalize())
        ax.set_title(f"Top {n} Movies by {field.capitalize()} in {year}")

    # Update plot when slider value changes
    def on_slider_change(val):
        update(val)

    # Attach an event listener to the slider
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
    }

    # Ask the user to choose a sorting field
    print("Selecciona el campo numérico para ordenar:")
    for key, value in numeric_fields.items():
        print(f"{key}: {value}")

    field_choice = input("Introduce el número del campo que quieres usar: ")
    if field_choice not in numeric_fields:
        print("Opción no válida.")
        return

    # Ask for number of top movies to display
    n = int(input("¿Cuántas películas quieres ver en el top N? "))

    field_name = numeric_fields[field_choice]

    # Generate and display the animated plot
    create_animated_plot(movies_list, n, field_name)


if __name__ == "__main__":
    matplotlib.use('TkAgg')  # Ensure TkAgg is used for interactive plotting
    main()
