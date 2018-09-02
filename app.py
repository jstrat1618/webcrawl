import requests
import bs4

def print_greeting():
    print("---------------------------------------")
    print("Hello From Main")
    print("---------------------------------------")



#Visit Site
def parse_html(url):
    response = requests.get(url)
    html_content = response.text

    soup = bs4.BeautifulSoup(html_content, 'html.parser')

    return soup

#Parse HTML
def extract_a_tags(soup):
    links = soup.find_all('a')

    return links['href']

def extract_link_tags(soup):
    links = soup.find_all('link')

    return links


# soup = bs4.BeautifulSoup(html_content, 'lxml')

#Extract Links

#Store Links

def main():
    print_greeting()

    myurl = 'http://justinstrate.com'

    mysoup = parse_html(myurl)

    links = extract_a_tags(mysoup)

    #links = extract_link_tags(mysoup)

    print(links)
    print(type(links))










if __name__ == '__main__':
    main()
