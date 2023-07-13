def solution(s):
    answer = []
    data = s[2:-2].split("},{")
    data = sorted(data, key = lambda x : len(x))
    
    for item in data:
        item = item.split(",")
        for value in item:
            if int(value) not in answer:
                answer.append(int(value))
    return answer