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

    # 그래프에서 자료 4개만 가져오기 (다른 파이썬 파일이랑 가져오는 방법 다름)

    # 날짜 데이터 가져오기 - ok
    date_list = []
    for i in range(0, 7, 2):    # 2개씩 띄워서 가져오기(0, 2, 4, 6)
        date_element1 = WebDriverWait(driver, 20). \
        until(EC.presence_of_all_elements_located((By.XPATH, "//*[@id='eventTabDiv_history_0']")))

        date_element2 = date_element1[0].find_element_by_tag_name("tbody")
        date_element3 = date_element2.find_elements_by_class_name("left")
        date_list.append(date_element3[i].text)

    # 발표 데이터 가져오기 - ok
    PT_list = []
    for i in range(0, 13, 3):  # 3개씩 띄워서 가져오기
        PT_element1 = WebDriverWait(driver, 20). \
            until(EC.presence_of_all_elements_located((By.XPATH, "//*[@id='eventTabDiv_history_0']")))

        PT_element2 = PT_element1[0].find_element_by_tag_name("tbody")
        PT_element3 = PT_element2.find_elements_by_class_name("noWrap")
        PT_list.append(PT_element3[i].text)

    # PT_lsit의 각 항목 증감율 계산하기
    PT_Result_list = []
    # if PT_list[0] == " ":
    #     PT_Result_list.append("기록 없음")
    # else:
    #     result = (float(PT_list[0]) - float(PT_list[1])) / float(PT_list[1]) * 100
    #     PT_Result_list.append(str(round(result, 2)) + "%")

    for i in range(1, 4):
        result = (float(PT_list[i]) - float(PT_list[i + 1])) / float(PT_list[i + 1]) * 100
        PT_Result_list.append(str(round(result, 2)) + "%")

    result_list = []

    result_list.append("미국 주택가격 지수: ")
    result_list.append(date_list[1])    # 직전 날짜
    result_list.append(PT_list[1])      # 직전 발표
    result_list.append(PT_Result_list)  # 최근 3개 증감율
    result_list.append(driver.current_url)

    print(result_list)

    driver.close()

