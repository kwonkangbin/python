#시험 엑스








from google.colab import drive
drive.mount('/content/gdrive/')
 
fp = open('/지역평균기온 .txt','r',encoding='utf-8')
data = fp.read()
fp.close()

fp = open('/지역평균기온 .txt','r',encoding='utf-8')
data2 = fp.read()
fp.close()

data = fp.read()
data
data2 = fp.readlines()
data2

dt = {}
for line in data : 
		line = line.replace('\n','')
		itemes = line.split(',')
		dt[item[0]]=int(item[1])
  print(type(dt))
  print(dt)
