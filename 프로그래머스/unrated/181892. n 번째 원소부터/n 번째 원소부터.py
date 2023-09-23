def solution(num_list, n):
    answer = []
    for num in range(n-1, len(num_list)):
        answer.append(num_list[num])
    return answer