# 풀이참조함
number="4177252841"
k=4

start=0
answer=""
for i in range(len(number)-k): # 1. 필요한숫자의 개수
    max_idx=start
    max_value=number[start]
    for j in range(start,i+k+1): # 2. k개의 숫자를 제거를 가정했을떄 뽑을수있는수
        if number[j]>max_value:
            max_idx=j
            max_value=number[j]

    start=max_idx+1 ## 3. 가장 크게 뽑을수있는 수 다음부터 시작
    answer+=max_value


print(answer)
