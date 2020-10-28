# coding=utf-8
import csv
import datetime

raw16 = open('D:\\譚\\大數據與商業分析\\期中報告\\2016_stock_data.csv','r',encoding = 'ANSI')
raw17 = open('D:\\譚\\大數據與商業分析\\期中報告\\2017_stock_data.csv','r',encoding = 'ANSI')
table16 = csv.reader(raw16)
table17 = csv.reader(raw17)
next(raw16) # 跳過標題列
next(raw17)

tempData = []
for row in table17:
	tempData.append(row)
for row in table16:
	tempData.append(row)	#list 中 list

counter = 0
DF = 0
stock_name = []
for row in tempData:
	if counter == 1867:
		break
	names = row[0].split()
	temp = [names[1] , DF]
	stock_name.append(temp)
	counter += 1
	
print("stockName setting over")
print()
	
#######################################################################################################
#-----------------------------------------------------------------------------------------------------#	
#######################################################################################################
	
raw_bbs = open('D:\\譚\\大數據與商業分析\\期中報告\\2016_bbs.csv','r',encoding = 'ANSI',errors='ignore')
raw_forum = open('D:\\譚\\大數據與商業分析\\期中報告\\2016_forum.csv','r',encoding = 'ANSI',errors='ignore')
raw_news = open('D:\\譚\\大數據與商業分析\\期中報告\\2016_news.csv','r',encoding = 'ANSI',errors='ignore')
raw_social = open('D:\\譚\\大數據與商業分析\\期中報告\\2017_social.csv','r',encoding = 'ANSI',errors='ignore')

table_bbs = csv.reader(raw_bbs)
table_forum = csv.reader(raw_forum)
table_news = csv.reader(raw_news)
table_social = csv.reader(raw_social)

next(raw_bbs) 
next(raw_forum)
next(raw_news)
next(raw_social)

data = []	# list 中 list
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
	
# counting DF of all stock_name
for rowData in data:	# ID / 看板 / post_time / title / author / content
	for rowStock in stock_name:		# stockName / DF(counter)
		if (rowStock[0] in rowData[3]) or (rowStock[0] in rowData[5]):
			rowStock[1] += 1 

print(stock_name)
print()		

# 找出 DF 最高的前 20 檔股票，完成選股。
top20 = [ ["",0], ["",0], ["",0], ["",0], ["",0], ["",0], ["",0], ["",0], ["",0], ["",0], ["",0], ["",0], ["",0], ["",0], ["",0], ["",0], ["",0], ["",0], ["",0], ["",0] ]
for i in range(len(stock_name)):
	for j in range(20):
		if stock_name[i][1] > top20[j][1]:
			for k in range(19,j,-1):
				top20[k] = top20[k-1]
			top20[j] = stock_name[i]
			break
			
print(top20)		# 
print()
