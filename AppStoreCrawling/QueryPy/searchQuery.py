import json
import time
import requests

# 조건에 맞게 요청URL을 만들고 json파일 반환 받기
def SearchAppStore(searchName="game", searchType="ios", county="kr", appNum="50"):
    typeTxt = 'software%2CiPadSoftware&term=' # 아이폰+아이패드 어플 검색
    if searchType == "iphone": # 아이폰에서 사용가능한 어플을 검색할 때
        typeTxt = "software&term=" 
    elif searchType == "ipad": # 아이패드에서 사용가능한 어플을 검색할 때
        typeTxt = 'iPadSoftware&term='
    elif searchType == 'mac':
        typeTxt = 'macSoftware&term='
    realUrl = 'https://itunes.apple.com/search?media=software&entity=' + typeTxt + searchName + '&country=' + county + '&limit=' + appNum
    
    # 위에 만든 URL로 애플한테 json파일 받아오기
    searchJson = requests.get(realUrl)
    searchJson.raise_for_status()

    # json.loads()함수는 json파일을 Python의 dist(딕셔너리) 형식으로 바꿔줍니다.
    return json.loads(searchJson.text)

# 받은 json파일을 분석해 필요한 정보를 csv파일으로 만들기
def makeCSVfile(jsonObject, searchName="game"):
    # csv파일을 쓰기 시~작!
    filename = searchName + '.json'
    f = open(filename, 'w', encoding='utf-8-sig', newline='')

    # 받은 모든 앱에 대한 응답에서
    for app in jsonObject['results']:
        oneRow = json.dumps(app, ensure_ascii=False)
        print(oneRow)
        f.write(oneRow)
        f.write("\n")
        # print("====================================================================")

if __name__ == "__main__":
    print("앱 스토어 검색/크롤러 프로그램입니다.")
    how = input("예시를 보고 싶으면 1를, 검색어를 직접 입력하고 싶으면 2를 입력하시고 Enter엔터를 누르세요")
    if how == '1':
        print("예시에서 검색어는 'game', 검색할 앱 종류는IOS(아이폰, 아이패드), 검색할 국가는 한국이며, ")
        print("상위50개 앱의 정보를 크롤러합니다. csv파일은 같은 경로에 gameQueryData.csv로 저장됩니다.")
        print("10초 뒤 크롤러가 시작됩니다.")
        time.sleep(10)
        makeCSVfile(SearchAppStore())
    elif how == '2':
        name = input("검색어를 입력 하세요: ")
        topNum = input("상위 몇 개의 앱을 가져올까요?(200이하의 자연수를 입력하세요): ")
        if isinstance(int(topNum), int) and int(topNum) < 201:
            makeCSVfile(SearchAppStore(searchName=name, appNum=topNum),name)
            print("크롤러 완료! csv파일은 \"",name,"QueryData.csv\"에 저장했습니다.")
        else: 
            print("200이하의 자연수가 아닙니다.")
    else:
        print("1 또는 2가 아닙니다.")

    


    

    

        
    

