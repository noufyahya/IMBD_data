# putting the data in a excel sheet
# using dataframes & pandas & BeautifulSoup

import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv

output = requests.get(
    'https://www.imdb.com/search/title/?title_type=feature&year=1950-01-01,2020-12-31').text
soup = BeautifulSoup(output, 'lxml')
movies = soup.find_all('div', class_='lister-item mode-advanced')

f = csv.writer(open("imbd.csv", "w"))
# Write column headers as the first line
f.writerow(["Movie-Name", "Rating", "Director"])


# the code
for movie in movies:
    movie_name = movie.find(
        'h3', class_='lister-item-header').a.text.replace('\n', ' ').strip()
    url = movie.a['href']
    movie_stars = movie.find('div', class_='ratings-bar').div.text.strip()
    _all = movie.find('div', class_='lister-item-content')
    director = _all.find('p', class_="").text.replace(
        '\n', '').replace('|    ', ', ').strip()
    f.writerow([movie_name, movie_stars, director])
