n,m=map(int,input().split())
number_list=list(map(int,input().split()))
answer=0

right=0
sum=0
for i in number_list:
        # 1 .구간합을 구한다 sum값이 m보다 작을떄까지
        while right<len(number_list) and sum<m:
              sum+=number_list[right]
              right+=1

        # 2. 구간합이 정답과 만족하는경우 +1
        if sum==m:
            answer+=1

        # 현재 left의 값을 뺴준다
        sum -= i



print(answer)