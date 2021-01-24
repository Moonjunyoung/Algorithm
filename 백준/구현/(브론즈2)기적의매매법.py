n=int(input())
juga=list(map(int,input().split()))

human_a=n
cost_a=0
human_b=n
cost_b=0

# 1.준현이의 매입방법  살수있으면 다산다
for i in juga:
    tmp=0
    if human_a>=i:
        tmp+=human_a//i
        cost_a+=tmp
        human_a-=i*tmp




# 2. 성민이 매입방법 : 3일 연속 하락하는 구간이 지난뒤 산다 이때 매입이 가능해야삼
# 매수방법 : 3일 연속 상승하는 구간이 지난뒤 매수

cnt=0
cnt2=0
for i in range(1,len(juga)):
    tmp2=0
    if juga[i]<juga[i-1]:
        cnt2=0
        cnt+=1

    elif juga[i]>juga[i-1]:
        cnt=0
        cnt2+=1

    # 1. 매수
    if cnt>=3:
        if human_b>=juga[i]:
            tmp2=human_b//juga[i]
            cost_b+=tmp2
            human_b-=juga[i] * tmp2
    # 2. 매도
    elif cnt2>=3:
         if cost_b!=0:
            human_b+=cost_b*juga[i]
            cost_b=0



if human_a+cost_a*juga[13]>human_b+cost_b*juga[13]:
   print('BNP')
elif human_a+cost_a*juga[13]==human_b+cost_b*juga[13]:
    print('SAMESAME')
else:
    print('TIMING')