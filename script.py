from lxml import html, etree
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def search_status(asin):
    opts = Options()
    opts.headless = True
    driver = webdriver.Chrome(executable_path=r'C:/Users/DavideLonigro/Box/Notebooks/_input/chromedriver.exe',options=opts)
    driver.get("http://www.amazon.fr/dp/"+asin)
    content = driver.page_source
    doc = html.fromstring(content)
    search = driver.find_element_by_css_selector("#availability > span")
    result = search.text
    driver.close()
    return print(asin+' '+result)

asin = str(input("Please enter ASIN: "))

search_status(asin)

# asin_list = ['B074M76Z25','B07FTWZ531']
# for asin in asin_list:
#     search_status(asin)