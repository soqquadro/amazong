import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from datetime import date

today = date.today()
date = today.strftime("%d/%m/%Y")


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
    driver = webdriver.Chrome(executable_path=r'/home/dlonigro/Projects/Amazong/chromedriver',options=opts)
    result = list()
    
    for asin in asin_list:
        # print(asin_list[i],' ',i) # <-- print out check
        driver.get("http://www.amazon.fr/dp/"+asin)
        
        try:
            av = driver.find_element_by_css_selector("#availability > span").text
            title = driver.find_element_by_css_selector("#productTitle").text
            minfo = driver.find_element_by_css_selector("#merchant-info").text
            # price = driver.find_element_by_css_selector("#price_inside_buybox").text
            result.append([date,asin,av,title,minfo]) 
            # result.append([date,asin,av,title,minfo,price])
            # result.append([asin,av,title])
            driver.back()
    
        except Exception:
            pass
            # result.append([asin,'N/A','N/A','N/A'])
            result.append([date,asin,'N/A','N/A','N/A'])
            # result.append([date,asin,'N/A','N/A','N/A','N/A'])
            # result.append([asin_list[i],'n/a','n/a'])
        
    driver.close()
    return result

def run(lst_asin,lst_names):
    result = list()
    out = list()
    
    for l in lst_asin:
        result.append(search_multi(l))
        
    for r in result:
        out.append(pd.DataFrame(r,columns=['DATE','ASIN','STATUS','NAME','INFO']))
        # out.append(pd.DataFrame(r, columns=['DATE','ASIN','STATUS','NAME','INFO','PRICE']))

    for df,n in zip(out,lst_names):
        df.to_excel(n+input_date+'.xlsx')

coffee = 'input/coffee.txt'
mg = 'input/mg.txt'
mcc = 'input/mcc.txt'
other = 'input/others.txt'

coffee_data = open(coffee,'r')
mg_data = open(mg,'r')
mcc_data = open(mcc,'r')
other_data = open(other,'r')

coffee_asin_list = coffee_data.read().split('\n')
mg_asin_list = mg_data.read().split('\n')
mcc_asin_list = mcc_data.read().split('\n')
other_asin_list = other_data.read().split('\n')

coffee_data.close()
mg_data.close()
mcc_data.close()
other_data.close()

lst_input = [
    coffee_asin_list,
    mg_asin_list,
    mcc_asin_list,
#    other_asin_list
]

lst_names = [
    'coffee_',
    'mg_',
    'mcc_',
#    'others_'
]

input_date = str(input('please insert date ddmmyy: '))
    
run(lst_input,lst_names)

# coffee_lst = search_multi(coffee_asin_list)
# mg_lst = search_multi(mg_asin_list)
# mcc_lst = search_multi(mcc_asin_list)

# df_coffee = pd.DataFrame(coffee_lst, columns=['DATE','ASIN','STATUS','NAME','INFO'])
# df_mg = pd.DataFrame(mg_lst, columns=['ASIN','STATUS','NAME'])
# df_mcc = pd.DataFrame(mcc_lst, columns=['ASIN','STATUS','NAME'])

# df_coffee.to_excel('coffee_'+input_date+'.xlsx')
# df_mg.to_excel('mg_'+input_date+'.xlsx')
# df_mcc.to_excel('mcc_'+input_date+'.xlsx')
