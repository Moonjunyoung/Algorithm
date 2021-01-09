n,k=map(int,input().split())
number_list=list(map(int,input().split()))
sum=0
# 1. 첫번쨰 인덱스값의 누적합을 먼저 구한다.
for i in range(k):sum+=number_list[i]
answer=sum
right=k

# 2. 두번쨰인덱스부터 누적합을 구함 이떄 right값을 한개  이동시키고 더하고 이전에 더했던값을 빼면 2번쨰인덱스로부터의 연속합이 나옴 이를반복
for i in range(1,n-k+1):
    sum-=number_list[i-1]
    sum+=number_list[right]
    right+=1
    answer=max(answer,sum)

print(answer)
