from collections import defaultdict

def solution(n, results):
    answer = 0
    win, lose = defaultdict(set), defaultdict(set)
    
    for winner, loser in results:
        print(winner, loser)
        win[winner].add(loser)
        lose[loser].add(winner)
        
        
    for i in range(1, n + 1) :
        for loser in lose[i]:
            win[loser].update(win[i])
        for winner in win[i]:
            lose[winner].update(lose[i])
            
    for i in range(1, n + 1):
        if len(win[i]) + len(lose[i]) == n - 1:
            answer += 1
    return answer