import itertools
import copy

n=int(input()) #수의개수
number_list=list(map(int,input().split())) ##숫자들
operation=list(map(int,input().split()))
op=[]

for i in range(len(operation)): # 1. 들어오는 연산의 값에 따라 리스트에 append
    if operation[i]!=0:
        for _ in range(operation[i]):
            op.append(i)

permute=set(itertools.permutations(op,len(op))) # 2. 1에서 append한것을 가지고 순열함수를 돌려서 모든경우확인
min_answer=1000000001 # 2-> 이거값 떄메도 한번 틀렷음
max_answer=-1000000001 


#3. 2번에서 구한 모든경우가지고 일일히 하나씩 계산
for i in permute:
    tmp=copy.deepcopy(number_list)
    for j in i:
        if len(tmp)!=0:
            a = tmp.pop(0)
            b = tmp.pop(0)
            if j==0:
                tmp.insert(0,a+b)
            elif j==1:
                tmp.insert(0,a-b)
            elif j==2:
                tmp.insert(0,a*b)
            elif j==3:
                if a<0: # =>이것도유의 
                    a=abs(a)//b
                    a*=-1
                else:
                    a=a//b
                tmp.insert(0,a)

    min_answer=min(min_answer,tmp[-1])
    max_answer=max(max_answer,tmp[-1])

print(max_answer)
print(min_answer)






