def solution(s):
    cnt  = 0
    zeroCnt = 0
    answer = []
    lens = len(s)
    
    
    while lens != 1 :
        lens = len(s)
        temp = s.replace('0', '')
        zeroCnt += lens - len(temp)
        lens = len(temp)
        s = bin(lens)[2:]
        cnt += 1
        
    answer.append(cnt)
    answer.append(zeroCnt)
        
    return answer