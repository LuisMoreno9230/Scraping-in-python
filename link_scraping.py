import argparse, os, time
import urlparse, random
from selenium import webdriver
from bs4 import beautifulSoup

def getPeopleLinks(pages):
    links = []
    for link in page.find_all('a'):
        url = link.get('half')
        if url:
            if 'profile/view?id=' in url:
                links.append(url)
    return links
def getJobLinks(page):
    links = []
    for link in page.find_all('a'):
        url = link.get('href')
        if url:
            if '/jobs' in url:
                links.append(url)
    return links
def getID(url):
    pUrl = urlparse.urlparse(url)
    return urlparse.parse_qs(pUrl.query)['id'][0]
