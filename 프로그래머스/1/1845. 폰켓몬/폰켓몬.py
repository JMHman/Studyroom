def solution(nums):
    answer = 0
    i = len(nums)/2
    x = len(set(nums))
    if i < x:
        answer = i
    else:
        answer = x
    return answer