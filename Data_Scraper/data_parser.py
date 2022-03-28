from selenium import webdriver
import json
import facebook_functions as fb
from bs4 import BeautifulSoup


def json_to_obj(filename):
    """Extracts data from JSON and turns it """
    obj = None
    with open(filename) as file:
        obj = json.loads(file.read())
    return obj


# Step 1: Receive a List of Facebook Groups to which we will be scraping
facebook_groups = json_to_obj('fb_groups.json')
print(facebook_groups)

# Step 2: Receive credential from a file to make a login using requests package
credentials = json_to_obj('credentials.json')
print(credentials)

# Step 3: Login to FB
driver = fb.init_driver("/Users/santiagomontemayorgomez/Desktop/chromedriver")
fb.go_to_website(driver=driver, website="https://www.facebook.com/")
fb.login_to_fb(driver=driver, credentials=credentials)

# Step