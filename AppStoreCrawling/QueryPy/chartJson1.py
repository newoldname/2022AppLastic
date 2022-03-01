# Version: 1.5.1
# 각각의 앱 정보를 출력할 지 결정하는 변수 추가함
# 1.5와 호환합니다.
import json
import time
import requests


# 조건에 맞게 요청URL을 만들고 json파일 반환 받기
def chartAppStore(chartType="topfree", isIpadApp=False, appNum="100", country="kr", isAppCategory=False,
                  appCategory='none'):
    deviceName = "applications"  # 디바이스 종류
    # 차트 종류
    chartTypeList = ['topfree', 'toppaid', 'topgrossing', 'new', 'newfree', 'newpaid']
    if isIpadApp:  # 아이패드이면
        deviceName = "ipadapplications"  # 디바이스 -> 아이패드
        chartTypeList = chartTypeList[:3]  # 아이패드에서 없는 차트 제거
    # ==맥OS는 나중에 업데이트할 예정==#

    # 차트 이름이 정확한 지 검토
    while chartType not in chartTypeList:  # 입력한 차트 이름이 차트 리스트에 존재하지 않다면
        print("차트 종류은 다음과 같다. 아래 중 하나를 정확하게 입력하시고 Enter엔터를 누르세요")
        print(chartTypeList)  # 모든 차트 이름 출력
        print("(참고로 차트 종류가 new, newfree, newpaid일 경우 카테고리는 적용할 수 없고, 앱 100개가 반환됩니다.)")
        chartType = input()  # 차트 이름 입력하기

    countryArr = ["al", "dz", "ao", "ai", "ag", "ar", "am", "au", "at", "az", "bs", "bh", "bb", "by", "be",
                  "bz", "bj", "bm", "bt", "bo", "bw", "br", "vg", "bn", "bg", "bf", "kh", "ca", "cv", "ky", "td", "cl",
                  "cn", "co", "cg", "cr", "hr", "cy", "cz", "dk", "dm", "do", "ec", "eg", "sv", "ee", "fj", "fi", "fr",
                  "gm", "de", "gh", "gr", "gd", "gt", "gw", "gy", "hn", "hk", "hu", "is", "in", "id", "ie", "il", "it",
                  "jm", "jp", "jo", "kz", "ke", "kr", "kw", "kg", "la", "lv", "lb", "lr", "li", "lt", "lu", "mo", "mk",
                  "mg", "mw", "my", "ml", "mt", "mr", "mu", "mx", "fm", "md", "mn", "me", "ms", "mz", "na", "np", "nl",
                  "nz", "ni", "ne", "ng", "no", "om", "pk", "pw", "pa", "pg", "py", "pe", "ph", "pl", "pt", "qa", "ro",
                  "ru", "st", "sa", "sn", "sc", "sl", "sg", "sk", "si", "sb", "za", "es", "lk", "kn", "lc", "vc", "sr",
                  "sz", "se", "ch", "tw", "tj", "tz", "th", "tt", "tn", "tr", "tm", "tc", "ug", "ua", "ae", "gb", "us",
                  "uy", "uz", "ve", "vn", "ye", "zw"]
    countryNameArr = ["Albania", "Algeria", "Angola", "Anguilla", "Antigua and Barbuda", "Argentina", "Armenia",
                      "Australia", "Austria", "Azerbaijan", "Bahamas", "Bahrain", "Barbados", "Belarus", "Belgium",
                      "Belize",
                      "Benin", "Bermuda", "Bhutan", "Bolivia", "Botswana", "Brazil", "British Virgin Islands",
                      "Brunei Darussalam",
                      "Bulgaria", "Burkina Faso", "Cambodia", "Canada", "Cape Verde", "Cayman Islands", "Chad", "Chile",
                      "China",
                      "Colombia", "Congo Republic of the", "Costa Rica", "Croatia", "Cyprus", "Czech Republic",
                      "Denmark", "Dominica",
                      "Dominican Republic", "Ecuador", "Egypt", "El Salvador", "Estonia", "Fiji", "Finland", "France",
                      "Gambia", "Germany",
                      "Ghana", "Greece", "Grenada", "Guatemala", "Guinea-Bissau", "Guyana", "Honduras", "Hong Kong",
                      "Hungary", "Iceland",
                      "India", "Indonesia", "Ireland", "Israel", "Italy", "Jamaica", "Japan", "Jordan", "Kazakhstan",
                      "Kenya", "Korea Republic Of",
                      "Kuwait", "Kyrgyzstan", "Lao People's Democratic Republic", "Latvia", "Lebanon", "Liberia",
                      "Liechtenstein", "Lithuania",
                      "Luxembourg", "Macau", "Macedonia", "Madagascar", "Malawi", "Malaysia", "Mali", "Malta",
                      "Mauritania", "Mauritius",
                      "Mexico", "Micronesia Federated States of", "Moldova", "Mongolia", "Montenegro", "Montserrat",
                      "Mozambique", "Namibia",
                      "Nepal", "Netherlands", "New Zealand", "Nicaragua", "Niger", "Nigeria", "Norway", "Oman",
                      "Pakistan", "Palau", "Panama",
                      "Papua New Guinea", "Paraguay", "Peru", "Philippines", "Poland", "Portugal", "Qatar", "Romania",
                      "Russia", "São Tomé and Príncipe",
                      "Saudi Arabia", "Senegal", "Seychelles", "Sierra Leone", "Singapore", "Slovakia", "Slovenia",
                      "Solomon Islands", "South Africa",
                      "Spain", "Sri Lanka", "St. Kitts and Nevis", "St. Lucia", "St. Vincent and The Grenadines",
                      "Suriname", "Swaziland", "Sweden",
                      "Switzerland", "Taiwan", "Tajikistan", "Tanzania", "Thailand", "Trinidad and Tobago", "Tunisia",
                      "Turkey", "Turkmenistan",
                      "Turks and Caicos", "Uganda", "Ukraine", "United Arab Emirates", "United Kingdom",
                      "United States", "Uruguay", "Uzbekistan",
                      "Venezuela", "Vietnam", "Yemen", "Zimbabw"]
    while country not in countryArr:  # 입력한 국가 코드가 국가 리스트에 존재하지 않다면
        print("===국가 코드 입니다=================================")
        for i in range(0, len(countryArr), 3):
            end = i + 3
            if end > len(countryArr): end = len(countryArr)
            for j in range(i, end):
                print(countryArr[j], ":", countryNameArr[j], "\t\t", end="")
            print("")
        country = input("국가 코드는 위와 같다. 국가 코드를(2자리 알파벳) 정확하게 입력하시고 Enter엔터를 누르세요")  # 국가 코드 입력하기

    # URL에 사용한 문자열 만들기
    chartDevice = chartType + deviceName
    realUrl = 'https://itunes.apple.com/' + country + '/rss/' + chartDevice + '/limit=' + appNum + '/json'

    categoryKorArr = ['도서', '비즈니즈', '교육', '엔터테인먼트', '금융', '음식 및 음료', '게임', '액션게임', '어드벤처게임', '캐주얼게임', '보드게임', '카드게임',
                      '카지노게임', '가족게임', '음악게임', '퍼즐게임', '레이싱게임', '롤플레잉게임', '시뮬레이션게임', '스포츠게임', '전략게임', '퀴즈게임', '단어게임',
                      '건강 및 피트니트', '라이프 스타일', '의료', '음악', '네비게이션', '뉴스', '잡지 및 신문', '사진 및 비디오', '생산성', '참고', '쇼핑',
                      '소셜 네트워킹', '스포츠', '여행', '유틸리티', '날씨']
    categoryEngArr = ['Book', 'Business', 'Education', 'Entertainment', 'Finance', 'Food & Drink', 'Games',
                      'Games-Action', 'Games-Adventure', 'Games-Arcade', 'Games-Board', 'Games-Card', 'Games-Casino',
                      'Games-Family', 'Games-Music', 'Games-Puzzle', 'Games-Racing', 'Games-Role Playing',
                      'Games-Simulation', 'Games-Sports', 'Games-Strategy', 'Games-Trivia', 'Games-Word',
                      'Health & Fitness', 'Lifestyle', 'Medical', 'Music', 'Navigation', 'News', 'Newsstand',
                      'Photo & Video', 'Productivity', 'Reference', 'Shopping', 'Social Networking', 'Sports', 'Travel',
                      'Utilities', 'Weather']
    categoryIdArr = ['6018', '6000', '6017', '6016', '6015', '6023', '6014', '7001', '7002', '7003', '7004', '7005',
                     '7006', '7009', '7011', '7012', '7013', '7014', '7015', '7016', '7017', '7018', '7019', '6013',
                     '6012', '6020', '6011', '6010', '6009', '6021', '6008', '6007', '6006', '6024', '6005', '6004',
                     '6003', '6002', '6001']
    # 카테고리 입력
    if isAppCategory and chartType not in ['new', 'newfree', 'newpaid']:
        while appCategory not in categoryIdArr:  # 입력한 카테고리가 리스트에 존재하지 않다면
            print("카테고리 코드표입니다")
            for i in range(0, len(categoryIdArr), 3):
                end = i + 3
                if end > len(categoryIdArr): end = len(categoryIdArr)
                for j in range(i, end):
                    print(categoryIdArr[j], ":", categoryKorArr[j], "\t\t", end="")
                print("")
            appCategory = input("카테고리는 위와 같다. 카테고리 코드를(4자리 숫자)정확하게 입력하시고 Enter엔터를 누르세요")  # 카테고리 코드 입력하기

        # URL에 사용한 문자열 만들기
        chartDevice = chartType + deviceName
        realUrl = 'https://itunes.apple.com/' + country + '/rss/' + chartDevice + "/genre=" + appCategory + '/limit=' + appNum + '/json'
        searchJson = requests.get(realUrl)
        searchJson.raise_for_status()
    else:
        # 이는 나중에 카테고리 이름을 반환하기 위함이다.
        appCategory = "-1"
        categoryEngArr.append("All")
        categoryKorArr.append("All")
        categoryIdArr.append("-1")
    # 위에 만든 URL로 애플한테 json파일 받아오기
    searchJson = requests.get(realUrl)
    searchJson.raise_for_status()

    # json.loads()함수는 json파일을 Python의 dist(딕셔너리) 형식으로 바꿔줍니다.
    return json.loads(searchJson.text), chartType, country, categoryKorArr[categoryIdArr.index(appCategory)]


# 차트 앱 고유 ID 받아오기
def getChartID(jsonObject):
    appIdList = []  # 차트안의 앱들의 고유ID를 저장하는 리스트
    if len(jsonObject['feed']) < 8:
        return [], "None"

    # 차트 업데이트 시간 가져오기
    chartTime = jsonObject['feed']['updated']['label']

    # 차트에 앱 하나만 있을 때
    if isinstance(jsonObject['feed']['entry'], dict):
        appIdList.append(jsonObject['feed']['entry']['id']['attributes']['im:id'])
        return appIdList, chartTime
    else:  # 앱 두개 이상이 있을 때
        # 각 앱에 대해
        for app in jsonObject['feed']['entry']:
            # 앱 고유 ID 저장
            appIdList.append(app['id']['attributes']['im:id'])
            print(appIdList[-1])
        print("================================")
        return appIdList, chartTime
        # ==차트에 대한 정보(갱신 시간, 차트 공식 이름)은 나중에 업데이트할 예정==#


# 위에서 받은 앱 ID들의 정보을 받아오고 json파일으로 저장하기
def searchByIdAndCSV(appIdList, countryCode, updateTime, listName='topfreechart', printAppLog=True):
    if len(appIdList) == 0: return 0  # 반환한 app 없으면 종료하기

    nowRanking = 0  # 현재 링킹을 표시하기 위한 변수이다.

    # 파일 쓰기 시작
    filename = listName + '.json'
    f = open(filename, 'w', encoding='utf-8-sig', newline='')

    # 앱 10개씩 돌린다. 
    for i in range(0, len(appIdList), 10):
        # === 남은 앱이 10개 미만일 때 인덱스 정확히 하기 ======#
        end = i + 10  #
        if end > len(appIdList): end = len(appIdList)  #
        # print("i: ", i, ", and end: ", end)          #
        ###############################################

        # 한 번에 앱 10개의 정보를 요청하기
        appIdListStr = ""
        for j in appIdList[i:end]:
            appIdListStr = appIdListStr + j + ","

        # 앱 10개의 정보를 요청하는 URL
        lookAppUrl = 'https://itunes.apple.com/lookup?id=' + appIdListStr[:-1] + "&country=" + countryCode
        if printAppLog:
            print(lookAppUrl)
        # 위에 만든 URL로 애플한테 json파일 받아오기
        lookAppJson = requests.get(lookAppUrl)
        lookAppJson.raise_for_status()
        # json.loads()함수는 json파일을 Python의 dict(딕셔너리) 형식으로 바꿔줍니다.
        lookAppDict = json.loads(lookAppJson.text)

        # 각 앱에 대해
        for app in lookAppDict['results']:
            # 아이폰/아이패드 지원 여부 검토
            iphoneOk = False
            ipadOk = False
            for suppoetName in app["supportedDevices"]:
                if suppoetName.find("iPhone") != -1:
                    iphoneOk = True
                    break
            for suppoetName in app["supportedDevices"]:
                if suppoetName.find("iPad") != -1:
                    ipadOk = True
                    break

            app["iPhoneSupport"] = iphoneOk
            app["iPadSupport"] = ipadOk
            nowRanking += 1
            app["Ranking"] = nowRanking
            app["UpdateTime"] = updateTime
            oneRow = json.dumps(app, ensure_ascii=False)
            if printAppLog:
                print(oneRow)
            f.write(oneRow)
            f.write("\n")
    f.close()


if __name__ == "__main__":
    print("앱 스토어 검색/크롤러 프로그램입니다.")
    how = input("예시를 보고 싶으면 1를, 세부 설정을 원하시면 2를 입력하시고 Enter엔터를 누르세요")
    if how == '1':
        print("=====================================================================")
        print('==예시는 "상위 100개"의 "한국" "아이폰" "무료 인기차트"이다.')
        print("==5초 뒤 크롤러가 시작됩니다.")
        time.sleep(5)
        chartJson, chartName, countryName, appCategoryName = chartAppStore()
        appList, chartTimeStr = getChartID(chartJson)
        chartFileName = chartName + "iPhone" + str(len(appList)) + countryName + appCategoryName
        searchByIdAndCSV(appList, countryName, chartTimeStr, listName=chartFileName)
    elif how == '2':
        isipad = False
        ipadCheck = input("아이폰 차트는 1, 아이패드 차트는 2를 입력하시고 Enter엔터를 누르세요: ")
        if ipadCheck == "2":
            isipad = True
            print("아이패드 차트로 설정합니다")
        else:
            print("아이폰 차트로 설정합니다")

        print("상위 몇 개의 앱을 가져올까요? 200이하의 자연수를 입력하세요")
        topNum = input("(참고로 일부 차트에서 개수만큼 반환하지 않아서 실제 개수는 파일 이름을 참고하시기 바랍니다):")
        if isinstance(int(topNum), int) and int(topNum) < 201:
            isCategory = False
            categoryCheck = input("카테고리를 사용하시려면 1를, 아니면 2를 입력하세요")
            if categoryCheck == "1":
                print("카테고리를 적용하겠습니다.")
                isCategory = True
            else:
                print("카테고리를 적용하지 않았습니다.")
            chartJson, chartName, countryName, appCategoryName = chartAppStore(chartType="none", isIpadApp=isipad,
                                                                               appNum=topNum, country="none",
                                                                               isAppCategory=isCategory)
            appList, chartTimeStr = getChartID(chartJson)
            chartFileName = chartName + ("iPad" if isipad else "iPhone") + str(
                len(appList)) + countryName + appCategoryName
            searchByIdAndCSV(appList, countryName, chartTimeStr, listName=chartFileName)
            print("크롤러 완료!")
        else:
            print("200이하의 자연수가 아닙니다.")
    else:
        print("1 또는 2가 아닙니다.")
