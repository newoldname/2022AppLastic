# Version: 1.1
# 페이지의 UpdateTime를 사용해 중복 파일을 검사함
import os
import json
import time
import schedule
import chartJson1 as chart
# chartJson1 Version: 1.5

a = 0 # debug

# 차트 앱 고유 ID 받아오기
def getChartIDScheduled(jsonObject):
    appIdList = []  # 차트안의 앱들의 고유ID를 저장하는 리스트
    if len(jsonObject['feed']) < 8:
        return [], "None"

    # 차트 업데이트 시간 가져오기
    chartTime = jsonObject['feed']['updated']['label']
    chartNameArr = jsonObject['feed']['id']['label']
    realChartName = chartNameArr.split("/", 3)[-1]

    # 시간 파일 읽고 업데이트 시간 확인
    f = open("./timeChecker.json", 'r', encoding="utf-8")
    fileString = f.read()
    if fileString == "":
        checkerDict = {}
    else:
        checkerDict = json.loads(fileString)
    f.close()

    if realChartName in checkerDict and checkerDict[realChartName] == chartTime:
        return [], "None"
    else:
        checkerDict[realChartName] = chartTime
        f = open("timeChecker.json", 'w', encoding='utf-8', newline='')
        json.dump(checkerDict, f, indent=2)
        f.close()

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


def autoSchedule():
    global a
    a+=1
    chartJson, chartName, countryName, appCategoryName = chart.chartAppStore()
    appList, chartUpdateTime = getChartIDScheduled(chartJson)
    chartFileName = str(a) + "schedule" + str(len(appList)) + countryName + chartUpdateTime
    chart.searchByIdAndCSV(appList, countryName, chartUpdateTime, listName=chartFileName)
    print("Once, a=", a)


if __name__ == "__main__":
    filePath = './timeChecker.json'
    if not os.path.isfile(filePath):
        f = open("timeChecker.json", 'w', encoding='utf-8', newline='')
        f.close()
    schedule.every().do(autoSchedule)
    while True:
        schedule.run_pending()
        time.sleep(1)
