def solution(record):
    answer = []
    user = {}
    
    for rec in record:
        tmp = rec.split(" ")
        if tmp[0] != 'Leave':
            user[tmp[1]] = tmp[2]
            

    
    for rec in record:
        tmp = rec.split(" ")
        if tmp[0] == 'Enter':
            answer.append(user[tmp[1]] + "님이 들어왔습니다.")
        elif tmp[0] == 'Leave':
            answer.append(user[tmp[1]] + "님이 나갔습니다.")
    
    
    return answer