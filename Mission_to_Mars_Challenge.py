# Import Splinter, Beautiful Soup, Pandas and Requests
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import requests

# Set the executable path and initialize Splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)

# Visit the mars nasa news site
url = 'https://redplanetscience.com/'
browser.visit(url)

# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)

# Convert the browser html to a soup object and then quit the browser
html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('div.list_text')

slide_elem.find('div', class_='content_title')

# Use the parent element to find the first a tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title

# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p

# ### Featured Images

# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)

# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()

# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')
img_soup


# find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel

# Use the base url to create an absolute url
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.head()

df.columns=['Description', 'Mars', 'Earth']
df.set_index('Description', inplace=True)
df

df.to_html()


# 1. Use browser to visit the URL 
url = 'https://marshemispheres.com/'
browser.visit(url)

# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')

# Results are returned as an iterable list
results = img_soup.find_all('div', class_='collapsible results')
titles = []
images = []

hemispheres = results[0].find_all('h3')
titles = results[0]('h3')
titles

hemispheres_images = results[0].find_all('img', class_='thumb')
images = results[0]('img', class_='thumb')
images

# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []

titles
images

mars_zip = zip(titles, images)

for title, image in mars_zip:
    mars_dict = {}
    mars_dict['title'] = title
    mars_dict['image'] = image
    hemisphere_image_urls.append(mars_dict)
   
# 3. Write code to retrieve the image urls and titles for each hemisphere.
hemisphere_image_urls

# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls

# 5. Quit the browser
browser.quit()
