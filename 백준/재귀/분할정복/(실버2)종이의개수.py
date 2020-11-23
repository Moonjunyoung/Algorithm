import sys
sys.setrecursionlimit(100000)

##시간 초과 발생

def check(x,y,number,n):
    
    for i in range(x,x+n):
        for j in range(y,y+n):
            if number!=papers[i][j]:
                return False
    
    return True

def divide(n,x,y):
    global answer_mi_count,answer_one_count,answer_zero_count
    if n==0:
        return

    if check(x,y,-1,n)==True:
        answer_mi_count+=1
        return
    if check(x,y,0,n)==True:
        answer_zero_count+=1
        return
    if check(x,y,1,n)==True:
        answer_one_count+=1
        return



    ##종이를 짜름
    n=n//3
    divide(n,x,y) ##
    divide(n,x,y+n) ##
    divide(n,x+n,y) ## 3번쨰
    divide(n,x+n,y+n)
    divide(n,x,y+2*n)
    divide(n,x+2*n,y+2*n)
    divide(n,x+2*n,y)
    divide(n,x+2*n,y+n)
    divide(n,x+n,y+2*n)
    ##종이를 9등분


n=int(input())
papers=[0]*n
answer_mi_count=0
answer_zero_count=0
answer_one_count=0

for i in range(n):papers[i]=list(map(int,input().split()))

divide(n,0,0)

print(answer_mi_count)
print(answer_zero_count)
print(answer_one_count)