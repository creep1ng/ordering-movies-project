from movie import Movie
from parse_csv import deserialize_movies_from_csv

if __name__ == "__main__":
    CSV_FILENAME = "final_dataset.csv"
    movies_list = deserialize_movies_from_csv(CSV_FILENAME)

    # Output the first movie's details to verify it's correctly deserialized
    # Using __dict__ to print the attributes of a Movie instance

    a = movies_list[0].year
    b = movies_list[1].year

    print(a)
    print(b)
    print(a > b)
