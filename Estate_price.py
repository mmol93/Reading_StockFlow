import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

## 미국 주택가격 지수 얻기 위한 파일임 - ok

def estate_price():
    options = webdriver.ChromeOptions()
    options.add_argument("headless")
    options.add_argument("disable-gpu")

    # 구글에 접속
    driver = webdriver.Chrome("C:/selenium/chromedriver", options=options)
    url = "https://kr.investing.com/economic-calendar/monthly-home-price-index-1287"
    driver.get(url)
    time.sleep(2)

    # 그래프에서 자료 3개만 가져오기
    for i in range(1, 3):
        name_xpath = "//*[@id='cross_rates_container']/table/tbody/tr[" + str(i) + "]/td[2]"
        name_element = WebDriverWait(driver, 12). \
        until(EC.presence_of_all_elements_located((By.XPATH, name_xpath)))

        name_list.append(name_element[0].text)
