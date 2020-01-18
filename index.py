# --------------------- IMPORTS ---------------------
# main selenium webdrive
from selenium import webdriver

# provides support for keyboard keys e.g. mocking a keypress
from selenium.webdriver.common.keys import Keys

# importing options to make the browser headless i.e. doesn't open a window
# while doing all the scraping / crawling stuff
from selenium.webdriver.chrome.options import Options

# using beautiful soup to parse the page
from bs4 import BeautifulSoup
import os
import re

# importing a function that prints a 2D List in a tabular form
from table import printTable

# importing useful functions made for the main code in this file
from definitions import *

# --------------------- INIT STUFF ---------------------

options = webdriver.ChromeOptions()  # importing for making chrome headless
options.add_argument('headless')   # headless means chrome doesn't pop up
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(30)

# base url to which the query will be attached later on to make the request
# i.e. get the src code
baseURL = 'https://viewdns.info/reversewhois/?'


# --------------------- MAIN PROGRAM ---------------------

def check_name_and_corresponding_url(name, driver):
    name = str(name)

    # using the name get the URL
    url = getURL(baseURL, name)

    # 'requesting' the url
    driver.get(url)

    # soupifying the source code
    soup = BeautifulSoup(driver.page_source, features="html.parser")

    # getting alll the tables from the soup
    tables = soup.findAll('table')

    # checking for errors
    # getting errorObj
    errorObj = checkForErrors(tables)

    return errorObj


def index(driver):
    # get the name of the entity
    name = getEntityName()

    # check if it results in a valid reverse WHOIS lookup result
    errorObj = check_name_and_corresponding_url(name, driver)

    # if it does NOT result in a valid reverse WHOIS lookup result
    # get a new entity name, and while doing that send the error from the previous time
    # check the new entity name just like the previous one was checked
    # keep looping until we get a valid result/response
    while errorObj['errorPresent']:
        name = getEntityName(errorPresent=True, errorMsg=errorObj['errorMsg'])
        errorObj = check_name_and_corresponding_url(name, driver)

    # ---- INPUT VALIDATED ------
    # getting tables.
    # when there is no error, the errorObj is returned with the tablesList
    # that was created during the last 'request'
    tables = errorObj['tables']

    # getting data in the form of 2D List
    data = getTableData(tables)

    # printing the data received above
    printTable(data, 10, 4, headingPresent=True)

    # closing driver
    driver.close()


index(driver)
