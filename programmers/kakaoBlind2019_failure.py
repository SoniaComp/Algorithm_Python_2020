## 예외 처리 (0일 때)
## 번호와 묶어서 실패율 정렬

def solution(N, stages):
    answer = []
    failureRate = {}
    idx = 1
    allNum = len(stages)
    notNum = 0
    for i in sorted(stages):
        if(idx == N+1):
            break
        if(i == idx):
            notNum += 1
        else:
            failureRate[idx] = notNum / allNum
            allNum -= notNum
            notNum = 0
            idx += 1

    return answer

solution(4, [2, 1, 2, 6, 2, 4, 3, 3])
