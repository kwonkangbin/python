evennumbers = [2,4,5,8]
oddrunbers = [1,3,5,7]
evennumbers.append(10)#마지막 요소에 10 추가
print(evennumbers)

evennumbers.insert(0,0)
print(evennumbers)

evennumbers.extend(oddrunbers)#리스트만 인자로 전달 리스트 두개 합치기
print(evennumbers)
evennumbers.sort()#오름차순
print(evennumbers)
evennumbers.reverse()
print(evennumbers)

evennumbers.insert(3,[11,12,13])
print(evennumbers)

evennumbers.remove(3)#제일 첫번째 3삭제
print(evennumbers)
print(evennumbers.pop())
print(evennumbers)

print(evennumbers.index(4))#4가 있는 인덱스 숫자
print(evennumbers)
print(evennumbers.count(4))#4가 몇개있는지 확인
print(len(evennumbers))


