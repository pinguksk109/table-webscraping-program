import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup

def table_to_csv(file_path, url, selecter):
	html = urlopen(url)
	soup = BeautifulSoup(html, "html.parser")

	#セレクタ
	table = soup.findAll("table", selecter)[0]

	trs = table.findAll("tr")
	#ファイルオープン
	csv_file = open("income2009.csv", "wt", newline='', encoding="utf-8")
	csv_write = csv.writer(csv_file)

	for tr in trs:
		csv_data = []
		#1行ごとにtd,tr要素のデータを取得してCSVに書き込み
		for cell in tr.findAll(['td', 'th']):
			#csv_headerに抜き出したデータを格納
			csv_data.append(cell.get_text()
url = "https://www.nenshuu.net/prefecture/shotoku/in_shotoku_city_past.php?nen=2009"

#セレクタ
selecter = {"id":"table_ranking"}

#指定したURL・セレクタの表のデータをCSVに保存
table_to_csv("test.csv", url, selecter)