import json
import requests
import time


# url를 만들고 딕셔너리 형식으로 데이터들을 반환하기
# 나라 코드가 정확한 지 검토하는 기능은 다음 업데이트에
def getWeb2Dict(appid, countryCode="kr"):
    reviewDictArr = []
    for i in range(1,11):
        nowurl = "https://itunes.apple.com/" + countryCode + "/rss/customerreviews/page=" + str(i) + "/id=" + str(appid) + "/sortby=mostrecent/json"
        print(nowurl)
        #input()
        gethtml = requests.get(nowurl)
        for i in range(1,6):
            if gethtml.status_code == requests.codes.ok:
                break
            else:
                print("Requests.get오류 발생, ", i, "초 후에 다시 시도하겠습니다.")
                time.sleep(i)
                gethtml = requests.get(nowurl)
            if i == 5:
                gethtml.raise_for_status()
        htmlDict = json.loads(gethtml.text)
        if not htmlDict['feed'].get('entry'): break
        else: reviewDictArr.extend(htmlDict['feed']['entry'])
    return reviewDictArr

# 필요한 정보/리뷰를 골라서 저장하기
def getReview2Json(dictArr, appid):
    filename = "reviwe" + str(appid) + '.json'
    f = open(filename, 'w', encoding='utf-8-sig', newline='')
    for review in dictArr:
        print(review)
        newdict={}
        newdict["UpdateTime"] = review["updated"]["label"]
        newdict["rating"] = review["im:rating"]["label"]
        newdict["title"] = review["title"]["label"]
        newdict["content"] = review["content"]["label"]
        onerow = json.dumps(newdict, ensure_ascii=False)
        f.write(onerow)
        f.write("\n")
    f.close()

def simpleReview(appid, countryCode="kr"):
    getReview2Json(getWeb2Dict(appid), appid)
    print("리뷰 크롤링 완료")


id = int(input("예시를 보고 싶으면 1를 입력하시고, 특정 앱의 리뷰를 보고 싶으면 앱의 id를 입력하세요"))
if id == 1: id = "544007664"
simpleReview(str(id))





# 나중에 엡데이트 해도 좋은 것들:
# 1. 