from flask import Blueprint,render_template,abort
import requests
import os
from requests import ConnectionError,ConnectTimeout,HTTPError,TooManyRedirects
import csv

tableApp = Blueprint('table_page',__name__)
apikey = '84a024b0-1d85-460c-b330-d96b9ea12cb9'
import json
with open('./w2rds-bdv5s.json',encoding="utf-8")as f:
    data = json.load(f)

@tableApp.route('/table',defaults={'region':None})
@tableApp.route('/table/<region>')
def table(region):
    '''
    if not os.path.exists('./csv/新北市.csv'):
        print("下載中")
        
        if response.status_code == 200:
            print("下載成功")
            with open('./csv/test.csv',mode='w',encoding='utf-8') as file:
                file.write(response.text)
            print('存檔完成')

    with open('./csv/test.csv',mode='r',encoding='utf-8') as file:
        next(file)
        csvReader = csv.reader(file)
        datalist = list(csvReader)
        print(datalist)
        print(datalist.__class__)
    print(len(datalist))
'''
    jsonObject = data
    sareas = list({datalist['品牌'] for datalist in jsonObject})

    if region is None:

        dataDict = dict()
        for key in sareas:
            regionList = [item for item in jsonObject if item['品牌'] == key]
            dataDict[key] = regionList

        for key, value in dataDict.items():
            print(key)
            #print(value)
            print(value.__class__)
            print("=========")

        return render_template('table.html', data=data, regions=sareas)
    else:
        areaList = [item for item in jsonObject if item['品牌'] == region]
        print(areaList)
        return render_template('table.html', data=areaList, regions=sareas, region=region)



