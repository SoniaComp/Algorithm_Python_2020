import sys
input = sys.stdin.readline

n = int(input())
a = [[list(map(int, input().split()))] for _ in range(n)]
# visited = [[list(0 in range(N))] for _ in range(N)]
# 이미 간 것을 0으로 하는 방법

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
count = 0
apt = []


def dfs(matrix, cnt, x, y):
    area[x][y] = 0
    cnt += 1
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if nx < 0 or nx>= n or ny<0 or ny>= n:
          continue
        if a[nx][ny] == '1':
          dfs(nx, ny)


for i in range(n):
  for j in range(n):
    if a[i][j] == '1':
      cnt = 0
      dfs(i, j)
      apt.append(cnt)


print(len(apt))
apt.sort()
for i in apt:
  print(i)
