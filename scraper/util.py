import bs4
import html5lib
from urllib.request import urlopen

def get_soup(url):
    page = urlopen(url)				# get page to soupify
    soup = bs4.BeautifulSoup(page, "html5lib")
    return soup