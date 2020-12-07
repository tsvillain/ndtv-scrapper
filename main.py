from bs4 import BeautifulSoup
import requests
import csv
from config import URL, OP_DEST


def scrap_data():
    html_page = requests.get(URL).text
    soup = BeautifulSoup(html_page, 'lxml')
    outer_container = soup.find('div', class_='new_storylising')
    list_of_article = outer_container.find_all('li')

    with open(OP_DEST, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Index', 'Image URL', 'Title', 'Description', 'URL', 'Publication Details'])

        for index, article in enumerate(list_of_article):
            if article.find('div', class_='new_storylising_img'):
                img_url = article.find('div', class_='new_storylising_img').img['src']
                content_container = article.find('div', class_='new_storylising_contentwrap')
                headline = content_container.h2.a.text.strip()
                article_url = content_container.h2.a['href']
                publishing_data = content_container.find('div', class_='nstory_dateline').text.strip()
                desc = content_container.find('div', class_='nstory_intro').text.strip()
                writer.writerow([index, img_url, headline, desc, article_url, publishing_data])

    print("Data Scrapped")


if __name__ == '__main__':
    scrap_data()
