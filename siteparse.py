import requests
import bs4


def parse_html(url):
    response = requests.get(url)
    html_content = response.text

    soup = bs4.BeautifulSoup(html_content, 'html.parser')

    return soup


def extract_a_tags(soup):
    links = soup.find_all(href=True)

    return links


def extract_links(soup):
    links = soup.find_all('link')

    link_list = [link['href'] for link in links]

    return link_list




