def solution(nums):
    i = len(nums) // 2  # 폰켓몬을 선택할 수 있는 최대 수
    x = len(set(nums))  # 고유한 폰켓몬 종류의 수
    return min(i, x)  # 선택할 수 있는 폰켓몬 종류의 최대 수를 반환
