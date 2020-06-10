# BFS는 최단거리를 찾자마자 종료할 수 있고,
# DFS는 모든 거리를 다 찾아야 함

from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
maze = [list(input().strip()) for _ in range(N)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

q = deque()
maxCount = 0


def bfs(x, y):
    cnt = 0
    q.append([x, y])
    c = [[0]*M for _ in range(N)]
    c[x][y] = 1
    maxN = 0
    while q:
        [x, y] = q.popleft()
        for i in range(4):
            Nx, Ny = x+dx[i], y+dy[i]
            if 0 < Nx < N and 0 < Ny < M and maze[Nx][Ny] == 'L':
                q.append([Nx, Ny])
                maze[Nx][Ny] = 'W'
                c[Nx][Ny] = c[x][y]+1
                maxN = max(c[Nx][Ny], maxN)
    return maxN - 1


for i in range(N):
    for j in range(M):
        if maze[i][j] == 'L':
            maxCount = (maxCount, bfs(i, j))

print(maxCount)
