# EOF를 만날때까지, 파일 읽기를 반복합니다,
f = open('myfile.txt', 'r')
while True:
    line = f.readline()
    if not line:
        break
    raw = line.split()
    print(raw)
f.close()

# 파이썬의 with-as 구문을 이용하려면
# 코드를 더 간결하게
# 1_ 파일을 close하지 않아도 됨
# 2_ readlines가 EOF까지만 읽으므로, while문안에서 EOF체크할 필요
with open('myfile.txt') as file:
    for line in file.readlines():
        print(line.strip().split('\t'))
