# putting the data in a excel sheet
# using dataframes & pandas & BeautifulSoup

import requests
from bs4 import BeautifulSoup as bs
import csv
import numpy as np
import pandas as pd

f = csv.writer(open("imbd3.csv", "w"))
# Write column headers as the first line
f.writerow(["Movie-Title", "Director_stars", "Value"])


# the code
pages = np.arange(1, 1000, 100)
for page in pages:
    page = requests.get(
        "https://www.imdb.com/search/title/?title_type=feature&year=1950-01-01,2020-12-31&start="+str(page)+"&ref_=adv_nxt")
    soup = bs(page.text, 'html.parser')
    movies = soup.find_all('div', class_='lister-item mode-advanced')

    for movie in movies:
        title = movie.find(
            'h3', class_='lister-item-header').a.text.replace('\n', ' ').strip()
        director = movie.find('div', class_='lister-item-content').find('p', class_="").text.replace(
            '\n', '').replace('|    ', ', ').strip()

        f.writerow([title, director])

        #print(f"{movie_title} |{director} |  ")
