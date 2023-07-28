def solution(info, query):
    answer = []
    
    for idx, que in enumerate(query):
        #query 분리
        que_list = que.replace(" and", "").split(" ")
        tmp = []
        for inf in info:
            visit = [0] * 4
            inf_list = inf.split()
            for t_idx ,t in enumerate(inf_list):
                if t_idx == 4 : break
                if que_list[t_idx] == '-' or que_list[t_idx] == t:
                    visit[t_idx] = 1
                else :break
                
            if 0 not in visit and int(que_list[4]) <= int(inf_list[4]):
                tmp.append(inf)
                
            
        answer.append(len(tmp))
                  
            
    return answer