# Version: 1.1
# Date: 2022-02-28

# chartJson1 Version: 1.5
import chartJson1 as chart
import time

categoryKorArr = ['도서', '비즈니즈', '교육', '엔터테인먼트', '금융', '음식 및 음료', '게임', '액션게임', '어드벤처게임', '캐주얼게임', '보드게임', '카드게임',
                  '카지노게임', '가족게임', '음악게임', '퍼즐게임', '레이싱게임', '롤플레잉게임', '시뮬레이션게임', '스포츠게임', '전략게임', '퀴즈게임', '단어게임',
                  '건강 및 피트니트', '라이프 스타일', '의료', '음악', '네비게이션', '뉴스', '잡지 및 신문', '사진 및 비디오', '생산성', '참고', '쇼핑',
                  '소셜 네트워킹', '스포츠', '여행', '유틸리티', '날씨']
categoryEngArr = ['Book', 'Business', 'Education', 'Entertainment', 'Finance', 'Food & Drink', 'Games', 'Games-Action',
                  'Games-Adventure', 'Games-Arcade', 'Games-Board', 'Games-Card', 'Games-Casino', 'Games-Family',
                  'Games-Music', 'Games-Puzzle', 'Games-Racing', 'Games-Role Playing', 'Games-Simulation',
                  'Games-Sports', 'Games-Strategy', 'Games-Trivia', 'Games-Word', 'Health & Fitness', 'Lifestyle',
                  'Medical', 'Music', 'Navigation', 'News', 'Newsstand', 'Photo & Video', 'Productivity', 'Reference',
                  'Shopping', 'Social Networking', 'Sports', 'Travel', 'Utilities', 'Weather']
categoryIdArr = ['6018', '6000', '6017', '6016', '6015', '6023', '6014', '7001', '7002', '7003', '7004', '7005', '7006',
                 '7009', '7011', '7012', '7013', '7014', '7015', '7016', '7017', '7018', '7019', '6013', '6012', '6020',
                 '6011', '6010', '6009', '6021', '6008', '6007', '6006', '6024', '6005', '6004', '6003', '6002', '6001']

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


def jsonOnce(chartInput, categoryBool, category, countryCode="kr"):
    chartJson, chartName, countryName, appCategoryName = chart.chartAppStore(chartType=chartInput, appNum="200",
                                                                             country=countryCode, 
                                                                             isAppCategory=categoryBool,
                                                                             appCategory=category)
    appList, chartTime = chart.getChartID(chartJson)
    chartFileName = "AUTO" + chartName + "iPhone" + str(len(appList)) + countryName + appCategoryName
    chart.searchByIdAndCSV(appList, countryCode, chartTime, listName=chartFileName)


def autojson(countryName):
    print("!!!====Warning===!!!===!!!====Warning===!!!===!!!====Warning===!!!")
    print("!!!본 함수는 해당 국가의 앱스토어의 모든 인기 차트를 한 번에 받아옵니다.")
    print("!!!같은 경로에 약 120개의 json파일이 생성되며,")
    print("!!!빈 폴더에서 이 함수를 실행할 것을 강력히 권장합니다!")
    print("!!!함수는 15초 후에 실행될 예정이니, 폴더을 잘 확인하시기 바랍니다.")
    print("!!!====Warning===!!!===!!!====Warning===!!!===!!!====Warning===!!!")
    time.sleep(15)
    start = time.time()
    for i in range(len(categoryIdArr)):
        for j in ['topfree', 'toppaid', 'topgrossing']:
            print(categoryIdArr[i], ":", j)
            jsonOnce(j, True, categoryIdArr[i], countryCode=countryName)

    for k in ['topfree', 'toppaid', 'topgrossing', 'new', 'newfree', 'newpaid']:
        jsonOnce(k, False, "None", countryCode=countryName)
    print("총 소요 시간(초):", time.time() - start)

def showCountryName():
    for i in range(0, len(countryArr), 3):
        end = i + 3
        if end > len(countryArr): end = len(countryArr)
        for j in range(i, end):
            print(countryArr[j], ":", countryNameArr[j], "\t\t\t", end="")
        print("")


def chooseCountryAndStart():
    checkNum = input("한국 차트를 원하시면 1를, 아니면 2를 입력하세요")
    if checkNum == "1":
        autojson("kr")
    elif checkNum == "2":
        countryCode = input("해당 나라의 2자리 코드를 입력하세요")
        while countryCode not in countryArr:
            print("해당 나라 코드가 존재하지 않습니다.")
            codeShow = input("전체 나라이름 및 2자리 코드를 보고 싶으면 1를, 아니면 2를 입력하세요")
            if codeShow == "1":
                showCountryName()
            countryCode = input("해당 나라의 2자리 코드를 정확히 입력하세요")
        autojson(countryCode)
    else: print("1또는 2가 아닙니다.")


if __name__ == "__main__":
    print("!!!====Warning===!!!===!!!====Warning===!!!===!!!====Warning===!!!")
    print("!!!본 프로그램은 한국 앱 스토어의 모든 차트를 한 번에 가져옵니다.")
    print("!!!같은 경로에 약 120개의 json파일이 생성되며,")
    print("!!!빈 폴더에서 이 프로그램을 실행할 것을 강력히 권장합니다!")
    print("!!!위 글을 모두 이해하셨고, 폴더/경로를 확인하셨다면 ")
    check = input("!!!\"understand\"를 입력해 프로그램을 시작하세요:")
    if check == "understand": chooseCountryAndStart()
    else: print("입력이 다릅니다. 프로그램을 종료합니다.")