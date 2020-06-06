import sys
from collections import deque
input = sys.stdin.readline

m, n = map(int, input().split())
a = [list(map(int, list(input().split()))) for _ in range(n)]
# [list(sys.stdin.readline().strip()) for _ in range(R)]
# strip은 문자열에 사용
d = [[0]*m for _ in range(n)]
dx = (-1, 0, 1, 0)
dy = (0, 1, 0, -1)


def bfs():
    dq = deque()
    # 데크
    # 앞과 뒤에서 양방향에서 데이터 처리 가능
    # https://excelsior-cjh.tistory.com/96
    dq.append((0, 0))
    a[0][0] = -1  # 이미 지나간 곳 표시
    while dq:
        x, y = dq.pop()
        for i in range(4):  # 0, 1, 2, 3
            nx, ny = x+dx[i], y+dy[i]  # 갈수 있는 후보군들
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue  # 범위 벗어남
            if a[nx][ny] == -1:  # 이미 지남
                continue
            elif a[nx][ny] == 0:  # 길이 뚫려 있음
                print('----')
                d[nx][ny] = d[x][y] # 뿌실 필요 없음
                print(d)
                dq.append((nx, ny))
                print(dq)
            else:  # 길이 막혀있음
                print('----')
                d[nx][ny] = d[x][y] + 1 # 하나 더 뿌심
                print(d)
                dq.appendleft((nx, ny))
                print(dq)
            a[nx][ny] = -1
    return d[n-1][m-1]


print(bfs())
