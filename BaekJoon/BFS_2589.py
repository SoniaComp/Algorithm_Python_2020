import sys
input = sys.stdin.readline

N, M = map(int, input().split())
maze = [list(input().strip()) for _ in range(N)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

maxcount = 0


def dfs(x, y, count):
    global maxcount
    for i in range(4):
        if x+dx[i] > N-1 or x+dx[i] < 0 or y+dy[i] < 0 or y+dy[i] > M-1:
            continue
        if(maze[x+dx[i]][y+dy[i]] == 'L'):
            maze[x+dx[i]][y+dy[i]] = 'W'
            count += 1
            if(count > maxcount):
                maxcount = count
            dfs(x+dx[i], y+dy[i], count)
        else:
            continue
    return count


dfs(0, 0, 0)
print(maxcount)
