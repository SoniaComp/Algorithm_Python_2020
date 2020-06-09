# 이진 탐색: 오름차순으로 정렬된 리스트에서 특정한 값의 위치를 찾는 알고리즘
# 검색속도가 아주 빠르다.


def bisect(a, x, lo=0, hi=None):
    if lo < 0:
        raise valueError('lo must be non-negative')
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo+hi)//2
        if a[mid] < x:
            lo = mid+1
        else:
            hi = mid
    return lo


mylist = [1, 2, 3, 7, 9, 11, 33]
print(bisect(mylist, 3)) # index 값 알랴줌
