def solution(record):
    answer = []
    id = {}
    for rec in record:
        rec = rec.split(' ')
        if(rec[0] == 'Enter' or rec[0] == 'Change'):
            id[rec[1]] = rec[2]
    for rec in record:
        rec = rec.split(' ')
        if rec[0] == 'Enter' or rec == 'Leave':
            str = id[rec[1]]+show(rec[0])
            answer.append(str)
    return answer


def show(rec):
    return {'Enter': '님이 들어왔습니다.', 'Leave': '님이 나갔습니다'}[rec]


print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo",
          "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]))
