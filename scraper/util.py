import bs4
from urllib.request import urlopen

def get_soup(url):
    page = urlopen(url)				# get page to soupify
    soup = bs4.BeautifulSoup(page, "html.parser")
    return soup