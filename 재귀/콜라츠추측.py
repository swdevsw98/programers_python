def collatz(num, cnt):
    if cnt == 500:
        return -1
    if num == 1: 
        return cnt
    elif num % 2 == 0 :
        cnt += 1
        return collatz(num/2, cnt)
    else : 
        cnt += 1
        return collatz(num*3 + 1, cnt)

def solution(num):
    answer = 0
    answer = collatz(num, answer)
    return answer