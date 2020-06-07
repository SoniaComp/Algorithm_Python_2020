# 몫과 나머지
# 파이썬의 divmod와 unpacking을 이용하면 다음과 같이 코드를 짤 수 있습니다.
a = 7
b = 5
print(*divmod(a, b))  # 1,2
print(divmod(a, b))  # (1, 2)
# divmod는 작은 숫자를 다룰 때는 a//b, a%b 보다 느립니다. 대신, 큰 숫자를 다룰 때는 전자가 후자보다 더 빠르지요.

# Packing
# 이런 경우처럼 함수가 받을 인자의 갯수를 유연하게 지정할 수 있다면 보다 유연하게 코드를 작성할 수 있습니다.
# 파이썬은 이런 경우를 지원하기 위해 packing을 지원합니다.
# 패킹은 인자로 받은 여러개의 값을 하나의 객체로 합쳐서 받을 수 있도록 합니다.
# 위치인자 패킹은 *한개를 매개변수 앞에 붙임으로 사용합니다.


def func(*args):
      print(args)  # (1, 2, 3, 4, 5, 6, 'a', 'b')
      print(type(args))  # <class 'tuple'>
# 이런식으로 매개변수 이름 앞에 *을 붙여준다면, 위치인자로 보낸 모든 객체들을 하나의 객체로 관리해줍니다.
# 위치인자가 패킹하는 매개변수를 만나면 그 이후에 위치인자가 몇개이던지, tuple로 하나의 객체가되어서 관리됩니다.

# 동일하게 키워드 인자에 패킹은 **을 통해 작성할 수 있습니다.


def kwpacking(**kwargs):
     print(kwargs)  # {'a': 1, 'b': 2, 'c': 3}
     print(type(kwargs)  # <class 'dict'>

# Unpacking
# 함수에서 unpacking을 할때는, 매개변수에서 *을 붙이는게 아니라 인자 앞에 *을 붙여서 사용합니다
def sum(a, b, c):
    return a + b + c

numbers = [1, 2, 3]
sum(numbers) # error

print(sum(*numbers)) # 출력 : 6

def cal(first, op, second):
    if op == '+':
        return first + second
    if op == '/':
        return first / second
    if op == '-':
        return first - second
    if op == '*':
        return first * second

prob = {
  'first': 12,
  'second': 34,
  'op': '*'
}

cal(**prob) # 결과 : 408