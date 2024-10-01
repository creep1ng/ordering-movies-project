from movie import Movie
from parse_csv import deserialize_movies_from_csv

if __name__ == "__main__":
    csv_filename = "final_dataset.csv"
    movies_list = deserialize_movies_from_csv(csv_filename)

    # Output the first movie's details to verify it's correctly deserialized
    # Using __dict__ to print the attributes of a Movie instance
    print(movies_list[0].__dict__)
    print(movies_list[0].year)
