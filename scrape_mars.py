from splinter import Browser
from bs4 import BeautifulSoup as bs
import time
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": ChromeDriverManager().install()}

    return Browser("chrome", **executable_path, headless=False)


def scrape_info():
    browser = init_browser()

    # Visit visitcostarica.herokuapp.com
    url = "https://mars.nasa.gov/news/"
    browser.visit(url)

    time.sleep(1)

    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")

    # Get the average temps
    slide_elem = soup.select_one("ul.item_list li.slide")
    news_title = slide_elem.find("div", class_="content_title").get_text()
    news_p = slide_elem.find("div", class_="article_teaser_body").get_text()


  

    # BONUS: Find the src for the sloth image
    relative_image_path = soup.find('div', class_= "list_image").find("img")["src"]

    mars_img = "https://mars.nasa.gov" + relative_image_path

    def get_data():
        df = pd.read_html('http://space-facts.com/mars/')[0] 
        df.columns = ['Description', 'Mars']
        df.set_index('Description', inplace=True)
        return df.to_html(classes="table table-striped")

    # to get the urls
    def featured_image(browser):
        url = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html'
        browser.visit(url)
        full_image_elem = browser.find_by_tag('button')[1]
        full_image_elem.click()
        html = browser.html
        img_soup = soup(html, 'html.parser')
        img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
        img_url = f'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/{img_url_rel[0]}'
        browser.quit()
        return img_url

    def hemisphere_images(browser):
        url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
        browser.visit(url)
        html = browser.html
        img_soup = soup(html, 'html.parser')
        img_url_rel = img_soup.find('collapsible results').find("item")
        relative_image_path = img_url_rel.find_all('div', class_= "item").find("img")["src"]
       # image_urls=f'https://astrogeology.usgs.gov/{img_url_rel}'
        image_urls=relative_image_path
        browser.quit()
        return image_urls

    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'

    browser.visit(url)
    #time.sleep(1)
    browser.visit(url)
    browser.quit()
    image_url1 = 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg'
    image_url2 = 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg'
    image_url3 = 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg'
    image_url4 = 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg'




            

    # Store data in a dictionary
    mars_data = {
        "mars_img": mars_img,
        "news_title": news_title,
        "news_p": news_p,
        "mars_facts":get_data(),
        "image_url1":image_url1,
        "image_url2":image_url2,
        "image_url3":image_url3,
        "image_url4":image_url4
        

    }

    # Close the browser after scraping
    

    
    browser.quit()

    

    # Return results
    return mars_data
