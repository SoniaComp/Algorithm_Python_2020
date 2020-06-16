import sys
T=int(sys.stdin.readline())
S=0
for _ in range(T):
    opcodeStr=sys.stdin.readline()
 
    opcode=opcodeStr.split()[0]
    if opcode=="add":#or 이용하여 해당비트가 0이라면 1로 만들어준다.
        S |= 1<<int(opcodeStr.split()[1])
    elif opcode=="remove":#and 를 이용하여 해당비트가 무엇이든간에 1로 만들어준다 not을 써주면 해당비트만 0으로 만들수있다.
        S &= ~(1<<int(opcodeStr.split()[1]))
    elif opcode=="check":#해당비트와 and 연산을 통해 0이라면 0을 1이라면 1을 반환한다.
        if S & (1<<int(opcodeStr.split()[1])):
            print(1)
        else:
            print(0)
    elif opcode=="toggle":#xor연산
        S ^= (1<<int(opcodeStr.split()[1]))
    elif opcode=="all":#모두 1로 만들어준다.
        S=(1<<21)-1
    elif opcode=="empty":#0으로 만들어준다.
        S=0
