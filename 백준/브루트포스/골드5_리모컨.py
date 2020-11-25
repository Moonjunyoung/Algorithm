# 1. 누를 수있는 리모컨의 버튼으로 이동할수있는 모든 채널을 구하는 함
def dfs(numbers,a):
    global all_remote_number

    if len(a)==6:
        return
    else:
        for i in numbers:
            a.append(i)
            tmp=""
            for i in a:tmp+=str(i)
            all_remote_number.append(tmp)
            dfs(numbers,a)
            a.pop()


number=input()
k=int(number)
n=int(input())


# n이 0이 들어올때 처리를 해주지 않으면 런타임 오류 뜸
if n!=0:
    not_number=list(map(str,input().split()))
else:
    not_number=[]

cur=100
number=list(number)
answer=9999999999999
remote_number=[]
all_remote_number=[]

# 1. 리모컨 숫자 버튼 만을 눌렀을떄 만들수있는 번호를 구한다
for i in range(0,10):
    if str(i) not in not_number:
        remote_number.append(i)




# 2. 누를수 있는 리모컨 숫자를 가지고있는 배열을 통해 이동할수있는 모든채널을 구하는 함수
dfs(remote_number,[])


# 3. 리모컨으로 이동할수있는 모든 채널을 구해서 해당 채널에서 목표채널까지 최소 이동개수를 구함
if len(all_remote_number)>0:
    for i in all_remote_number:
        tmp=int(i)
        tmp=str(i)
        remote_cnt=len(tmp)
        remote_cnt+=abs(int(tmp)-k)
        answer=min(answer,remote_cnt)






k=int(k)
cnt=999999999

# 4. 현재채널 100에서 원하는채널까지 + or - 를 하여 이동할수있는 채널을 구함
if k>=100:
    cnt=0
    while k!=cur:
          cur+=1
          cnt+=1
else:
    cnt=0
    while cur!=k:
        cnt+=1
        cur-=1


answer=min(answer,cnt)
print(answer)