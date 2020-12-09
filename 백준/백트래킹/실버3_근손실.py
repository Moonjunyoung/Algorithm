def dfs(total,day):
    global kit,check,answer,k,n
    if total<500:
        return

    if day==n:
        answer+=1
        return


    for i in range(len(check)):
        if check[i]==False:
            check[i]=True
            total+=kit[i]
            total-=k
            dfs(total,day+1)
            check[i]=False
            total-=kit[i]
            total+=k

    return

answer=0
n,k=map(int,input().split())
kit=list(map(int,input().split()))
check=[False]*n

dfs(500,0)
print(answer)