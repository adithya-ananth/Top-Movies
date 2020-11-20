from bs4 import BeautifulSoup as bs
import requests

r = requests.get('https://www.imdb.com/chart/moviemeter/?sort=ir,desc&mode=simple&page=1')
soup = bs(r.content, features = 'html.parser')

table = soup.find("table")
list_of_movies = table.find("tbody")
movies = list_of_movies.find_all("tr")

count = 0
for movie in movies:
    count += 1
    
    name = movie.find(class_ = "titleColumn")
    rating = movie.find(class_ = "ratingColumn imdbRating")
                        
    print("Movie:", name.find("a").text)
    print("Rating:", rating.text[1:])

    if count == 10:
        break
    
