#-*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import pandas as pd
import re

#データをcsvに書き込む
def writeToCsv(data, file_name):
    df = pd.DataFrame(data)
    # CSV ファイル (employee.csv) として出力
    df.to_csv(file_name + ".csv")
    print(file_name + 'でcsv保存を完了しました')
#サイト(num)ページ目の会社を取得(companysに詰め込む)=>pagesToCompanys
def getCompanys(ori_url, num, search_result):
  idx = ori_url.rfind(r'?')
  url = ori_url[:idx] + 'p' + str(num) + '/' + ori_url[idx:]
  # print(url)
  r = requests.get(url)
  soup = BeautifulSoup(r.content, 'html.parser')
  # html_doc = requests.get(ori_url + num).text
  # soup = BeautifulSoup(html_doc, 'html.parser') # BeautifulSoupの初期化
  for p in soup.find_all('p', class_='company size-14px'):
      companys.append(p.find('span').string)
#num回スクレイピングを繰り返す
def pagesToCompanys(num, search_result):
    for i in range(1, num + 1):
      if i == 1:
        companys.append('')
        companys.append('【' + search_result + '】')
      getCompanys(ori_url, i, search_result)
      percent = 100 * (i / num)
      print(str(percent) + '％')
      if i == num:
          print(search_result + ':完了')
          print('合計' + str(len(companys)) + '企業取得しました')

#ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー
companys = []
search_result = "IT✖️システムエンジニア"
ori_url = 'https://type.jp/job-1/1001/area3-tokyo/?pathway=37'
pagesToCompanys(23, search_result)

search_result = "IT✖️アプリケーションエンジニア"
ori_url = 'https://type.jp/job-1/1002/area3-tokyo/?pathway=37'
pagesToCompanys(7, search_result)

search_result = "IT✖️プログラマー"
ori_url = 'https://type.jp/job-1/1003/area3-tokyo/?pathway=37'
pagesToCompanys(12, search_result)

search_result = "IT✖️データベース・サーバ・ネットワークエンジニア"
ori_url = 'https://type.jp/job-1/1004/area3-tokyo/?pathway=37'
pagesToCompanys(12, search_result)

search_result = "IT✖️通信インフラ系エンジニア"
ori_url = 'https://type.jp/job-1/1007/area3-tokyo/?pathway=37'
pagesToCompanys(1, search_result)

search_result = "IT✖️社内SE、テスター、その他"
ori_url = 'https://type.jp/job-1/1006/area3-tokyo/?pathway=37'
pagesToCompanys(3, search_result)



file_name = 'typeの企業検索結果'
writeToCsv(companys,file_name)
