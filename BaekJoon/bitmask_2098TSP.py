import sys
input = sys.stdin.readline

n = int(input())
# 간선의 weight 표시
adj = [list(map(int, input().split())) for i in range(n)]
# 비트마스크로 n개의 1표시
cpl = (1 << n)-1
# 가장 큰 수
INF = 1 << 30

ans = INF
start = 0
DP = [[0]*(1 << n) for _ in range(n)]
# 다이나믹프로그래밍1: 각 단계의 최적해를 별도의 배열에 저장해둡니다.
# 다이나믹프로그래밍2: 별도의 재귀 함수를 이용해 이 선택을 따라가며 각 선택지를 저장하거나 출력


def solve(cur, visited):
    # 종료조건: 모두 방문했을 때
    if visited == cpl:  # 맨 마지막
        return adj[cur][start]
    if DP[cur][visited]:  # 메모이제이션
        return DP[cur][visited]
    ans = INF
    for i in range(n):
        if adj[cur][i] and not visited & (1 << i):
            # visited &(1<<i): 1<<i 가 존재하는지
            ans = min(ans, solve(i, visited | (1 << i))+adj[cur][i])
            # visited |(1<<i): 1<<i를 visited에 추가
    DP[cur][visited] = ans  # 현재 노드에서 출발해서 모든 노드 방문했을 때
    return ans


ans = min(ans, solve(start, 1 << start))
print(ans)
