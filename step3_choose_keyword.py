# coding=utf-8
import csv
from operator import itemgetter				  # 公司名稱  在此改
raw = open('D:\\譚\\大數據與商業分析\\期中報告\\輸出檔案\\台積電_文章漲跌歸類.csv','r',encoding = 'ANSI',errors='ignore')
table = csv.reader(raw)
next(raw)
next(raw)
next(raw)

data = []
for row in table:
	data.append(row)	

up_titles = []
up_docs = []
down_titles = []
down_docs = []
all_titles = []
all_docs = []

counter = 0
for row in data:
	all_titles.append(row[3])
	all_docs.append(row[5])
	counter += 1
	print(counter)

	if row[6] == "漲":
		up_titles.append(row[3])
		up_docs.append(row[4])
	elif row[6] == "跌":
		down_titles.append(row[3])
		down_docs.append(row[4])

def ngram(string,n):
    return [string[i:i+n] for i in range(0,len(string)-n+1)]

print("Data setting over")
print()
	
up_tf = dict()
up_df = dict()
down_tf = dict()
down_df = dict()

#以n gram去做
for n in range(2,7):
	#漲的文章
	for i in range(len(up_titles)):
		# print(n," ",i)
		#儲存切小段的陣列
		up_title = ngram(up_titles[i],n)
		up_doc = ngram(up_docs[i],n)
		up_tmp = dict()

		#數n gram出現次數，先掃過一次關鍵字的標題，EX:包含台積電的文章&標題的標題
		for g in up_title:
			# print(g)
			check = True
			for word in g:
				# 判斷是不是中文字
				if not(u'\u4e00' <= word <= u'\u9fff'):
					check = False
			if check == False:
				continue
			up_tmp[g] =up_tmp.get(g,0)+1
			# print(tmp.get(g,0))

		#數n gram出現次數，再掃文章
		for g in up_doc:
			# print(g)
			check = True
			for word in g:
				if not(u'\u4e00' <= word <= u'\u9fff'):
					check = False
			if check == False:
				continue
			up_tmp[g] =up_tmp.get(g,0)+1
			# print(tmp.get(g,0))

		#tmp存到tf df
		for g in up_tmp:
			#tf要存總共出現次數 df要存出現在幾個文章當中
			up_tf[g] = up_tf.get(g,0)+up_tmp[g]
			up_df[g] = up_df.get(g,0)+1

		#如果tf長度過長
		if len(up_tf)>100000:
			up_sorted_tf = sorted(up_tf.items(),key = lambda x:x[1])
			# print(sorted_tf)
			for i in range(50000):
				up_tf.pop(up_sorted_tf[i][0])
				up_df.pop(up_sorted_tf[i][0])
	
	#跌的文章
	for i in range(len(down_titles)):
		# print(n," ",i)
		#儲存切小段的陣列
		down_title = ngram(down_titles[i],n)
		down_doc = ngram(down_docs[i],n)
		down_tmp = dict()

		#數n gram出現次數，先掃過一次關鍵字的標題，EX:包含台積電的文章&標題的標題
		for g in down_title:
			# print(g)
			check = True
			for word in g:
				# 判斷是不是中文字
				if not(u'\u4e00' <= word <= u'\u9fff'):
					check = False
			if check == False:
				continue
			down_tmp[g] =down_tmp.get(g,0)+1
			# print(tmp.get(g,0))

		#數n gram出現次數，再掃文章
		for g in down_doc:
			# print(g)
			check = True
			for word in g:
				if not(u'\u4e00' <= word <= u'\u9fff'):
					check = False
			if check == False:
				continue
			down_tmp[g] =down_tmp.get(g,0)+1
			# print(tmp.get(g,0))

		#tmp存到tf df
		for g in down_tmp:
			#tf要存總共出現次數 df要存出現在幾個文章當中
			down_tf[g] = down_tf.get(g,0)+down_tmp[g]
			down_df[g] = down_df.get(g,0)+1

		#如果tf長度過長
		if len(down_tf)>100000:
			down_sorted_tf = sorted(down_tf.items(),key = lambda x:x[1])
			# print(sorted_tf)
			for i in range(50000):
				down_tf.pop(down_sorted_tf[i][0])
				down_df.pop(down_sorted_tf[i][0])
				

print("cutting n gram over")
print()
				
# sorted_df = sorted(df.items(),key = lambda x:x[1], reverse = True)
#只取前面的1000筆資料
# sorted_df = sorted_df[0:3000]
# print("========================================")
# print(sorted_df)
# print("========================================a")
# print(len(sorted_df))

# for key in sorted_df:
# 	# print(key)
# 	i = sorted_df.index(key)
# 	j = i + 1
# 	while j < len(sorted_df) and ( ((float)(sorted_df[i][1]) / sorted_df[j][1] < 1.25) ):
# 		#如果前一個包含在後一個裡面則pop掉
# 		if sorted_df[i][0] in sorted_df[j][0]:
# 			tf.pop(sorted_df[i][0])
# 			df.pop(sorted_df[i][0])
# 			break
# 		j = j + 1

up_trash = []
down_trash = []
up_sorted_df = sorted(up_df.items(),key = lambda x:len(x[0]), reverse = True)
down_sorted_df = sorted(down_df.items(),key = lambda x:len(x[0]), reverse = True)
# print(sorted_df)
# print("-------------------------------")
for key in up_sorted_df:
	i = up_sorted_df.index(key)
	if(len(up_sorted_df[i][0])<3):
		break;
	subArr = ngram(up_sorted_df[i][0],len(up_sorted_df[i][0])-1)
	sub1 = up_df.get(subArr[0],0)
	sub2 = up_df.get(subArr[1],0)
	# print(sub1,sub2)
	# print(sorted_df[i][1])
	# print((float)(sub1)/sorted_df[i][1])
	if sub1!=0 and ( ((float)(sub1)/up_sorted_df[i][1]<1.1) or (sub1-up_sorted_df[i][1])<10 ):
		up_trash.append(subArr[0])
	# print((float)(sub2)/sorted_df[i][1])
	if sub2!=0 and ( ((float)(sub2)/up_sorted_df[i][1]<1.1) or (sub2-up_sorted_df[i][1])<10 ):
		up_trash.append(subArr[1])
		
for key in down_sorted_df:
	i = down_sorted_df.index(key)
	if(len(down_sorted_df[i][0])<3):
		break;
	subArr = ngram(down_sorted_df[i][0],len(down_sorted_df[i][0])-1)
	sub1 = down_df.get(subArr[0],0)
	sub2 = down_df.get(subArr[1],0)
	# print(sub1,sub2)
	# print(sorted_df[i][1])
	# print((float)(sub1)/sorted_df[i][1])
	if sub1!=0 and ( ((float)(sub1)/down_sorted_df[i][1]<1.1) or (sub1-down_sorted_df[i][1])<10 ):
		down_trash.append(subArr[0])
	# print((float)(sub2)/sorted_df[i][1])
	if sub2!=0 and ( ((float)(sub2)/down_sorted_df[i][1]<1.1) or (sub2-down_sorted_df[i][1])<10 ):
		down_trash.append(subArr[1])

for i in up_trash:
	#因為有重複的 EX:12345 2345\空白 都挑出2345廢詞
	if(up_tf.get(i,0)):
		up_tf.pop(i)
		up_df.pop(i)
		
for i in down_trash:
	#因為有重複的 EX:12345 2345\空白 都挑出2345廢詞
	if(down_tf.get(i,0)):
		down_tf.pop(i)
		down_df.pop(i)

print("trash throwing over")
print()
		
up_all_tf = dict()
up_all_df = dict()
down_all_tf = dict()
down_all_df = dict()

for n in range(2,7):
	for i in range(len(all_titles)):
		if i%10000==0:
			print(i)
		title = ngram(all_titles[i],n)
		doc = ngram(all_docs[i],n)
		up_tmp = dict()
		down_tmp = dict()

		for g in title:
			if g in up_tf.keys():
				up_tmp[g] = up_tmp.get(g,0)+1
			if g in down_tf.keys():
				down_tmp[g] = down_tmp.get(g,0)+1
				
		for g in up_doc:
			if g in up_tf.keys():
				up_tmp[g] = up_tmp.get(g,0)+1
			if g in down_tf.keys():
				down_tmp[g] = down_tmp.get(g,0)+1
				
		for g in up_tmp:
			up_all_tf[g] = up_all_tf.get(g,0)+ up_tmp[g]
			up_all_df[g] = up_all_df.get(g,0)+1
			
		for g in down_tmp:
			down_all_tf[g] = down_all_tf.get(g,0)+ down_tmp[g]
			down_all_df[g] = down_all_df.get(g,0)+1

print("all_tf、all_df setting over")
print()
			
up_sorted_tf = sorted(up_tf.items(),key = lambda x:x[1], reverse = True)
down_sorted_tf = sorted(down_tf.items(),key = lambda x:x[1], reverse = True)

up_output = []
up_output.append([len(up_docs),'doc'])
up_output.append(['編號','詞','TF','DF','全部TF','全部DF'])

down_output = []
down_output.append([len(down_docs),'doc'])
down_output.append(['編號','詞','TF','DF','全部TF','全部DF'])

up_it = 1
for i in up_sorted_tf:
	if i[1]<50:
		break
	up_output.append( [ up_it,i[0] , up_tf.get(i[0]) , up_df.get(i[0]) , up_all_tf.get(i[0]) , up_all_df.get(i[0]) ] )
	up_it = up_it+1

down_it = 1
for i in down_sorted_tf:
	if i[1]<50:
		break
	down_output.append( [ down_it , i[0] , down_tf.get(i[0]) , down_df.get(i[0]) , down_all_tf.get(i[0]) , down_all_df.get(i[0]) ] )
	down_it = down_it+1
		
		# 公司名稱  在此改
up_f = open('D:\\譚\\大數據與商業分析\\期中報告\\輸出檔案\\台積電_漲2_6_gram.csv',"w", newline='',errors='ignore')
up_w = csv.writer(up_f)
up_w.writerows(up_output)
up_f.close()
		
		# 公司名稱  在此改
down_f = open('D:\\譚\\大數據與商業分析\\期中報告\\輸出檔案\\台積電_跌2_6_gram.csv',"w", newline='',errors='ignore')
down_w = csv.writer(down_f)
down_w.writerows(down_output)
down_f.close()