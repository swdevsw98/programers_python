def solution(genres, plays):
    answer = []
    sum_dic = {}
    play_dic = {}
        
    for i in range(len(plays)):
        play_dic[i] = plays[i]
    
    for i in range(len(genres)):
        sum_dic[genres[i]] = sum_dic.get(genres[i],0) + plays[i]
        
    # print(sum_dic, max(sum_dic.values()))
    
    for _ in range(len(sum_dic)):
        sum_dic.pop(gen)
        gens = []
        for idx, j in enumerate(genres):
            if j == gen:
                gens.append(idx)
        
        gens.sort()
        print(gens)
        
        for i in range(2):
            if i == 1 and len(gens) == 1:
                break
            idx = 0
            playMax = 0
            for j in gens:

                if playMax < play_dic[j]:
                    idx = j
                    playMax = play_dic[j]
                    
            play_dic[idx] = -1
            answer.append(idx)
            

    
    return answer