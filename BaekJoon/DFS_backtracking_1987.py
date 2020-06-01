import sys

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def DFS(x, y, ans):
    global answer
    print(x + y + ans)
    answer = max(ans, answer)

    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]

        # index 벗어나지 않는지 체크하고, 새로운 칸이 중복되는 알파벳인지 체크한다
        if ((0 <= nx < R) and (0 <= ny < C)) and (board[nx][ny] not in passed):
            passed.append(board[nx][ny])
            print('append')
            print(passed)
            DFS(nx, ny, ans+1)
            passed.remove(board[nx][ny])
            print('remove')
            print(passed)


R, C = map(int, sys.stdin.readline().split())
board = [list(sys.stdin.readline().strip()) for _ in range(R)]

answer = 1
passed = [board[0][0]]
DFS(0, 0, answer)
print(answer)
