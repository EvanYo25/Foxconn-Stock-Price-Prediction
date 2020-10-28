# coding=utf-8
import csv
import datetime

target_stock = "台積電"	#記得改結尾輸出的檔名
n = 3	# D+n 的 n 天後

raw_bbs = open('D:\\譚\\大數據與商業分析\\期中報告\\2016_bbs.csv','r',encoding = 'ANSI',errors='ignore')
raw_forum = open('D:\\譚\\大數據與商業分析\\期中報告\\2016_forum.csv','r',encoding = 'ANSI',errors='ignore')
raw_news = open('D:\\譚\\大數據與商業分析\\期中報告\\2016_news.csv','r',encoding = 'ANSI',errors='ignore')
raw_social = open('D:\\譚\\大數據與商業分析\\期中報告\\2017_social.csv','r',encoding = 'ANSI',errors='ignore')
																# 每檔股票名字要改
raw_actual = open('D:\\譚\\大數據與商業分析\\期中報告\\輸出檔案\\台積電_實際漲跌.csv','r',encoding = 'ANSI',errors='ignore')

table_bbs = csv.reader(raw_bbs)
table_forum = csv.reader(raw_forum)
table_news = csv.reader(raw_news)
table_social = csv.reader(raw_social)
table_actual = csv.reader(raw_actual)

next(raw_bbs) 
next(raw_forum)
next(raw_news)
next(raw_social )
next(raw_actual)
next(raw_actual)
next(raw_actual)
next(raw_actual)

plus = datetime.timedelta(days = 0, seconds = 60*60*13 + 60*30)
actual_ref = []		# 實際漲跌，用來參照
for row in table_actual:
	tempTime = datetime.datetime.strptime(row[0], "%Y-%m-%d")
	row[0] = tempTime + plus	# 時間皆初始化為 13:30
	actual_ref.append(row)		# 0 datetime / 1 stockPrice / 2 漲跌平 / 3 SD

data = []
for row in table_bbs:
	temp = []
	row[5] = datetime.datetime.strptime(row[5], "%Y-%m-%d %H:%M:%S")
	temp.append(row[1])		# 	0	ID
	temp.append(row[4])		# 	1	看板
	temp.append(row[5])		# 	2	post_time
	temp.append(row[9])		# 	3	title
	temp.append(row[10])	# 	4	author
	temp.append(row[11])	# 	5	content
	data.append(temp)
for row in table_forum:
	temp = []
	row[5] = datetime.datetime.strptime(row[5], "%Y-%m-%d %H:%M:%S")
	temp.append(row[1])		# 	0	ID
	temp.append(row[4])		# 	1	看板
	temp.append(row[5])		# 	2	post_time
	temp.append(row[9])		# 	3	title
	temp.append(row[10])	# 	4	author
	temp.append(row[11])	# 	5	content
	data.append(temp)
for row in table_news:
	temp = []
	row[5] = datetime.datetime.strptime(row[5], "%Y-%m-%d %H:%M:%S")
	temp.append(row[1])		# 	0	ID
	temp.append(row[4])		# 	1	看板
	temp.append(row[5])		# 	2	post_time
	temp.append(row[9])		# 	3	title
	temp.append(row[10])	# 	4	author
	temp.append(row[11])	# 	5	content
	data.append(temp)
for row in table_social:
	temp = []
	row[11] = datetime.datetime.strptime(row[11], "%Y-%m-%d %H:%M:%S")
	temp.append(row[1])		# 	0	ID
	temp.append(row[6])		# 	1	看板
	temp.append(row[11])	# 	2	post_time
	temp.append(row[12])	# 	3	title
	temp.append(row[13])	# 	4	author
	temp.append(row[14])	# 	5	content
	data.append(temp)

print("Data setting over")
print()

'''
print(data[140355][2], "type =", type(data[140355][2]) )
print(actual_ref[220][0],"type =", type(actual_ref[220][0]) )
print("bool :",data[140355][2] > actual_ref[220][0], "diff :",actual_ref[220][0] - data[140355][2])
'''
						# D + n 天，的n在此決定 (若 n = 1，則週五13:30~週日13:30的文章用不到，因此先定 n = 3
diff1 = datetime.timedelta(days = n, seconds = 0)
# 一篇一篇doc分類(看漲 / 看跌 文章)
for i in range(len(data)):
	found = False
	
	for row in actual_ref:	# 0 datetime / 1 stockPrice / 2 漲跌平 / 3 SD
		t1 = ( data[i][2] + diff1).time()
		sec = t1.hour * 3600 + t1.minute * 60 + t1.second
		dif = datetime.timedelta(days = 0, seconds = sec)
		DplusN_morning = (data[i][2] + diff1) - dif # 文章的D+n天後，調到早上00:00:00，這樣當天中午有股價的話才不會被跳過
		
		if DplusN_morning < row[0] :#找到這篇doc歸類在哪天，並記錄該天是漲或跌(13:30整的不算"當天文章"，算"隔天文章")
			data[i].append(row[2])	# 加上 "漲跌平" 這欄
			found = True
			break
			# data[] 變成 : 0 ID / 1 看板 / 2 post_time / 3 title / 4 author / 5 content / 6 漲跌平
	if found == False:
		data[i].append("超出期間") # 還是要append東西，以防 step 3 跑時 list out of range
			
# 加上輸出csv檔所需的標題			
titles = ["ID","看板","post_time","title","author","content","漲跌平分類"]
targetList = [target_stock , " "]
data.insert(0,titles)			#加入標題		row[2]
data.insert(0," ")				#空行			row[1]
data.insert(0,targetList)		#加入公司名		row[0]

												# 記得改此檔名 
f = open('D:\\譚\\大數據與商業分析\\期中報告\\輸出檔案\\台積電_文章漲跌歸類.csv',"w", newline='',errors='ignore')
w = csv.writer(f)
w.writerows(data)
f.close()