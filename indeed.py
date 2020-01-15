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
  url = ori_url + str(num) + '0'
  r = requests.get(url)
  soup = BeautifulSoup(r.content, 'html.parser')
  # html_doc = requests.get(ori_url + num).text
  # soup = BeautifulSoup(html_doc, 'html.parser') # BeautifulSoupの初期化
  for span in soup.find_all('span', class_='company'):
      if span != '' and span != None:
        # companys.append(span.string)
        # company = span.string.strip('\n')
        # companys.append(company)
        print(span.string)
#num回スクレイピングを繰り返す
def pagesToCompanys(num, search_result):
    for i in range(num):
      if i == 0:
        companys.append('')
        companys.append('【' + search_result + '】')
      getCompanys(ori_url, i, search_result)
      percent = 100 * (i / num)
      print(str(percent) + '％')
      if i == num - 1:
          print('100.0％')
          print(search_result + ':完了')
          print('合計' + str(len(companys)) + '企業取得しました')

#ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー
companys = []

# search_result = "IT✖️ソフトウェア"
# ori_url = 'https://jp.indeed.com/%E6%B1%82%E4%BA%BA?q=title%3AIT%E3%80%81%E3%82%BD%E3%83%95%E3%83%88%E3%82%A6%E3%82%A7%E3%82%A2&l=%E6%9D%B1%E4%BA%AC%E9%83%BD&radius=0&start='
# pagesToCompanys(52, search_result)
#
# search_result = "IT✖️アプリ"
# ori_url = 'https://jp.indeed.com/jobs?q=title%3AIT%E3%80%81%E3%82%A2%E3%83%97%E3%83%AA&l=%E6%9D%B1%E4%BA%AC%E9%83%BD&radius=0&start='
# pagesToCompanys(22, search_result)

search_result = "IT✖️IoT"
ori_url = 'https://jp.indeed.com/jobs?q=title%3AIT%E3%80%81IoT&l=%E6%9D%B1%E4%BA%AC%E9%83%BD&radius=0&start='
pagesToCompanys(4, search_result)

# search_result = "IT✖️Webエンジニア"
# ori_url = 'https://jp.indeed.com/jobs?q=title%3AIT%E3%80%81WEB%E3%82%A8%E3%83%B3%E3%82%B8%E3%83%8B%E3%82%A2&l=%E6%9D%B1%E4%BA%AC%E9%83%BD&radius=0&start='
# pagesToCompanys(50, search_result)

file_name = 'indeedの企業検索結果'
file_name = 'test'
writeToCsv(companys,file_name)
