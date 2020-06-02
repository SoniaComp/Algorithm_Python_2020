def calc(stones, k, mid):  # 건널 수 있는지를 체크 하는 것
    print('-----')
    print(stones)
    print(k)
    print(mid)
    now = 0
    for stone in stones:
        if(stone < mid):  # stone - mid 가 0이면 이번 회엔 건널 수 있다는 것임
            now += 1
            print('now', now)  # 즉 stone < mid 이면 전 사람 건널 때 0이 되어서 못 건너게 됐다는 것.
            # 건너 뛰는 것 값을 + 1 해준다.
        else:   # 연속으로 나온게 아니면 다시 0으로 만들어줌.
            now = 0
            print('now', 0)
        if(now >= k):  # now가 k랑 같거나 커지면 못 건너는 것.
            return False
    return True


def solution(stones, k):
    left = 1  # 최소 1명은 건널 수 있기 때문에
    right = max(stones) + 1  # 최고 값 + 1, 그래야 두개 더해서 // 할 때 내림을 하게 되기 때문에 제대로 됨.
    print('right', right)
    while(left < right - 1):  # 1차이 날 땐 더이상 가운데가 없기 때문에 left쪽이 답/ right에 넣는 mid는 불가능한 값으로 측정 되어있음
        print('-')
        mid = (left + right) // 2  # 중간의 값 정수가 나오게
        print('mid', mid)
        if(calc(stones, k, mid)):  # mid가 가능한지 확인
            left = mid
            print('left', left)
        else:
            right = mid
            print('right', left)
    print('answer', left)
    return left


solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3)
