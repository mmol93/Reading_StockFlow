import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 미국 3대지수(다우, S&P, 나스닥) 얻음

def three_main_Flow():
    options = webdriver.ChromeOptions()
    options.add_argument("headless")
    options.add_argument("disable-gpu")

    # 구글에 접속
    driver = webdriver.Chrome("C:/selenium/chromedriver", options=options)
    url = "https://kr.investing.com/indices/usa-indices"
    driver.get(url)
    time.sleep(2)

    ## 얻어야할 정보가 많지 않기 때문에 각 지수별로 Xpath를 설정하여 정보를 얻는다
    ## 즉, 변수로 그냥 따로 따로 쓴다

    # S&P 정보 얻기
    SnP_name = driver.find_element_by_xpath('//*[@id="pair_166"]/td[2]').text
    SnP_change = driver.find_element_by_xpath('//*[@id="pair_166"]/td[7]').text

    # 나스닥 정보 얻기
    NasDac_name = driver.find_element_by_xpath('//*[@id="pair_14958"]/td[2]').text
    NasDac_change = driver.find_element_by_xpath('//*[@id="pair_14958"]/td[7]').text

    # 다우 정보 얻기
    Dau_name = driver.find_element_by_xpath('//*[@id="pair_169"]/td[2]').text
    Dau_change = driver.find_element_by_xpath('//*[@id="pair_169"]/td[7]').text

    # 각 지수들 리스트로 묶어서 출력하기
    dau_list = []
    dau_list.append(Dau_name)
    dau_list.append(Dau_change)

    SnP_lsit = []
    SnP_lsit.append(SnP_name)
    SnP_lsit.append(SnP_change)

    NasDac_List = []
    NasDac_List.append(NasDac_name)
    NasDac_List.append(NasDac_change)

    print(dau_list)
    print(SnP_lsit)
    print(NasDac_List)
