def solution(progresses, speeds):
    answer = []
    queue = []
    
    for i in range(len(progresses)):
        count = 0
        while progresses[i] < 100 :
            count += 1
            progresses[i] += speeds[i]
        queue.append(count)
        
    cnt = 1
    tmpMax = queue[0]
    for idx, i in enumerate(queue):
        if idx == 0:
            continue
        if tmpMax < i :
            tmpMax = i
            answer.append(cnt)
            cnt = 0
        if idx == len(queue) - 1:
            cnt += 1
            answer.append(cnt)
        cnt += 1
            
            
    return answer