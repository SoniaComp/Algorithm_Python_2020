import heapq
import sys
input = sys.stdin.readline()


def bfs(v):
    q = []
    visited = [[False] * M for _ in range(N)]
    visited[v[0]][v[1]] = True
    heapq.heappush(q, [0, v])

    while q:
        v = heapq.heappop(q)
        for a in range(4):
            i = v[1][0] + di[a]
            j = v[1][1] + dj[a]
            if i == N-1 and j == M-1:
                print(v[0])
                return
            if 0 <= i < N and 0 <= j < M and not visited[i][j]:
                visited[i][j] = True
                heapq.heappush(q, v[0]+1 
                if maze[i][j]== '1' else v[0], [i, j])
