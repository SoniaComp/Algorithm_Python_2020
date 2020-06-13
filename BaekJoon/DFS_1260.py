# N : 정점 갯수, M : 간선 갯수, V : 시작 정점 번호
N, M, V = map(int, input().split())
# 0으로 왼쪽 위쪽을 둘러쌈(인덱스와 번호가 헷갈려서)
matrix = [[0] * (N + 1) for _ in range(N + 1)]

# 간선 갯수로 인접 행렬 만들기
for _ in range(M):
    link = list(map(int, input().split()))
    matrix[link[0]][link[1]] = 1
    matrix[link[1]][link[0]] = 1

# 깊이 우선 탐색(Depth First Search)
# current_node : 시작 정점, row : 인접 행렬, foot_print : 발자취 리스트


def dfs(current_node, row, foot_prints):
    # 발자취 리스트에 쌓기
    foot_prints += [current_node]
    # 인접 행렬의 row에 있는 갯수만큼 for문 돌린다.
    for search_node in range(len(row[current_node])):
        # 인접 행렬에서 1(=True)거나 찾는 노드가 발자취 리스트에 없는 경우
        # if 절이니까 찾으면 바로 넘어감
        if row[current_node][search_node] and search_node not in foot_prints:
            foot_prints = dfs(search_node, row, foot_prints)
    return foot_prints

# 너비 우선 탐색(Breadth First Search)


def bfs(start):
    # 큐 (빨대모양이라고 생각하면 편함)
    queue = [start]
    # 발자취 리스트
    foot_prints = [start]

    # 큐가 공 리스트가 될때까지(할게없을때까지)
    while queue:
        # 큐에서 현재 가장 처음에 들어간거(인덱스 0 인거)를 current_node에 넣는다
        # 큐는 공리스트가 된다.
        current_node = queue.pop(0)
        # 돌면서 끝에 결국 queue가 아무것도 없게 된다.
        for search_node in range(len(matrix[current_node])):
            if matrix[current_node][search_node] and search_node not in foot_prints:
                foot_prints += [search_node]
                queue += [search_node]
    return foot_prints


    # *붙인 이유는 리스트 형태를 풀어주기 위함
print(*dfs(V, matrix, []))
print(*bfs(V))
