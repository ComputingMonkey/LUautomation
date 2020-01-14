#-*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import pandas as pd

#データをcsvに書き込む
def writeToCsv(data):
    df = pd.DataFrame(data)
    # CSV ファイル (employee.csv) として出力
    df.to_csv("search1.csv")

#サイト(num)ページ目の会社を取得(companysに詰め込む)
def getCompanys(ori_url, num, tag, cla):
  # ori_url = 'https://doda.jp/DodaFront/View/JobSearchList.action?so=50&tp=1&pic=1&ind=11L&es=2&ds=0&pr=13&page='
  num = str(num)
  html_doc = requests.get(ori_url + num).text
  soup = BeautifulSoup(html_doc, 'html.parser') # BeautifulSoupの初期化
  blocks = soup.find_all(tag, class_=cla)
  # print(companys)
  for block in blocks:
    company = block.string
    companys.append(company)
  companys.append('finished scraping')

#num回スクレイピングを繰り返す
def pagesToCompanys(num):
    for i in range(num):
      getCompanys(ori_url, num, tag, cla)
      percent = 100 * (i / num)
      print(str(percent) + '％完了')
