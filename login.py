# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

input_id = input("아이디를 입력해주세요.\n")
members = ['egoing', 'k8805', 'leezche']
for member in members:
    if member == input_id:
        print('Hello!, '+member)
        import sys
        sys.exit()#강제종료
print('Who are you?')
