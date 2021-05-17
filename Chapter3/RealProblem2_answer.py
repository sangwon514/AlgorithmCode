n, m = map(int, input().split())

result = 0
for n in range(n):
    data = list(map(int, input().split())) # 한 줄씩 입력받아 확인
    minValue = min(data) # 현재 줄에서 '가장 작은 수' 찾기
    result = max(minValue, result) # '가장 작은 수'들 중에서 가장 큰 수 찾기

print(result)