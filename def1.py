# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
def cal(num1,num2,op):
	ans = 0
	if op == '+': ans = num1 + num2
	elif op == '-': ans = num1 - num2
	elif op == '*': ans = num1 * num2
	elif op == '/': ans = num1 / num2
	
	show(num1,num2,op,ans)
	
def numinput():
	data = int(input('숫자를 입력하세요.'))
	return data

def strinput(msg):
	data = input(msg)
	return data

def show(num1,num2,op,ans):
	print(f'{num1} {op} {num2} = {ans}')
	
if __name__=='__main__':#이부분 __ 시험!!!!!!!
	num1 = numinput()
	num2 = numinput()
	op = strinput('연산자를 입력하세요.')
	cal(num1,num2,op)
