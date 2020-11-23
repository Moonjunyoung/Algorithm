n=int(input())

answer=0



start=9

# 1. 해당 len 까지 검사
# 2. 120일 경우 len = 3
# len=1 answer=9 , len=2 answer=189 , len=3 이면 121-100 * 3 

for i in range(1,len(str(n))+1):
    if i==len(str(n)):
        tmp=(n+1)-(start//9)
        answer+=tmp*i
        break

    answer+=i*start
    start*=10



print(answer)
