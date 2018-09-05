import requests
import bs4
import os
import csv


def print_greeting():
    print("---------------------------------------")
    print("Hello From Main")
    print("---------------------------------------")


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

def get_links():
    #check link isn't already stored

    file = os.path.abspath("url_list.csv")

    url = []
    visit = []

    with open(file, 'r') as my_file:
        reader = csv.DictReader(my_file)
        for line in reader:
            url.append(line['url'])
            visit.append(line['visit'])

    my_dict = {"url":url, "visit":visit}

    return my_dict




def main():
    print_greeting()

    #Visit site

    myurl = 'http://justinstrate.com'

    #Parse HTML
    #mysoup = parse_html(myurl)

    #links = extract_links(mysoup)

    stored_links = get_links()

    print(stored_links)








if __name__ == '__main__':
    main()
