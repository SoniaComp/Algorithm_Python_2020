# 곱집합 구하기
# 두 스트링 'ABCD', 'xy' 의 곱집합은 Ax Ay Bx By Cx Cy Dx Dy 입니다.

import numpy as np
import operator
from functools import reduce
import itertools

iterable1 = 'ABCD'
iterable2 = 'xy'
iterable3 = '1234'
itertools.product(iterable1, iterable2, iterable3)

# 2차원 리스트를 1차원 리스트로 만들기

my_list = [[1, 2], [3, 4], [5, 6]]

# 방법 1 - sum 함수
answer = sum(my_list, [])

# 방법4 - list comprehension 이용
[element for array in my_list for element in array]

###########
# itertools 사용

# 방법 2 - itertools.chain
list(itertools.chain.from_iterable(my_list))

# 방법 3 - itertools와 unpacking
list(itertools.chain(*my_list))

##################
# reduce 함수 이용 1
list(reduce(lambda x, y: x+y, my_list))

# reduce 함수 이용2
list(reduce(operator.add, my_list))

##########
# numpy
np.array(my_list).flatten().tolist()