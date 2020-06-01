import sys
from collections import deque, defaultdict
r, c = map(int, sys.stdin.readline().split())
maps = []
for _ in range(r):
    maps.append(list(map(int, sys.stdin.readline().split())))


def bfs(start, maps, visited):
    ice = defaultdict(int)
    queue = deque()
    queue.append(start)
    dirs = [(0, 1), (0, -1), (-1, 0), (1, 0)]
    while queue:
        y, x = queue.popleft()
        visited[y][x] = 1
        for dy, dx in dirs:
            ny, nx = y+dy, x+dx
            if 0 <= ny < len(maps) and 0 <= nx < len(maps[0]):
                # 주변이 바다인 경우. 근처의 0 개수를 더해준다
                if maps[ny][nx] == 0:
                    ice[(y, x)] += 1
                # 주변이 빙산인 경우
                elif maps[ny][nx] != 0 and not visited[ny][nx]:
                    visited[ny][nx] = 1
                    queue.append((ny, nx))
    return ice


def solution(r, c, maps):
    time = 0
    while True:
        visited = [[0 for _ in range(c)] for _ in range(r)]
        continent = 0
        for y in range(r):
            for x in range(c):
                # 빙산인 경우
                if maps[y][x] != 0 and not visited[y][x]:
                    # 빙산 좌표별로 근처 0의 개수를 저장한 dictionary를 얻는다
                    ice = bfs((y, x), maps, visited)
                    continent += 1
        # 빙산이 2개 이상인 경우
        if continent > 1:
            return time
        # 빙산이 사라진 경우
        if continent == 0:
            return 0
        # 빙산 좌표별로 0 개수에 맞게 값을 바꿔준다.
        for (y, x), cnt in ice.items():
            maps[y][x] = 0 if maps[y][x] < cnt else maps[y][x] - cnt
        time += 1


print(solution(r, c, maps))
