from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")

yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")


articles = soup.find_all(name="span", class_="titleline")

scores = soup.find_all(name="span", class_="score")

article_texts = []
article_links = []
article_scores = []

for article in articles:
    article_tag = article.find(name="a")
    article_text = article_tag.getText()
    article_link = article_tag.get("href")
    article_texts.append(article_text)
    article_links.append(article_link)

for score in scores:
    value = int(score.getText().split()[0])
    article_scores.append(value)

index_of_highest_score = article_scores.index(max(article_scores))
print(article_texts[index_of_highest_score])
print(article_links[index_of_highest_score])