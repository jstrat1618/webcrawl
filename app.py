import os
import csv
import collections
import siteparse as sp


Website = collections.namedtuple("Website", "url, visit")

def print_greeting():
    print("---------------------------------------")
    print("Hello From Main")
    print("---------------------------------------")

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

def store_links(links):
    file = os.path.abspath("url_list.csv")


    with open(r'url_list.csv', 'a', newline='') as csvfile:
        for link in links:
            fieldnames = ['url', 'visit']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({'url': link, 'visit': 'no'})


def main():
    print_greeting()

    stored_links = get_links()

    sites = list(zip(stored_links["url"], stored_links["visit"]))

    websites = [Website(url=u[0], visit=u[1]) for u in sites]

    counter = 1
    max_count = 200

    for website in websites:
        if website.visit == "no":
            mysoup = sp.parse_html(website.url)
            links = sp.extract_links(mysoup)

            links2store = [_ for _ in links if _ not in stored_links["url"]]

            store_links(links2store)

            counter += 1

            if counter > max_count:
                break
        print(stored_links)





if __name__ == '__main__':
    main()
