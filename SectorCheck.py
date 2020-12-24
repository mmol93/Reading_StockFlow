import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 증시 흐름 분석 툴

## 미국 주식 섹터별 주요 종목 상황체크
# +1.3% or -1.3%일 때 해당 섹터명 + 종목명을 출력함

options = webdriver.ChromeOptions()
options.add_argument("headless")
options.add_argument("disable-gpu")
driver = webdriver.Chrome("C:/selenium/chromedriver", options=options)

name = []   # 종목명
change = [] # 변동율

selected_index = [] # 기준 1.3 넘는 부분만 뽑아내는 인덱스 - 이를 name과 change에서 재활용함


def sectorCheck():
    options = webdriver.ChromeOptions()
    options.add_argument("headless")
    options.add_argument("disable-gpu")

    ## 테크주 확인 - 마소, 어도비, 오라클
    # 마이크로소프트에 접속
    connectToLink("https://kr.investing.com/equities/microsoft-corp", name, change)

    # 어도비에 접속
    connectToLink("https://kr.investing.com/equities/adobe-sys-inc", name, change)

    # 오라클에 접속
    connectToLink("https://kr.investing.com/equities/oracle-corp", name, change)

    select_stock("테크주: ")

    ## 엔터주 확인 - 디즈니, 넷플릭스
    # 디즈니 접속
    connectToLink("https://kr.investing.com/equities/disney", name, change)

    # 넷플릭스 접속
    connectToLink("https://kr.investing.com/equities/netflix,-inc.", name, change)

    select_stock("엔터주: ")

    ## 인터넷 쇼핑주 확인 - 아마존
    # 아마존 접속
    connectToLink("https://kr.investing.com/equities/amazon-com-inc-earnings", name, change)

    select_stock("인터넷쇼핑주: ")


    ## 경제주 확인 - 비자, 마스터
    # 비자 접속
    connectToLink("https://kr.investing.com/equities/visa-inc", name, change)

    #마스터 접속
    connectToLink("https://kr.investing.com/equities/mastercard-cl-a", name, change)

    select_stock("경제주: ")

    ## 요식업주 확인 - 코카콜라, 맥날, 버거킹
    # 코카콜라 접속
    connectToLink("https://kr.investing.com/equities/coca-cola-co", name, change)

    # 맥도날드 접속
    connectToLink("https://kr.investing.com/equities/mcdonalds", name, change)

    # 버거킹 접속
    connectToLink("https://www.investing.com/equities/restaurant-brands-intrnational", name, change)

    select_stock("요식업주: ")

    ## 인터넷주 - 구글, 페북
    # 구굴 접속
    connectToLink("https://www.investing.com/equities/google-inc", name, change)

    # 페북 접속
    connectToLink("https://kr.investing.com/equities/facebook-inc", name, change)

    select_stock("인터넷주: ")

    ## 5G통신주 - 버라이즌, AT
    # 버라이즌 접속
    connectToLink("https://kr.investing.com/equities/verizon-communications", name, change)

    # AT접속
    connectToLink("https://www.investing.com/equities/at-t", name, change)

    select_stock("5G통신주: ")

    ## 컨슈머주 - 월마트
    # 월마트 접속
    connectToLink("https://kr.investing.com/equities/wal-mart-stores", name, change)

    select_stock("컨슈머주: ")

    ## 은행주 - 뱅오아, 제이피모건
    # 뱅크오브아메리카 접속
    connectToLink("https://www.investing.com/equities/bank-of-america", name, change)

    # 제이피모건 접속
    connectToLink("https://kr.investing.com/equities/jp-morgan-chase", name, change)

    select_stock("은행주: ")

    ##의료, 헬스케어주 - 화이자, 모더나, 존슨앤존슨
    # 화이자 접속
    connectToLink("https://kr.investing.com/equities/pfizer", name, change)

    # 모더나 접속
    connectToLink("https://kr.investing.com/equities/moderna", name, change)

    # 존슨앤존슨
    connectToLink("https://kr.investing.com/equities/johnson-johnson", name, change)

    select_stock("헬스케어주: ")

    driver.quit()

def connectToLink(url, name_List, change_list):
    driver.get(url)
    time.sleep(2)
    # name_list : 웹 표지에 있는 종목명
    name_List.append(driver.find_element_by_xpath('//*[@id="leftColumn"]/div[1]/h1').text)

    # change_list : 웹 표지에 있는 종목의 변동률(%)
    try:
        change_list.append(
            driver.find_element_by_xpath('//*[@id="quotes_summary_current_data"]/div[1]/div[1]/div[1]/div[2]/span[4]').text)
    except:
        change_list.append(
            driver.find_element_by_xpath('//*[@id="quotes_summary_current_data"]/div[1]/div[2]/div[1]/span[4]').text)


def select_stock(tpye):
    for i in range(0, len(change)):
        # change에 있는 부호(+,-)와 %를 없애고 int로 만들어주는 작업
        str_change = change[i]
        float_change1 = str_change[:-1]
        float_change2 = float(float_change1[1:])

        if float_change2 > 1.3:
            selected_index.append(i)

    if len(selected_index) > 0:
        for i in range(0, len(selected_index)):
            print(tpye + name[selected_index[i]] + ", " + change[selected_index[i]])

    name.clear()
    change.clear()
    selected_index.clear()