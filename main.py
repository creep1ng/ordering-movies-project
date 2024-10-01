from src.movie import Movie
from src.parse_csv import parse_csv

if __name__ == "__main__":
    csv_filename = "final_dataset.csv"
    movies_list = deserialize_movies_from_csv(csv_filename)

    # Output the first movie's details to verify it's correctly deserialized
    # Using __dict__ to print the attributes of a Movie instance
    print(movies_list[0].__dict__)
