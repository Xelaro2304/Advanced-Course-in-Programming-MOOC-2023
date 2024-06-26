# Write your solution here
# Remember the import statement
from datetime import date

def list_years(dates: list):
    year_list = []
    for i in dates:
        year_list.append(i.year)
    year_list.sort()
    return year_list
