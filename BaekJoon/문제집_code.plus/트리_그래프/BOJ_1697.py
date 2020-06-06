# 리스트(List)를 큐로 사용하면 절대 안됩니다. 큐는 반드시 collections.deque를 써야 합니다.
# queue.Queue는 멀티스레딩을 위해 만들어진 큐이고 매우 느립니다.

from collections import deque


def bfs():
    q = deque()
    q.append(N)
    while q:
        v = q.popleft()
        if v == K:  # 만나기까지 시간
            print(time[v])
            return
        for next_step in (v-1, v+1, v*2):
            if 0 <= next_step < MAX and not time[next_step]:
                time[next_step] = time[v]+1  # 거기까지 도달하한 시간
                q.append(next_step)


MAX = 100001
N, K = map(int, input().split())
time = [0]*MAX
bfs()
