from datetime import date
from dataclasses import dataclass


@dataclass(eq=False)
class Movie:
    movie: str
    year: int
    production_budget: float
    domestic_gross: float
    foreign_gross: float
    worldwide_gross: float
    month: int
    profit: float
    profit_margin: float
    roi: float
    pct_foreign: float
    match_key: str
    popularity: float
    release_date: date
    original_language: str
    vote_average: float
    vote_count: int
    genre_list: list[str]
    genres: str
    action: bool
    adventure: bool
    animation: bool
    comedy: bool
    crime: bool
    documentary: bool
    drama: bool
    family: bool
    fantasy: bool
    history: bool
    horror: bool
    music: bool
    mystery: bool
    romance: bool
    science_fiction: bool
    tv_movie: bool
    thriller: bool
    war: bool
    western: bool

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Movie):
            return self.year == other.year

        return NotImplemented

    def __lt__(self, other: 'Movie') -> bool:
        return self.year < other.year

    def __le__(self, other: 'Movie') -> bool:
        return self.year <= other.year
