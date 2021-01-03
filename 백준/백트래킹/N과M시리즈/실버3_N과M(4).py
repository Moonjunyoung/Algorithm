# N과 M (4) 자연수 N과 M이 주어졌을 때,1부터 N까지 자연수 중에서 M개를 고른 수열
# 같은 수를 여러 번 골라도 된다
def dfs(number,cur):
    global n,m
    if len(number)==m:
        for i in number:
            print(i,end=' ')
        print()
        return

    for i in range(cur,n+1):
        number.append(i)
        dfs(number,i)
        number.pop()


    return

n,m=map(int,input().split())


dfs([],1)
