from itertools import permutations

def solution(k, dungeons):
    answer = -1
    
    for i in permutations(dungeons, len(dungeons)):
        tmp = 0
        tmp_k = k
        for j in i:
            if tmp_k < j[0]:
                break
            else:
                tmp_k -= j[1]
                tmp += 1
        
        answer = max(answer, tmp)
    
    return answer