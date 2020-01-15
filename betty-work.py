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
  # ori_url = 'https://doda.jp/DodaFront/View/JobSearchList.action?so=50&tp=1&pic=1&ind=11L&es=2&ds=0&pr=13&page='
  ori_url += '?page='
  html_doc = requests.get(ori_url + str(num)).text
  soup = BeautifulSoup(html_doc, 'html.parser') # BeautifulSoupの初期化
  for company in soup.find_all('td', text =re.compile('株式会社')):
      companys.append(company.string)
#num回スクレイピングを繰り返す
def pagesToCompanys(num, search_result):

    for i in range(num + 1):
      if i == 0:
        companys.append('')
        companys.append('【' + search_result + '】')
      getCompanys(ori_url, i + 1, search_result)
      percent = 100 * (i / num)
      print(str(percent) + '％')
      if i == num:
          print(search_result + ':完了')
          print('合計' + str(len(companys)) + '企業取得しました')

#ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー
companys = []
search_result = "IT✖️ソフトウェア設計・開発"
ori_url = 'https://betty-work.jp/zenkoku/PC13/MC1'
pagesToCompanys(76, search_result)
search_result = "IT✖️インフラ設計・構築"
ori_url = 'https://betty-work.jp/zenkoku/PC13/MC2'
pagesToCompanys(14, search_result)

search_result = "IT✖️HTMLコーダー・フロントエンドエンジニア"
ori_url = 'https://betty-work.jp/zenkoku/PC13/MC6'
pagesToCompanys(1, search_result)

search_result = "IT✖️データ分析・マーケティング"
ori_url = 'https://betty-work.jp/zenkoku/PC13/MC7'
pagesToCompanys(1, search_result)

file_name = 'betty-workの企業検索結果'
writeToCsv(companys,file_name)
