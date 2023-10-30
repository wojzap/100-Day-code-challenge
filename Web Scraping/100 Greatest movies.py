from bs4 import BeautifulSoup
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
data = response.text

soup = BeautifulSoup(data, "html.parser")
movies_data = soup.find_all(name="h3", class_="title")

movies = [movie.getText() for movie in movies_data]
movies.reverse()
print(movies)

with open("movies.txt", "w", encoding="utf-8") as file:

    for movie in movies:
        file.write(movie + "\n")