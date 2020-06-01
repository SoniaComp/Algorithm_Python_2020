import sys

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def BFS(x, y):
    global answer
    # 전역 변수 이용
    q = set([(x, y, board[x][y])])

    while q:
        print('q=')
        print(q)
        x, y, ans = q.pop()
        print(x, y, ans)
        for i in range(4):
            # 좌우 상하 갈 수 있는지 호ㅘㄱ인
            nx = x+dx[i]
            ny = y+dy[i]
            # 칼럼을 벗어나지 않고, ans 겹치는 알파벳 없는지 체크
            if((0 <= nx < R)and (0 <= ny < C) and(board[nx][ny] not in ans)):
                q.add((nx, ny, ans + board[nx][ny]))
                print('q.add=')
                print(q)
                answer = max(answer, len(ans)+1)


# 먼저 R, C 행,열 값 입력받음
R, C = map(int, sys.stdin.readline().split())
board = [list(sys.stdin.readline().strip()) for _ in range(R)]
# strip은 공백 삭제!

answer = 1
BFS(0, 0)

print(answer)
