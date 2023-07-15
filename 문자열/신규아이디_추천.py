def solution(new_id):
    answer = ''
    
    #step 1
    answer = new_id.lower()
    
    #step 2
    filter = []
    for c in answer:
        if c.isalpha() or c.isdigit() or c in ('-','_','.'):
            filter.append(c)
    answer = ''.join(filter)
    
    #step 3
    while '..' in answer:
        answer = answer.replace('..', '.')
        
    #step 4
    answer = answer.strip('.')
    
    #step 5
    if len(answer) == 0:
        answer = 'a'
        
    #step 6
    if len(answer) >= 16:
        answer = answer[0:15]
        answer = answer.strip('.')
        
    #step 7
    if len(answer) <= 2:
        while len(answer) != 3:
            answer += answer[-1]
            
    
    
    return answer