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

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("email", help="linkedin email")
    parser.add_argument("password", help="linkedin password")
    args = parser.parse_args()

    browser = webdriver.Firefox()
    browser.get("https://linkedin.com/uas/login")

    emailElement = browser.find_element_by_id("session_key-login")
    emailElement.send_keys(args.email)
    passElement = browser.find_element_by_id("session_password-login")
    passElement.send_keys(args.password)
    passElement.submit()

    os.system('clear')
    print "[+] Success! Logged In, Bot Starting!"
    ViewBot(browser)
    browser.close()

if __name__ == "__main__":

    main()

    