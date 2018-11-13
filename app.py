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

    with open(r'url_list.csv', 'a', newline='') as csvfile:
        for link in links:
            fieldnames = ['url', 'visit']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({'url': link, 'visit': 'no'})




def record_transaction(sites):
    with open('url_list.csv', 'w') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["url", "visit"])
        for row in sites:
            writer.writerows([[row.url, row.visit]])


def main_loop(websites):
    counter = 1
    max_count = 200

    stored_links = [site.url for site in websites]

    parsed_sites = []
    new_urls = []

    for website in websites:
        print(website.visit)
        if website.visit == "no":
            print("Hello There {}".format(website.visit))
            mysoup = sp.parse_html(website.url)
            parsed_sites.append(website.url)

            website._replace(visit = "yes")

            links = sp.extract_links(mysoup)
            new_links = [_ for _ in links if _ not in stored_links]

            new_urls = new_urls + new_links

            counter += 1

            if counter > max_count:
                break


    all_sites = parsed_sites + new_urls

    new_sites = [Website(site, "yes" if site in parsed_sites else "no") for site in all_sites]

    record_transaction(new_sites)


def main():
    print_greeting()

    stored_links = get_links()

    sites = list(zip(stored_links["url"], stored_links["visit"]))

    websites = [Website(url=u[0], visit=u[1]) for u in sites]

    main_loop(websites)



if __name__ == '__main__':
    main()
