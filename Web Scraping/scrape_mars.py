#import dependencies
from bs4 import BeautifulSoup as bs
import pandas as pd
from splinter import Browser
import re
import pymongo
from time import sleep
def scrape():

    #Create path for chromedriver, execute splinter Browser function.
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)

    #Declare url variable for Mars news, visit with Browser function
    url = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
    browser.visit(url)
    sleep(2)

    #Find latest mars news headline and teaser
    html = browser.html
    soup = bs(html, 'html.parser')
    news_title = soup.find("div", class_="content_title").find("a").text
    news_p = soup.find("div", class_="article_teaser_body").text

    #Find latest image
    url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(url)
    sleep(2)
    browser.click_link_by_id('full_image')
    sleep(2)
    html = browser.html
    soup = bs(html, 'html.parser')
    raw_image = soup.find("img", class_= "fancybox-image")['src']
    featured_image_url = "https://www.jpl.nasa.gov/" + raw_image

    #Find weather tweet that starts with "SOL"
    url = "https://twitter.com/marswxreport?lang=en" 
    browser.visit(url)
    sleep(2)
    html= browser.html
    soup = bs(html, "html.parser")
    tweet_list = soup.find_all("li", class_="stream-item")
    for tweet in tweet_list:
        mars_weather = tweet.find("div").find("p").text
        if re.match("SOL ",mars_weather):
            break
        else:
            pass

    #Pull mars facts to pandas table then export html version
    url = "https://space-facts.com/mars/"
    browser.visit(url)
    sleep(2)
    html = browser.html
    soup = bs(html, "html.parser")

    tables = pd.read_html("https://space-facts.com/mars/")
    sleep(2)
    mars_table = tables[0]
    html_table = mars_table.to_html(header=False, index=False)

    #pull hemisphere images
    url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    hemisphere_image_urls = [
        {"title": "Valles Marineris Hemisphere", "img_url": ""},
        {"title": "Cerberus Hemisphere", "img_url": ""},
        {"title": "Schiaparelli Hemisphere", "img_url": ""},
        {"title": "Syrtis Major Hemisphere", "img_url": ""},
    ]
    for i in range(len(hemisphere_image_urls)):
        browser.visit(url)
        sleep(2)
        name = hemisphere_image_urls[i]["title"]
        browser.click_link_by_partial_text(name)
        sleep(2)
        html = browser.html
        sleep(2)
        soup = bs(html,"html.parser")
        img = soup.find_all('li')[-4]
        hemisphere_image_urls[i]["img_url"] = img.find('a')['href']
   

    mars_data = {"news_title" : news_title, "news_p": news_p, "image" : featured_image_url, "weather" : mars_weather, "facts" : html_table, "hemispheres" : hemisphere_image_urls}
    return mars_data