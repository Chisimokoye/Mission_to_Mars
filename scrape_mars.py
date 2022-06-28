from splinter import Browser
from bs4 import BeautifulSoup as bs
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import pandas as pd 



def init_browser():
	executable_path = {"executable_path": ChromeDriverManager().install()}
	return Browser('chrome', **executable_path, headless=False)
	
def scrape():
	browser = init_browser()
	data = {}
	mars_news_url = "https://redplanetscience.com/"
	browser.visit(mars_news_url)

	html = browser.html
	soup = bs(html, "html.parser")
	
	title_mars = soup.find('div', class_='content_title').get_text()
	Mars_para = soup.find('div', class_='article_teaser_body').get_text()
	


	feat_url = "https://spaceimages-mars.com"
	browser.visit(feat_url)
	html = browser.html
	img_soup = bs(html, "html.parser")

	img_url_rel = img_soup.find('img').get('src')
	img_url = f'https://spaceimages-mars.com/{img_url_rel}'
		

	mars_facts_url = "https://galaxyfacts-mars.com/"
	mars_facts = pd.read_html(mars_facts_url)
	mars_facts_df = mars_facts[0]
	mars_facts_df.columns = ['Details', 'Mars', 'Earth']
	mars_facts_df = mars_facts_df.transpose()
	
	
	
	
	mars_hemi_url = 'https://marshemispheres.com/'
	browser.visit(mars_hemi_url)
	
	links = browser.find_by_css("a.product-item img")
	for item in range(len(links)):
		hemisphere = {}
		browser.find_by_css("a.product-item img")[item].click()
		sample_element = browser.find_link_by_text("Sample").first
		hemisphere["img_url"] = sample_element["href"]
		hemisphere["title"] = browser.find_by_css("h2.title").text
		hemisphere_image_urls.append(hemisphere)


	data = {"Mars Title": title_mars,
	"Mars_para": Mars_para,
	"img_url": img_url,
	"mars_facts_df": mars_facts_df.to_html(),
	"hemisphere_image_urls": hemisphere_image_urls}
	
	browser.quit()
	print(scrape)
	return data
