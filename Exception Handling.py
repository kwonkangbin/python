try:
	print("나누기 전용 계산기입니다")
	nums = []
	nums.append(input("첫 번째 숫자를 입력하세요 : "))
	nums.append(input("두 번째 숫자를 입력하세요 : "))
	nums.append(int(nums[0]/nums[1])/nums[2])
	print(f"{nums[0]}/{nums[1]}/{nums[2]}")
except ValueError:
	print("에러, 잘못된 값 입력")
except ZeroDivisionError as err:
	print(err)
except Exception as err:
	print("에러, 잘못된 값 입력")
	print(err)
	
	#레이즈문 시험!!!!!!!!!!
	
		
