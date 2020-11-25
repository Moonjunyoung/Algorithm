#겹치지않는 경우를 고려한다 
def dfs(li):
    global n
    if len(li)==n:
        for i in li:
            print(i,end=' ')
        print()
        return

    for i in range(1,n+1):
        if check[i]==False:
            check[i]=True
            li.append(i)
            dfs(li)
            li.pop()
            check[i]=False




n=int(input())
check=[False]*(n+1)

dfs([])

