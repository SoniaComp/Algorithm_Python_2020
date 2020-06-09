# sequence: int 타입 인덱스를 통해, 원소를 접근할 수 있는 iterable입니다.
# join: sequence 멤버를 하나로 이어붙이기
my_list = ['1', '100', '33']
answer = ''.join(my_list)

n = 3
answer = 'abc'*n  # 'abcabcabc'

n = 2
answer = [123, 456]*n  # [123,456,123,456]
