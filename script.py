import pandas as pd
from lxml import html
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def search_multi(asin_list):
    opts = Options()
    opts.headless = True
    driver = webdriver.Chrome(executable_path=r'C:/Users/DavideLonigro/Box/Notebooks/_input/chromedriver.exe',options=opts)
    result = list()
    try:
        for asin in asin_list:
            # print(asin) # <-- print out check
            driver.get("http://www.amazon.fr/dp/"+asin)
            av = driver.find_element_by_css_selector("#availability > span").text
            title = driver.find_element_by_css_selector("#productTitle").text
            result.append([asin,av,title])
            driver.back()
    except:
        print('whoopsie some ASIN is not available: '+asin)
        
    driver.close()
    return result

coffee = 'input/coffee.txt'
mg = 'input/mg.txt'
mcc = 'input/mcc.txt'

coffee_data = open(coffee,'r')
mg_data = open(mg,'r')
mcc_data = open(mcc,'r')

coffee_asin_list = coffee_data.read().split('\n')
mg_asin_list = mg_data.read().split('\n')
mcc_asin_list = mcc_data.read().split('\n')

coffee_data.close()
mg_data.close()
mcc_data.close()

input_date = str(input('please insert date ddmmyy: '))

coffee_lst = search_multi(coffee_asin_list)
mg_lst = search_multi(mg_asin_list)
mcc_lst = search_multi(mcc_asin_list)

df_coffee = pd.DataFrame(coffee_lst, columns=['ASIN','STATUS','NAME'])
df_mg = pd.DataFrame(mg_lst, columns=['ASIN','STATUS','NAME'])
df_mcc = pd.DataFrame(mcc_lst, columns=['ASIN','STATUS','NAME'])

df_coffee.to_excel('coffee_'+input_date+'.xlsx')
df_mg.to_excel('mg_'+input_date+'.xlsx')
df_mcc.to_excel('mcc_'+input_date+'.xlsx')