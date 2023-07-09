def solution(s):
    arr = list(s)
    count = 0
    answer = ''
    
    for i in arr :
        if i == " " :
            count = 0
            answer += answer.join(" ")
            continue
        if count % 2 == 0:
            i = i.upper()
        else :
            i = i.lower()
        count += 1
        answer += answer.join(i)
    return answer