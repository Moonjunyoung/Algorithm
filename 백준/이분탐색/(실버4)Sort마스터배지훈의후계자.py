import bisect
n,m=map(int,input().split())
a=[]
d=[]
for i in range(n):
    tmp=int(input())
    a.append(tmp)

for i in range(m):
    tmp = int(input())
    d.append(tmp)

# 1. 정렬
a.sort()

# 2. 이분탐색으로 찾음
for i in d:
    left=bisect.bisect_left(a,i)
    right=bisect.bisect_right(a,i)
    if abs(left-right)>0:
        print(left)
    else:
        print(-1)

