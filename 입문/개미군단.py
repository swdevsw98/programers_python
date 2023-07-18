def solution(hp):
    answer = 0
    ant = [5,3,1]
    
    for i in ant :
        temp = hp//i
        answer += temp
        hp -= i * temp
        
    return answer