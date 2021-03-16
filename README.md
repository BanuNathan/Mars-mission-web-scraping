#                                                                    
                                 <img src= "https://github.com/BanuNathan/web-scraping-challenge/blob/master/website.png">
# Mars Mission 
## Built a web application that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page.

### URLs visited :
#### https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest
####               https://space-facts.com/mars/
####               https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars
#
### Used MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped from the URLs above.

### Started by converting the Jupyter notebook into a Python script called scrape_mars.py with a function called scrape that will execute all of the  
### scraping code from above and return one Python dictionary containing all of the scraped data.

### Next, created a route called /scrape that will import the scrape_mars.py script and call the scrape function.

### Stored the return value in Mongo as mars_mongo database as a Python dictionary.
### Create a root route / that will query the Mongo database and pass the mars data into an HTML template to display the data.

### Created a template HTML file called index.html that will take the mars data dictionary and display all of the data in the appropriate HTML elements. The final website will look as belownn

