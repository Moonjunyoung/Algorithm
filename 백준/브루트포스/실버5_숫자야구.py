def check_answer(my_number):
    my_number=list(my_number)

    if '0' in my_number: # 1. 숫자 안에 0이 들어가 있으면 안된다.
        return False

    my_number=set(my_number)
    if len(my_number)==3: ## 2. 숫자가 중복된 숫자인지 확인한다.
        return True
    else:
        return False


def check_score(my_number,target_number): #점수구하는법
    check=[False]*10
    my_number=str(my_number)
    target_number=str(target_number)

    strike=0
    ball=0

    # 1. 먼저 타겟숫자의 숫자들을 체크한다
    for i in target_number:check[int(i)]=True

    # 2. 내 숫자가 타겟숫자에 들어있는지 확인하고 없을경우에는 건너 뛴다.
    for i in range(len(my_number)):
        if check[int(my_number[i])]==False:continue

        # 2. 내 숫자가 타겟 숫자에 들어가 있고 동일한 자릿수면 스트라이크 동일한 자릿수x 볼 처리
        if my_number[i]==target_number[i]:
            strike+=1
        else:
            ball+=1

    return [strike,ball]

n=int(input())
a=n
numbers=[]
strike=[]
ball=[]
while a!=0:
    num,s,b=map(int,input().split())
    numbers.append(num)
    strike.append(s)
    ball.append(b)
    a-=1

answer=0
for i in range(100,1000): # 100 ~1000 의 모든숫자들이 답에 속해있는지 찾는다.
    cnt=0
    for j in range(n):
        s,b=check_score(i,numbers[j])
        if strike[j]==s and ball[j]==b:
            cnt+=1
        else:
            break

    if cnt==n and check_answer(str(i)): ## 정답인 숫자 안에 중복된 숫자가 들어간지 0 이 들어가있는지 확인한다.
        answer+=1


print(answer)
