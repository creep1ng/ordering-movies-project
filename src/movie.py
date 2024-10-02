from datetime import date


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

    def __init__(self, movie: str, year: int, production_budget: float, domestic_gross: int, foreign_gross: int,
                 worldwide_gross: int, month: int, profit: int, profit_margin: float, roi: float, pct_foreign: float,
                 match_key: str, popularity: float, release_date: date, original_language: str, vote_average: float,
                 vote_count: int, genre_list: list[str], genres: str, action: bool, adventure: bool, animation: bool,
                 comedy: bool, crime: bool, documentary: bool, drama: bool, family: bool, fantasy: bool, history: bool,
                 horror: bool, music: bool, mystery: bool, romance: bool, science_fiction: bool, tv_movie: bool,
                 thriller: bool, war: bool, western: bool):
        self.movie = movie
        self.year = year
        self.production_budget = production_budget
        self.domestic_gross = domestic_gross
        self.foreign_gross = foreign_gross
        self.worldwide_gross = worldwide_gross
        self.month = month
        self.profit = profit
        self.profit_margin = profit_margin
        self.roi = roi
        self.pct_foreign = pct_foreign
        self.match_key = match_key
        self.popularity = popularity
        self.release_date = release_date
        self.original_language = original_language
        self.vote_average = vote_average
        self.vote_count = vote_count
        self.genre_list = genre_list
        self.genres = genres
        self.action = action
        self.adventure = adventure
        self.animation = animation
        self.comedy = comedy
        self.crime = crime
        self.documentary = documentary
        self.drama = drama
        self.family = family
        self.fantasy = fantasy
        self.history = history
        self.horror = horror
        self.music = music
        self.mystery = mystery
        self.romance = romance
        self.science_fiction = science_fiction
        self.tv_movie = tv_movie
        self.thriller = thriller
        self.war = war
        self.western = western

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Movie):
            return self.year == other.year

        return NotImplemented

    def __lt__(self, other: 'Movie') -> bool:
        return self.year < other.year

    def __le__(self, other: 'Movie') -> bool:
        return self.year <= other.year
