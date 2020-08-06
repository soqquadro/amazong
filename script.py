import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def search_multi(asin_list):
    opts = Options()
    opts.headless = False
    opts.add_argument = "--no-sandbox"
    opts.add_argument = "enable-automation"
    opts.add_argument = "--disable-dev-shm-usage"
    opts.add_argument = "start-maximized"
    opts.add_argument = "--disable-infobars"
    opts.add_argument = "--disable-gpu"
    opts.add_argument = "--disable-browser-side-navigation"
    driver = webdriver.Chrome(executable_path=r'C:/Users/DavideLonigro/Box/Notebooks/_input/chromedriver.exe',options=opts)
    result = list()
    
    for asin in asin_list:
    # for i in range(2000,2500,1):
        # print(asin_list[i],' ',i) # <-- print out check
        driver.get("http://www.amazon.fr/dp/"+asin)
        # driver.get("https://www.amazon.com/dp/"+asin)
        # driver.get("https://www.amazon.de/dp/"+asin)
        # driver.get("https://www.amazon.de/dp/"+asin_list[i])
        try:
            av = driver.find_element_by_css_selector("#availability > span").text
            title = driver.find_element_by_css_selector("#productTitle").text
            result.append([asin,av,title])
            # result.append([asin_list[i],av,title])
            driver.back()
    
        except Exception:
            pass
            result.append([asin,'N/A','N/A'])
            # result.append([asin_list[i],'n/a','n/a'])
            
    # df = pd.DataFrame(result,columns=['ASIN','STATUS','NAME'])
        
    driver.close()
    return result

coffee = 'input/coffee.txt'
mg = 'input/mg.txt'
mcc = 'input/mcc.txt'
# other = 'input/germ.txt'

coffee_data = open(coffee,'r')
mg_data = open(mg,'r')
mcc_data = open(mcc,'r')
# other_data = open(other,'r')

coffee_asin_list = coffee_data.read().split('\n')
mg_asin_list = mg_data.read().split('\n')
mcc_asin_list = mcc_data.read().split('\n')
# other_asin_list = other_data.read().split('\n')

coffee_data.close()
mg_data.close()
mcc_data.close()
# other_data.close()

input_date = str(input('please insert date ddmmyy: '))

coffee_lst = search_multi(coffee_asin_list)
mg_lst = search_multi(mg_asin_list)
mcc_lst = search_multi(mcc_asin_list)
# other_lst = search_multi(other_asin_list)

df_coffee = pd.DataFrame(coffee_lst, columns=['ASIN','STATUS','NAME'])
df_mg = pd.DataFrame(mg_lst, columns=['ASIN','STATUS','NAME'])
df_mcc = pd.DataFrame(mcc_lst, columns=['ASIN','STATUS','NAME'])
# df_other = pd.DataFrame(other_lst,columns=['ASIN','STATUS','NAME'])

df_coffee.to_excel('coffee_'+input_date+'.xlsx')
df_mg.to_excel('mg_'+input_date+'.xlsx')
df_mcc.to_excel('mcc_'+input_date+'.xlsx')
# df_other.to_excel('ger'+input_date+'.xlsx')