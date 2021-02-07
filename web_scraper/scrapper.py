import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Coffee"


def serve_some_soup():
    response = requests.get(url)
    content = response.content
    soup = BeautifulSoup(content, 'html.parser')
    return soup

def get_citations_needed_count(url):
    soup = serve_some_soup()
    result = soup.find_all(title="Wikipedia:Citation needed")
    total_citations_needed = len(result)

    print("total: ", total_citations_needed)
    return total_citations_needed

get_citations_needed_count(url)

def get_citations_needed_report(url):
    str_of_results = ""
    soup = serve_some_soup()
    result = soup.find_all('sup', class_='noprint Inline-Template Template-Fact')
    previous = None
    # print(dir(soup))

    for i in result:
        p = i.find_parent('p')
        str_of_results += p.text.strip()#, '\n' *3
        str_of_results += '\n'*3

    
    print(str_of_results)
    return str_of_results

get_citations_needed_report(url)