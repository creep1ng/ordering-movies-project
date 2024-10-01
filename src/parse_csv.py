from movie import Movie
import csv
from datetime import datetime
from ast import literal_eval


def deserialize_movies_from_csv(csv_filename: str) -> list[Movie]:
    movies = []

    with open(csv_filename, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)

        for row in reader:
            # Convert fields to the correct datatypes:
            try:
                movie = row['movie']
                year = int(row['year'])
                production_budget = float(row['production_budget'])
                domestic_gross = int(row['domestic_gross'])
                foreign_gross = int(row['foreign_gross'])
                worldwide_gross = int(row['worldwide_gross'])
                month = int(row['month'])
                profit = int(row['profit'])
                profit_margin = float(row['profit_margin'])
                roi = float(row['roi'])
                pct_foreign = float(row['pct_foreign'])
                match_key = row['match_key']
                popularity = float(row['popularity'])
                release_date = datetime.strptime(
                    # Parse string -> date
                    row['release_date'], '%Y-%m-%d').date()
                original_language = row['original_language']
                vote_average = float(row['vote_average'])
                vote_count = int(row['vote_count'])
                # Convert string representation of list -> list
                genre_list = literal_eval(row['genre_list'])
                genres = row['genres']

                # Boolean Fields (like Action, Adventure, etc.) are stored as '1' or '0' in the CSV
                action = bool(int(row['Action']))
                adventure = bool(int(row['Adventure']))
                animation = bool(int(row['Animation']))
                comedy = bool(int(row['Comedy']))
                crime = bool(int(row['Crime']))
                documentary = bool(int(row['Documentary']))
                drama = bool(int(row['Drama']))
                family = bool(int(row['Family']))
                fantasy = bool(int(row['Fantasy']))
                history = bool(int(row['History']))
                horror = bool(int(row['Horror']))
                music = bool(int(row['Music']))
                mystery = bool(int(row['Mystery']))
                romance = bool(int(row['Romance']))
                science_fiction = bool(int(row['Science Fiction']))
                tv_movie = bool(int(row['TV Movie']))
                thriller = bool(int(row['Thriller']))
                war = bool(int(row['War']))
                western = bool(int(row['Western']))

                # Create a Movie object and append it to the list
                movie_obj = Movie(
                    movie=movie, year=year, production_budget=production_budget, domestic_gross=domestic_gross,
                    foreign_gross=foreign_gross, worldwide_gross=worldwide_gross, month=month, profit=profit,
                    profit_margin=profit_margin, roi=roi, pct_foreign=pct_foreign, match_key=match_key,
                    popularity=popularity, release_date=release_date, original_language=original_language,
                    vote_average=vote_average, vote_count=vote_count, genre_list=genre_list, genres=genres,
                    action=action, adventure=adventure, animation=animation, comedy=comedy, crime=crime,
                    documentary=documentary, drama=drama, family=family, fantasy=fantasy, history=history,
                    horror=horror, music=music, mystery=mystery, romance=romance, science_fiction=science_fiction,
                    tv_movie=tv_movie, thriller=thriller, war=war, western=western
                )

                movies.append(movie_obj)
            except Exception as e:
                print(f"Error processing row: {row}. Error: {e}")

    return movies
