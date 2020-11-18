import itertools

n,s=map(int,input().split())
number_list=list(map(int,input().split()))

answer=0



for i in range(n,0,-1):
    combination_list = list(itertools.combinations(number_list,i)) ##조합을 사용해서 5개일떄 4개일떄 3개일떄의 조합을 구해서 답을 찾아냄
    for j in combination_list:
        sum=0
        for z in j:
            sum+=z

        if sum==s:
            answer+=1

print(answer)
