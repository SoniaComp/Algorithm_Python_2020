# 순열과 조합: combinations, permutations
import itertools

pool = ['A', 'B', 'C']
print(list(map(''.join, itertools.permutations(pool))))  # 3개의 원소로 수열 만들기
print(list(map(''.join, itertools.permutations(pool, 2))))  # 2개의 원소로 수열 만들기

# 원소가 주어진 시퀀스에서 어떻게 쓰이는지
# 가장 많이 등장하는 알파벳 찾기 - Counter
import collections
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 7, 9, 1, 2, 3, 3, 5, 2, 6, 8, 9, 0, 1, 1, 4, 7, 0]
answer = collections.Counter(my_list)

print(answer[1]) # = 4
print(answer[3])  # = 3
print(answer[100]) # = 0
