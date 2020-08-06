import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

opts = Options()
opts.headless = False
opts.add_argument = "--no-sandbox"
opts.add_argument = "enable-automation"
opts.add_argument = "--disable-dev-shm-usage"
opts.add_argument = "start-maximized"
opts.add_argument = "--disable-infobars"
opts.add_argument = "--disable-gpu"
opts.add_argument = "--disable-browser-side-navigation"

class FindResults():
    
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=r'C:/Users/DavideLonigro/Box/Notebooks/_input/chromedriver.exe',options=opts)

    def read_path(self,path):
        data = open(path,'r')
        asin_list = data.read().split('\n')
        data.close()
        return asin_list
    
    def search_multi(self,path,path_out):
        result = list()
        for asin in self.read_path(path):
            self.driver.get("https://www.amazon.it/dp/"+asin)
            try:
                # self.driver.implicitly_wait(2)
                av = self.driver.find_element_by_css_selector("#availability > span").text
                title = self.driver.find_element_by_css_selector("#productTitle").text
                result.append([asin,av,title])
                self.driver.back()
            except Exception:
                pass
                result.append([asin,'N/A','N/A'])
                df = pd.DataFrame(result, columns=['ASIN','STATUS','NAME'])
            
        self.driver.close()
        
        df = pd.DataFrame(result, columns=['ASIN','STATUS','NAME'])
        
        return df.to_excel(path_out)
    
fres = FindResults()

fres.search_multi('input/italy_2K.txt','output/italy-2000.xlsx')
# fres.search_multi('input/usa_test.txt','output/test.xlsx')