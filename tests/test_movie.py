from src.movie import Movie
from datetime import date

# Create some sample Movie objects
movie1 = Movie(
    movie="Movie 1", year=2000, production_budget=1000000, domestic_gross=500000, foreign_gross=600000,
    worldwide_gross=1100000, month=6, profit=100000, profit_margin=0.1, roi=1.0, pct_foreign=0.54,
    match_key="2000 Movie 1", popularity=75.0, release_date=date(2000, 6, 15), original_language="en",
    vote_average=7.0, vote_count=1000, genre_list=["Action", "Comedy"], genres="Action,Comedy",
    action=True, adventure=False, animation=False, comedy=True, crime=False, documentary=False, drama=False,
    family=False, fantasy=False, history=False, horror=False, music=False, mystery=False, romance=False,
    science_fiction=False, tv_movie=False, thriller=False, war=False, western=False
)

movie2 = Movie(
    movie="Movie 2", year=2010, production_budget=2000000, domestic_gross=400000, foreign_gross=700000,
    worldwide_gross=1100000, month=7, profit=200000, profit_margin=0.15, roi=1.2, pct_foreign=0.6,
    match_key="2010 Movie 2", popularity=80.0, release_date=date(2010, 7, 20), original_language="en",
    vote_average=6.8, vote_count=500, genre_list=["Drama", "Comedy"], genres="Drama,Comedy",
    action=False, adventure=False, animation=False, comedy=True, crime=False, documentary=False, drama=True,
    family=False, fantasy=False, history=False, horror=False, music=False, mystery=False, romance=False,
    science_fiction=False, tv_movie=False, thriller=False, war=False, western=False
)

movie3 = Movie(
    movie="Another Movie 1", year=2000, production_budget=1500000, domestic_gross=700000, foreign_gross=800000,
    worldwide_gross=1500000, month=8, profit=500000, profit_margin=0.2, roi=1.3, pct_foreign=0.55,
    match_key="2000 Another Movie 1", popularity=60.0, release_date=date(2000, 8, 10), original_language="en",
    vote_average=7.5, vote_count=800, genre_list=["Romance", "Drama"], genres="Romance,Drama",
    action=False, adventure=False, animation=False, comedy=False, crime=False, documentary=False, drama=True,
    family=False, fantasy=False, history=False, horror=False, music=False, mystery=False, romance=True,
    science_fiction=False, tv_movie=False, thriller=False, war=False, western=False
)

# Test __eq__ method


def test_movie_equality():
    # movie1 and movie3 have the same year, so they should be equal
    assert movie1 == movie3

    # movie1 and movie2 have different years, so they should not be equal
    assert movie1 != movie2

# Test __lt__ method


def test_movie_less_than():
    # movie2 is newer than movie1, so movie1 should be 'less than' movie2 as per the comparison logic
    assert movie1 < movie2

    # But movie2 should **not** be 'less than' movie1
    assert not movie2 < movie1

# Test __le__ method


def test_movie_less_than_or_equal():
    # movie1 and movie3 have the same year, so movie1 should be 'less than or equal to' movie3
    assert movie1 <= movie3

    # movie1 should also be 'less than or equal to' movie2
    assert movie1 <= movie2

    # movie2 is newer than movie1, so it should **not** be 'less than or equal' to movie1
    assert not movie2 <= movie1
