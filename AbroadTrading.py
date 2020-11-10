import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

## 한국 경상수지 지수 얻기 위한 파일임 - ok

def tradingGraph():
    options = webdriver.ChromeOptions()
    options.add_argument("headless")
    options.add_argument("disable-gpu")

    # 구글에 접속
    driver = webdriver.Chrome("C:/selenium/chromedriver", options=options)
    url = "https://kr.investing.com/economic-calendar/south-korean-current-account-789"
    driver.get(url)
    time.sleep(2)

    # 그래프에서 자료 4개만 가져오기 (다른 파이썬 파일이랑 가져오는 방법 다름)

    # 날짜 데이터 가져오기 - ok
    date_list = []
    for i in range(0, 7, 2):    # 2개씩 띄워서 가져오기(0, 2, 4, 6)
        date_element1 = WebDriverWait(driver, 12). \
        until(EC.presence_of_all_elements_located((By.XPATH, "//*[@id='eventTabDiv_history_0']")))

        date_element2 = date_element1[0].find_element_by_tag_name("tbody")
        date_element3 = date_element2.find_elements_by_class_name("left")
        date_list.append(date_element3[i].text)

    # 발표 데이터 가져오기 - ok
    PT_list = []
    for i in range(0, 13, 3):  # 3개씩 띄워서 가져오기
        PT_element1 = WebDriverWait(driver, 12). \
            until(EC.presence_of_all_elements_located((By.XPATH, "//*[@id='eventTabDiv_history_0']")))

        PT_element2 = PT_element1[0].find_element_by_tag_name("tbody")
        PT_element3 = PT_element2.find_elements_by_class_name("noWrap")
        PT_list.append(PT_element3[i].text)

    result_list = []

    result_list.append("한국 경상수지 지수: ")
    result_list.append(date_list[1])    # 직전 날짜

    # 직전 발표 데이터들(4개 -> 3개로 변경함 - 20.11.10) - ok
    for i in range(1, 4):
        if PT_list[i] == " ":
            result_list.append("아직 자료없음")
        else:
            result_list.append(PT_list[i])

    result_list.append(driver.current_url)

    print(result_list)

    driver.close()

