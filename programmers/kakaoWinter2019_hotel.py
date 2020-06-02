import sys
sys.setrecursionlimit(10000000)  # 설정해주지 않으면 재귀가 많이 일어나면서 런타임에러 등이 나타날 수 있다.


def findEmptyRoom(number, rooms):  # 빈방을 찾는 함수
    # 현재 방넘버에 나무도 배정되지 않은 경우
    if number not in rooms:
        # 현재 방넘버 기준, 다음으로 빈방 좌표를 저장한다.
        rooms[number] = number + 1
        print('number')
        print(number)
        print(rooms)
        # 현재 방넘버 x를 반환한다.
        return number
    # 아무도 배정받지 않은 방이 나올 때까지, 함수를 실행
    empty = findEmptyRoom(rooms[number], rooms)
    rooms[number] = empty + 1
    print(rooms)
    return empty


def solution(k, room_number):
    answer = []
    rooms = dict()  # 몇번 방이 비어있는지 체크하는 딕셔너리

    for number in room_number:
        print('---')
        emptyRoom = findEmptyRoom(number, rooms)
        answer.append(emptyRoom)
        print('answer')
        print(answer)

    return answer


solution(10, [1, 3, 4, 1, 3, 1])
