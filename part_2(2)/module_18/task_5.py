import requests
from bs4 import BeautifulSoup


def find_and_get_subheadings(url_link):
    response = requests.get(url_link)
    b_soup = BeautifulSoup(response.content, 'html.parser')
    subheadings_list = [heading.text.strip() for heading in b_soup.find_all('h3')]

    return subheadings_list


url = 'http://www.columbia.edu/~fdc/sample.html'
result = find_and_get_subheadings(url)

print(result)
