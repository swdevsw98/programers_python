def solution(n):
    answer = []
    
    while n >= 3:
        answer.append(n%3)
        n //= 3
        
    answer.append(n)
    
    mul = 1
    result = 0
    for i in range(len(answer) - 1, -1 , -1):
        result += answer[i] * mul
        mul *= 3
        
    
    return result