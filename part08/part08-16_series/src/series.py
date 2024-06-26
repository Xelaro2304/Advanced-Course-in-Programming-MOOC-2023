# Write your solution here:
class Series:

    def __init__(self, title: str, seasons: int, genres:list):
        self.title = title
        self.seasons = f'({seasons} seasons)'
        self.genres = ', '.join(genres)
        self.ratings = []

    def __str__(self):

        if self.ratings == []:
            return f'{self.title} {self.seasons}\ngenres: {self.genres}\nno ratings'
        else:
            average = sum(self.ratings)/len(self.ratings)
            return f'{self.title} {self.seasons}\ngenres: {self.genres}\n{len(self.ratings)} ratings, average {average:.1f} points'
        
    def rate(self, rating: int):
        self.ratings.append(rating)

def minimum_grade(rating: float, series_list: list):
    match = []
    for series in series_list:
        average = sum(series.ratings)/len(series.ratings)
        if average >= rating:
            match.append(series)
    return match

def includes_genre(genre: str, series_list: list):
    match = []
    for series in series_list:
        if genre in series.genres:
            match.append(series)
    return match

