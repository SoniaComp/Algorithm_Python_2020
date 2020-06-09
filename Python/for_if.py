#for 과 if 문을 한번에
# 파이썬의 list comprehension을 사용하면 한 줄 안에 for 문과 if 문을 한 번에 처리할 수 있습니다.

mylist = [3, 2, 6, 7]
answer = [ i**2 for i in mylist if i %2 == 0]
# list comprehension의 syntax는 Displays for lists, sets and dictionaries 에서 확인하실 수 있습니다. 1
