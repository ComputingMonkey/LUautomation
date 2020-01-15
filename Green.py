#-*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import pandas as pd

#データをcsvに書き込む
def writeToCsv(data,file_name):
    df = pd.DataFrame(data)
    # CSV ファイル (employee.csv) として出力
    df.to_csv(file_name + ".csv")
    print(file_name + 'でcsv保存を完了しました')
#サイト(num)ページ目の会社を取得(companysに詰め込む)
def getCompanys(ori_url, num, tag, cla, search_result):
  # ori_url = 'https://doda.jp/DodaFront/View/JobSearchList.action?so=50&tp=1&pic=1&ind=11L&es=2&ds=0&pr=13&page='
  num = str(num)
  html_doc = requests.get(ori_url + num).text
  soup = BeautifulSoup(html_doc, 'html.parser') # BeautifulSoupの初期化
  blocks = soup.find_all(tag, class_=cla)
  #それぞれのブロックについて企業名を取得
  if num == 1:
      companys.append('検索結果' + search_result)
  companys.append('【' + search_result + '】')
  for block in blocks:
    company = block.string
    companys.append(company)

#num回スクレイピングを繰り返す
def pagesToCompanys(num):
    for i in range(num):
      getCompanys(ori_url, num, tag, cla, search_result)
      percent = 100 * (i / num)
      print(str(percent) + '％')
      if i == num - 1:
          print('100％完了:' + search_result)
          print('合計' + str(len(companys)) + '企業取得しました')



companys = []
#Greenのスクレイピング
#ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー
search_result = "IT/Web・通信・インターネット系✖️ソフトウェア/パッケージベンダ"
ori_url = 'https://www.green-japan.com/search_key/01?key=ottqep2gz9fa4c7cwbxq&keyword=&page='
tag = 'h3'
cla = 'card-info__detail-area__box__title'
last_page = 55
pagesToCompanys(last_page)

search_result = "IT/Web・通信・インターネット系✖️モバイル/アプリサービス"
ori_url = 'https://www.green-japan.com/search_key/01?key=yfbovw38e6359vh5lm8y&keyword=&page='
tag = 'h3'
cla = 'card-info__detail-area__box__title'
last_page = 52
pagesToCompanys(last_page)

search_result = "IT/Web・通信・インターネット系✖️IoT/M2M/ロボット"
ori_url = 'https://www.green-japan.com/search_key/01?key=78u70qo7lx7z8v0ap5az&keyword=&page='
tag = 'h3'
cla = 'card-info__detail-area__box__title'
last_page = 11
pagesToCompanys(last_page)

search_result = 'AR/VR/MR'
ori_url = 'https://www.green-japan.com/search_key/01?key=dkhxk7j2b78767omrvyo&keyword=&page='
tag = 'h3'
cla = 'card-info__detail-area__box__title'
last_page = 4
pagesToCompanys(last_page)


file_name = 'Greenの企業検索結果'
writeToCsv(companys,file_name)
