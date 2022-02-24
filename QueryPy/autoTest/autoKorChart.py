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


def jsonOnce(category, chartInput, categoryBool, countryCode="kr"):
    chartJson, chartName, countryName, appCategoryName = chart.chartAppStore(chartType=chartInput, appNum="200",
                                                                             isAppCategory=categoryBool,
                                                                             appCategory=category,
                                                                             country=countryCode)
    appList = chart.getChartID(chartJson)
    chartFileName = "AUTO" + chartName + "iPhone" + str(len(appList)) + countryName + appCategoryName
    chart.searchByIdAndCSV(appList, listName=chartFileName)


def autojson(countryName="kr"):
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
            jsonOnce(categoryIdArr[i], j, True,countryCode=countryName)
        # time.sleep(0.5)

    for k in ['topfree', 'toppaid', 'topgrossing', 'new', 'newfree', 'newpaid']:
        jsonOnce("None", k, False)
    print("총 소요 시간(초):", time.time() - start)


if __name__ == "__main__":
    print("!!!====Warning===!!!===!!!====Warning===!!!===!!!====Warning===!!!")
    print("!!!본 프로그램은 한국 앱 스토어의 모든 차트를 한 번에 가져옵니다.")
    print("!!!같은 경로에 약 120개의 json파일이 생성되며,")
    print("!!!빈 폴더에서 이 프로그램을 실행할 것을 강력히 권장합니다!")
    print("!!!위 글을 모두 이해하셨고, 폴더/경로를 확인하셨다면 ")
    check = input("!!!\"understand\"를 입력해 프로그램을 시작하세요:")
    if check == "understand": autojson()
    else: print("입력이 다릅니다. 프로그램을 종료합니다.")