def count_odd_number(number):
    tmp=list(number)
    cnt=0
    for i in tmp:
        if int(i)%2==1:
            cnt+=1
    return cnt




def dfs(number,odd_num):
    global answer_max,answer_min

    odd_number=count_odd_number(number)
    if len(number)==1: ##수가 한자리면 더이상 아무것도 하지못하고 종료
        answer_max = max(answer_max, odd_number+odd_num)
        answer_min = min(answer_min, odd_number+odd_num)
        return

    elif len(number)==2: #수가 두자리면 2개로나눠서 합을 구함
         tmp=int(number)//10+int(number)%10
         dfs(str(tmp),odd_num+odd_number)
         return

    elif len(number)>=3: #수가 세자리이상이면 임의의 위치에서 3개의수로 분할
         for i in range(len(number)):
             for j in range(i+1,len(number)):
                 for z in range(j+1,len(number)):
                     a=int(number[i:j])
                     b=int(number[j:z])
                     c=int(number[z:])
                     if len(str(a)+str(b)+str(c))!=len(number):continue
                     dfs(str(a+b+c),odd_num+odd_number)


    return



s=input()
answer_min=0x7fffffff
answer_max=-0
dfs(s,0)

print(answer_min,answer_max)