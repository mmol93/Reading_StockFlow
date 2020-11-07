import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


## 미국 선물 지수 얻기 위한 파일임 - ok

def indexOfFuture():
    options = webdriver.ChromeOptions()
    options.add_argument("headless")
    options.add_argument("disable-gpu")

    # 구글에 접속
    driver = webdriver.Chrome("C:/selenium/chromedriver", options=options)
    url = "https://kr.investing.com/indices/indices-futures"
    driver.get(url)
    time.sleep(2)

    name_list = []

    # 지수 이름 가져오기
    for i in range(1, 4):
        name_xpath = "//*[@id='cross_rates_container']/table/tbody/tr[" + str(i) + "]/td[2]"
        name_element = WebDriverWait(driver, 12). \
        until(EC.presence_of_all_elements_located((By.XPATH, name_xpath)))

        name_list.append(name_element[0].text)

    change_list = []
    # 지수 변동율 가져오기
    for i in range(1, 4):
        change_xpath = "//*[@id='cross_rates_container']/table/tbody/tr[" + str(i) + "]/td[8]"
        change_element = WebDriverWait(driver, 12). \
        until(EC.presence_of_all_elements_located((By.XPATH, change_xpath)))

        change_list.append(change_element[0].text)

    show_list = []

    for i in range(0, 3):
        show_list.insert(0, "(선물)" + name_list[i])
        show_list.insert(1, change_list[i])
        print(show_list)    # 선물 지수 리스트 출력(다우, S&P, 나스닥)
        show_list.clear()
