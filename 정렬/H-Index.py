def solution(citations):
    answer = 0
    arr = sorted(citations)
    for idx, val in enumerate(arr):
        if len(arr) - idx <= val:
            answer = max(answer, len(arr) - idx)
    return answer