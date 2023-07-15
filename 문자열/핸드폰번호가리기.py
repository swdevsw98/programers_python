def solution(phone_number):
    answer = ''
    len_number = len(phone_number)
    
    for i in range(len_number - 4):
        answer += "*"
    answer += phone_number[len_number-4 : len_number]
    return answer