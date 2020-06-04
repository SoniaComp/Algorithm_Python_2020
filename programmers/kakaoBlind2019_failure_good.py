def solution(N, stages):
    result = {}
    num = len(stages)

    for stage in range(1, N+1):  # N+1은 포함안된다.
        if num != 0:  # 예외처리
            count = stages.count(stage)  # 여기서는 count함수를 이용
            result[stage] = count/num
            num -= count
        else:
            result[stage] = 0

    return sorted(result, key=lambda x:result[x], reverse=True)
print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
