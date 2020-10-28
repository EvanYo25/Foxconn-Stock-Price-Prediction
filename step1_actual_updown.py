# coding=utf-8
import csv
import datetime

target_stock = "3008 大立光"	#記得改結尾輸出的檔名

raw16 = open('D:\\譚\\大數據與商業分析\\期中報告\\2016_stock_data.csv','r',encoding = 'ANSI')
raw17 = open('D:\\譚\\大數據與商業分析\\期中報告\\2017_stock_data.csv','r',encoding = 'ANSI')
table16 = csv.reader(raw16)
table17 = csv.reader(raw17)
next(raw16) # 跳過標題列
next(raw17)

data = []
for row in table17:
	data.append(row)
for row in table16:
	data.append(row)	#list 中 list
data.reverse()		# 日期改為順序

target = []	# 第一欄 : datetime / 第二欄 : 股價 / 第三欄 : 漲跌平 (append上去) / 第四欄 : SD值
for row in data:
	if row[0] == target_stock:
		temp = [row[1] , row[2]]
		target.append(temp)	
		
# 處理資料型態 : 日期(string >> datetime)  /  股價(string >> float)
for row in target:
	tempDate = datetime.datetime.strptime(row[0], "%Y/%m/%d")
	row[0] = tempDate.date()
	row[1] = float(row[1])
	
targetList = [target_stock , " "]
titles = ["日期","股價","漲跌平","SD"]
target.insert(0,titles)			#加入標題		row[2]
target.insert(0," ")			#空行			row[1]
target.insert(0,targetList)		#加入公司名		row[0]

for i in range( 4 , len(target) ):	# 從第1天(row[4])開始，因要跟前一天比(第0天(row[3])沒有前一天)
	if target[i][0].weekday() in range(1,5):	# 週二(1)~週五(4)
		nday = 1
	else:	#周一(0)
		nday = 3
		
	# 股價漲跌幅度標準
	if target[i][1] < 10:
		SD = 0.005
	elif target[i][1] < 50:
		SD = 0.01
	elif target[i][1] < 100:
		SD = 0.015
	elif target[i][1] < 200:
		SD = 0.02
	elif target[i][1] < 300:
		SD = 0.025
	elif target[i][1] < 500:
		SD = 0.03
	elif target[i][1] < 1000:
		SD = 0.035
	else: 
		SD = 0.04
	
	if ( (target[i][1] - target[i-nday][1]) / target[i-nday][1] ) <= -SD:
		target[i].append("跌")
	elif ( (target[i][1] - target[i-nday][1]) / target[i-nday][1] ) >= SD:
		target[i].append("漲")
	else:
		target[i].append("平")
	
	target[i].append(SD)
														# 記得改此檔名 
f = open('D:\\譚\\大數據與商業分析\\期中報告\\輸出檔案\\大立光_實際漲跌.csv',"w", newline='')
w = csv.writer(f)
w.writerows(target)
f.close()


