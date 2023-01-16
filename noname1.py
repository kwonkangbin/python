# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

def cal(a, op, b):
	if op == '+': print(f"{a} {op} {b} = {a + b}")
	elif op == '-': print(f"{a} {op} {b} = {a - b}")
	elif op == '*': print(f"{a} {op} {b} = {a * b}")
	elif op == '/': print(f"{a} {op} {b} = {a / b}")

	
a = input().split(" ")#시험!!!
x = int(a[0])
op = a[1]
y = eval(a[2])
cal(x, op, y)
