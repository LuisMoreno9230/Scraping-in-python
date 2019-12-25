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