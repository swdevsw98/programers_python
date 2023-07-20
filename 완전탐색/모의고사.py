def solution(answers):
    answer = []
    one = [1,2,3,4,5]
    two = [2,1,2,3,2,4,2,5]
    three = [3,3,1,1,2,2,4,4,5,5]
    cnt = [0,0,0]
    
    for idx, i in enumerate(answers):
        if one[idx % 5] == i:
            cnt[0] += 1
        if two[idx % 8] == i:
            cnt[1] += 1
        if three[idx % 10] == i:
            cnt[2] += 1
    
    num = max(cnt)
    for idx, i in enumerate(cnt):
        if i == num :
            answer.append(idx + 1)
    
    return answer