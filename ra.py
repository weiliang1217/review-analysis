data = []
count = 0
with open ('reviews.txt', 'r') as file: # 開啟某個檔案並讀取內容，使用with open ('file_name.type', 'r') as ___
	for line in file: # 透過.append函式將line內容 for loop填寫至data清單中
		data.append(line)
		count += 1
		if count % 10000 == 0:
			print(len(data))
sum_len = 0 # 預計從第0則留言開始計算 字數/留言
for word in data:
	sum_len += len(word) #sum_len = sum_len + 1
print(sum_len) # 確認 +=是否有確實執行
avg = sum_len/ len(data) # 定義avg
print(avg)
