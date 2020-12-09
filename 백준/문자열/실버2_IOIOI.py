n=int(input())
m=int(input())
s=input()

answer=0
pattern_cnt=0

i=1
while i<m-1:
    if s[i-1]=='I' and s[i]=='O' and s[i+1]=='I':  ## IOI면
       pattern_cnt+=1  # 저장
       if pattern_cnt==n: ## n값과 동일하면 정답
           answer+=1  #
           pattern_cnt-=1 #하나를 뻄
       i+=1 ##인덱스 한칸증가
    else:
        pattern_cnt=0
    i+=1

print(answer)


