data = []
count = 0
with open ('reviews.txt', 'r') as file: # 開啟某個檔案並讀取內容，使用with open ('file_name.type', 'r') as ___
	for line in file: # 透過.append函式將line內容 for loop填寫至data清單中
		data.append(line)
		count += 1
		if count % 10000 == 0:
			print(len(data))
print(len(data))
print(data[0])


