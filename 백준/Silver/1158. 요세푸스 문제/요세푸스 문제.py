import sys

def josephus(n,k):
    
    n_list = list(range(1, n+1)) 
    result = []
    index = 0
    
    while n_list:  # 리스트에 요소가 남아있는 동안
        index = (index + k - 1) % len(n_list)  # 다음 인덱스 계산
        result.append(n_list.pop(index))  # 해당 인덱스의 요소를 결과에 추가하고 리스트에서 제거


    return "<" + ", ".join(map(str, result)) + ">"

N, K = map(int ,sys.stdin.readline().strip().split())

print(josephus(N,K))
        
    