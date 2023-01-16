def profile(name,age,*language): 
	print("이름 : {}\t나이 : {}\t".format(name,age),end=" ") 
	#여기에 0,1 변수 쓰는 법 (바로 뒤에 있다)
	for lang in language: 
		print(lang,end=" ") 
	print() 

profile("유재석",20,"Python","Java","C","C++","C#") 
profile("김태호",25,"kotlin", "Swift")
