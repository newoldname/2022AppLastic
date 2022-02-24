import csv
import json
import time
import requests

# 조건에 맞게 요청URL을 만들고 json파일 반환 받기
def chartAppStore(chartType="topfree", isIpadApp=False, appNum="100"):
    deviceName = "applications" # 디바이스 종류
    # 차트 종류
    chartTypeList = ['topfree', 'toppaid', 'topgrossing', 'new', 'newfree', 'newpaid'] 
    if isIpadApp: # 아이패드이면 
        deviceName = "ipadapplications"   # 디바이스 -> 아이패드
        chartTypeList = chartTypeList[:3] # 아이패드에서 없는 차트 제거
    #==맥OS는 나중에 업데이트할 예정==#

    # 차트 이름이 정확한 지 검토
    while chartType not in chartTypeList: # 입력한 차트 이름이 차트 리스트에 존재하지 않다면
        print("차트 종류은 다음과 같다. 아래 중 하나를 정확하게 입력하시고 Enter엔터를 누르세요") 
        print(chartTypeList) # 모든 차트 이름 출력
        chartType = input() # 차트 이름 입력하기
    
    #====국가 및 카테고리 설정은 나중에 업데이트할 예정====#
    country="kr"                                #
    appCategory = "/genre=카테고리 고유ID/"        #
    #==========================================#

    # URL에 사용한 문자열 만들기
    chartDevice = chartType + deviceName
    realUrl = 'https://itunes.apple.com/'+ country + '/rss/' + chartDevice + '/limit=' + appNum + '/json'

    # 위에 만든 URL로 애플한테 json파일 받아오기
    searchJson = requests.get(realUrl)
    searchJson.raise_for_status()

    # json.loads()함수는 json파일을 Python의 dist(딕셔너리) 형식으로 바꿔줍니다.
    return json.loads(searchJson.text), chartType

# 차트 앱 고유 ID 받아오기
def getChartID(jsonObject):
    appIdList = [] # 차트안의 앱들의 고유ID를 저장하는 리스트

    # 각 앱에 대해
    for app in jsonObject['feed']['entry']:
        # 앱 고유 ID 저장
        appIdList.append(app['id']['attributes']["im:id"])
        print(appIdList[-1])
    print("================================")
    return appIdList, len(appIdList)
    #==차트에 대한 정보(갱신 시간, 차트 공식 이름)은 나중에 업데이트할 예정==#

# 위에서 받은 앱 ID들의 정보을 받아오고 csv파일으로 저장하기
def searchByIdAndCSV(appIdList, listName='topfreechart'):
    nowRanking = 0 # 현재 링킹을 표시하기 위한 변수이다.
    # === csv파일 작성 구간 === #
    filename = listName + 'Data.csv'
    f = open(filename, 'w', encoding='utf-8-sig', newline='')
    writer = csv.writer(f)
    writer.writerow(["앱 이름", "순위", '아이폰 지원여부', '아이패드 지원여부', '앱 총평점', '앱 총리뷰수', '앱 메인 카테고리', '앱 가격', '앱 링크', '앱 상세설명', ])
    
    # 앱 10개씩 돌린다. 
    for i in range(0,len(appIdList),10):
        # === 남은 앱이 10개 미만일 때 인덱스 정확히 하기
        end = i+10
        if end>len(appIdList): end = len(appIdList)
        print("i: ", i, ", and end: ", end)

        #한 번에 앱 10개의 정보를 요청하기
        appIdListStr = ""
        for j in appIdList[i:end]:
            appIdListStr = appIdListStr + j + ","
        #앱 10개의 정보를 요청하는 URL
        lookAppUrl = 'https://itunes.apple.com/lookup?id=' + appIdListStr[:-1] + "&country=kr"
        print(lookAppUrl)

        # 위에 만든 URL로 애플한테 json파일 받아오기
        lookAppJson = requests.get(lookAppUrl)
        lookAppJson.raise_for_status()

        # json.loads()함수는 json파일을 Python의 dict(딕셔너리) 형식으로 바꿔줍니다.
        lookAppDict = json.loads(lookAppJson.text)
        # 각 앱에 대해
        for app in lookAppDict['results']:
            # print를 통해 코드를 이해하세요!
            appName = app['trackName']
            print('앱 이름:',appName)

            iphok = False
            if len(app['screenshotUrls']) > 0: iphok = True
            ipadok = False
            if len(app['ipadScreenshotUrls']) > 0: ipadok = True
            # ipad스크린샷 조차 없는 버그(애플의 실수)가 있어서 
            # 실제 지원 제품군의 이름을 통해 아이폰/아이패드 지원 여부 판단
            if not iphok:
                for supportName in app['supportedDevices']:
                    print(supportName)
                    input()
                    if supportName.find("iPhone") != -1:
                        print("iphone oked")
                        iphok = True
                        break
            if not ipadok:
                for supportName in app['supportedDevices']:
                    print(supportName)
                    input()
                    if supportName.find("iPad") != -1:
                        print("ipad oked")
                        ipadok = True
                        break
            print("iPhone 지원 여부:", iphok)
            print("iPad 지원 여부:", ipadok)
                
            appRate = app['averageUserRating']
            appRateNum = app['userRatingCount']
            print('총 ', appRateNum,'명이 ',appRate,'점을 줌.')

            mainCategory = app['primaryGenreName']
            print("공식 메인 카테고리는:",mainCategory)

            categorys = app['genres']
            categorysIds = app['genreIds']
            print('공식 세부 카테고리: ', end="")
            for i in range(len(categorys)):
                print('<', categorys[i], ', id=',categorysIds[i],'>', end="")
            print()

            appPrice = app['price']
            print("가격:",appPrice)

            appUrl = app['trackViewUrl']
            print("앱 링크:", appUrl)

            appDetail = app['description']
            appDetail = appDetail.replace("\n", ".")
            print("앱 상세 설명:",appDetail)

            

            nowRanking+=1
            writer.writerow([appName, nowRanking, iphok, ipadok, appRate, appRateNum, mainCategory, appPrice, appUrl, appDetail])

            print("====================================================================")
    f.close()

if __name__ == "__main__":
    print("앱 스토어 검색/크롤러 프로그램입니다.")
    how = input("예시를 보고 싶으면 1를, 세부 설정을 원하시면 2를 입력하시고 Enter엔터를 누르세요")
    if how == '1':
        print("=====================================================================")
        print('==예시는 "상위 100개"의 "한국" "아이폰" "무료 인기차트"이다.')
        print("==csv파일은 같은 경로에 topfreeiPhone100Data.csv로 저장됩니다.")
        print("==10초 뒤 크롤러가 시작됩니다.")
        time.sleep(10)
        chartJson, chartName = chartAppStore()
        appList, realAppNum = getChartID(chartJson)
        chartFileName = chartName + "iPhone" + str(realAppNum)
        searchByIdAndCSV(appList, listName=chartFileName)
    elif how == '2':
        isipad = input("아이폰 차트는 1, 아이패드 차트는 2를 입력하시고 Enter엔터를 누르세요: ")
        if isipad == "2":
            isipad = True
            print("아이패드 차트로 설정합니다")
        else:
            isipad = False
            print("아이폰 차트로 설정합니다")
        
        print("상위 몇 개의 앱을 가져올까요?(200이하의 자연수를 입력하세요): ")
        topNum = input("참고로 일부 차트에서 개수만큼 반환하지 않아서 실제 개수는 파일 이름을 참고하시기 바랍니다.")
        if isinstance(int(topNum), int) and int(topNum) < 201:
            chartJson, chartName = chartAppStore(chartType="none", isIpadApp=isipad, appNum=topNum)
            appList, realAppNum = getChartID(chartJson)
            chartFileName = chartName + ("iPad" if isipad else "iPhone") + str(realAppNum)
            searchByIdAndCSV(appList, listName=chartFileName)
            print("크롤러 완료!")
        else: 
            print("200이하의 자연수가 아닙니다.")
    else:
        print("1 또는 2가 아닙니다.")

