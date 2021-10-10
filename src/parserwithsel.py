import requests 
import time 
from selenium import webdriver 
from bs4 import BeautifulSoup 
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"}
def get_datar(name):
    url="https://coinmarketcap.com/currencies/"+name+"/news/"
    options=webdriver.ChromeOptions()
    options.set_capability("general.useragent.override",headers)
    options.add_argument('headless')
    options.add_argument('window-size=1200x600')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    try: 
        driver=webdriver.Chrome(
            executable_path=r"C:\Users\Acer\Desktop\pp\chromedriver.exe",
            options=options
        )
        driver.get(url=url)
        time.sleep(5)
        soup=BeautifulSoup(driver.page_source,'lxml')
        print("                                      ===================LAST NEWS======================                    ")
        for title in soup.find_all('a' ,class_='svowul-0 jMBbOf cmc-link'):
            print("Title:")
            print(title.h3.text)
            if 'https' in title.get('href'):
                p=requests.get(title.get('href'),headers=headers).text
                ss=BeautifulSoup(p,'lxml')
            else:
                p=requests.get('https://coinmarketcap.com'+title.get('href'),headers=headers).text
                ss=BeautifulSoup(p,'lxml')
            for para in ss.find_all('p',class_=None):
                print(para.text)
            print("==================================================================================================")
    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()



