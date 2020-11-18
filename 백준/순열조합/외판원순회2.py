import itertools

 ##메모리 초과 남
n=int(input())

travel_map=[0]*n
for i in range(n):travel_map[i]=list(map(int,input().split()))
travel_route=[]
for i in range(n):travel_route.append(i)
permute_route=set(itertools.permutations(travel_route,n))
permute_route=sorted(permute_route)

answer=1000003
for value in permute_route:
    cost=0
    flag=True
    for j in range(len(value)-1):
        start=value[j]
        next=value[j + 1]
        if travel_map[start][next]==0:
            flag=False
            break ##방문불가
        cost+=travel_map[start][next]

    if flag==True:
        if travel_map[value[len(value)-1]][value[0]]==0:continue
        cost+=travel_map[value[len(value)-1]][value[0]] ##다시 원래도시로 돌아옴
        answer=min(answer,cost)


print(answer)

# 풀이 접근은 맞았는데 메모리초과 
#아래 다른사람 코드 비슷한풀이고 메모리초과 x

import sys
from itertools import permutations
from itertools import permutations

n = int(input())
d= []
for i in range(n):
    d.append([int(a) for a in input().split()])

perm = [i for i in range(n)]
answer = 9123491234
def sum_routes(r):
    global d, n
    tmp = 0
    for i in range(len(r)-1):
        if d[r[i]][r[i+1]] !=0:
            tmp +=d[r[i]][r[i+1]]
        else:
            return -1

    if d[r[-1]][r[0]] ==0:
        return -1
    else:
        tmp += d[r[-1]][r[0]]

    return tmp

for c in permutations(perm):
    tmpans = sum_routes(c)
    if tmpans != -1:
        answer = min(answer, tmpans)

print(answer)