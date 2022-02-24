from re import T
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv

# 동적 페이지에 대해 셀레니움으로 처리하기 
# - 크롬 안띄우고 처리해보기(headless chrome : Chrome without Chrome)

# 현재 로딩된 앱 개수(글로벌  변수)
appNum = 0

# 로딩이 왼료했는지 검사 
# 원리: 이전의 앱 개수와 현재의 앱 개수 비교, 현재의 앱 개수가 많아졌으면 로딩이 완료된 상황
def howManyApp(web): # 현재 돌고 있는 브로우저를 변수로 가져오기 
    global appNum
    soup = BeautifulSoup(web.page_source, 'lxml')

    # 현재 앱 개수 계산
    now = len(soup.find_all('li', attrs={'class':'ii-row media'}))
    if now == appNum: # 앱 개수가 변하지 않았다면
        return False 
    else: # 앱 개수가 변했다면
        appNum = now # 앱 개수 갱신
        return now # 숫자를 반환함으로써 while문에서 True의 역할을 해줌

def AppStoreSearchPage(searchName="요리게임", deviceOs="ios", county="kr"):
    ## 크롬 띄우고 처리할 경우 아래를 주석 처리 -----------------------
    # options = webdriver.ChromeOptions()
    # options.headless = True  # 크롬 안띄우기
    # options.add_argument('window-size=1920x1080')  # 윈도우 창 크기 지정
    # browser = webdriver.Chrome('./chromedriver.exe', options=options)
    # 여기까지 주석 처리 -------------------------------------------

    browser = webdriver.Chrome('./chromedriver.exe')  # 크롬 띄울 경우 주석 처리 풀기
    browser.maximize_window()

    # url는 함수 호출 시의 변수에 따라 자동 생성됨
    url = 'https://fnd.io/#/' + county + '/search?mediaType=' + deviceOs + '&term=' + searchName
    browser.get(url)

    WebDriverWait( browser , 10 ).until(EC.presence_of_element_located((By.CLASS_NAME, 'media-list')))

    # 초기 앱 개수 저장
    soup = BeautifulSoup(browser.page_source, 'lxml')
    global appNum
    appNum = len(soup.find_all('li', attrs={'class':'ii-row media'}))

    # 페이지 스크롤 및 로딩 판단 
    for i in range(3):

        # js 명령어를 통해 페이지를 가장 아래로 한 번 내리기
        browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')

        a = 0 # 로딩 판단 횟수
        end = False # 스크롤 끝낼 지 결정하는 변수
        while not howManyApp(browser): # 로딩이 아직 안 끝나면
            a+=1 # 로딩 안됨 횟수 +1
            if a>20: # 만약 계속 로딩이 안되면 (로딩 안된 횟수가 20번을 넘으면)
                end = True # 페이지 스크롤 종료하게 만들기
                break # while문 나가기
            time.sleep(0.1) # 0.1초동안 로딩하는 걸 기다리기
        if end: break # 계속 로딩이 안되면 스크롤 동작 종료(for문에서 나가기)
    print('스크롤 완료')
    print('지금까지 나온 앱 개수: ', appNum)

    # 지금까지의 웹페이지를 bs에 가져오기
    soup = BeautifulSoup(browser.page_source, 'lxml')

    # 모든 앱의 element 찾기
    appList = soup.find_all('div', class_='media-heading ii-media-heading col-xs-8 col-sm-10')
    
    # csv파일 새로 만들기
    filename = 'data.csv'
    f = open(filename, 'w', encoding='utf-8-sig', newline='')
    writer = csv.writer(f)
    writer.writerow(["AppName", 'AppType', 'AppRate', 'isIphone', 'isIpad', 'AppUrl'])
    # 각 앱(의 element)에 대해
    for app in appList:
        appName = app.a.div.span.get_text()
        print('앱 이름:', appName) # 앱 이름 출력

        appShortUrl = app.a['href']
        appRealUrl = 'https://fnd.io/' + appShortUrl
        print('앱 링크:', appRealUrl) # 앱 링크 출력

        # 참고: 여기는 일반적인 방법이 아닌 해당 웹에 특화된 크롤러 방법이다
        # 그래서 앱의 카테고리, 아이폰/패드 지원 여부, 리뷰 수의 크롤러 방법이
        # 조금 이상하게 했습니다(뭐 결과만 잘 나오면 되죠 ㅎㅎ)
        lastData = app.find_next('div')
        appTypeAndSupport = lastData.find_next('div').text
        noSpace = appTypeAndSupport.replace(" ", "")
        lastArr = noSpace[:-6].split("\n")
        appType = lastArr[3]
        print('앱 카테고리:', appType) # 앱 카테고리 출력
        
        iphok = False
        ipadok = False
        if "iphone" in lastArr: iphok = True 
        if "ipad" in lastArr: ipadok = True
        print("아이폰 지원여부:", iphok) # 아이폰 지원 여부
        print("아이패드 지원여부:", ipadok) # 아이패드 지원 여부
        if lastArr[-1] != "":
            appRate = int(lastArr[-1].split("(")[1].replace(",",""))
        else: appRate = 0
        print('앱 리뷰 수:', appRate) # 앱 리뷰수 출력
        print("====================================================")
        input("Debugging Mode, Click enter to continue")
        writer.writerow([appName, appType, appRate, iphok, ipadok, appRealUrl])

    browser.quit()    

AppStoreSearchPage()