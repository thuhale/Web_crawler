import sys
import os
import requests

from bs4 import BeautifulSoup
from bs4 import SoupStrainer
from selenium import webdriver

#Find all category links according to level 1 to 3
def FindCategory(level):
    r = requests.get('http://www.sephora.com/')
    soup = BeautifulSoup(r.text, "html.parser")
    header_html = soup.find_all(attrs={'class': 'Header-nav'})

    soup2 = BeautifulSoup(str(header_html[0]), "html.parser")
    if level==3: linkClass = "Nav-link"
    else: linkClass = "meganav__link"
    links = soup2.findAll('a', linkClass)
    return links

def FindProductsInOneCategory(categoryLink):
    url = 'http://www.sephora.com' + categoryLink['href'] + '?pageSize=-1'
    chromedriver = "/Users/lehathu/Desktop/Web_crawler/chromedriver"
    os.environ["webdriver.chrome.driver"] = chromedriver
    driver = webdriver.Chrome("/Users/lehathu/Desktop/Web_crawler/chromedriver")

    driver.get(url)
    soup = BeautifulSoup(driver.page_source , 'html.parser')
    driver.close()
    productDiv = soup.find_all(attrs={'class': 'search-results'})

    soup2 = BeautifulSoup(str(productDiv[0]), "html.parser")
    productLinks = soup2.findAll('a')
    for link in productLinks:
        print link['href']


def main():
    print 'Sephora website, showing only Meganav_link (1st level category)'
    categoryLinks = FindCategory(3)
    FindProductsInOneCategory(categoryLinks[0])


# this is the standard boilerplate
if __name__ == '__main__':
    main()