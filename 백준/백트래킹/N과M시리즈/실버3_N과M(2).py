# N과 M (2) 자연수 N과 M이 주어졌을 때, 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
def dfs(number,cur):
    global n,m
    if len(number)==m:
        for i in number:
            print(i,end=' ')
        print()

    for i in range(cur,n+1): # cur값 이전값은 나올수없게 함
        if i not in number:
            number.append(i)
            dfs(number,i)
            number.pop()


    return

n,m=map(int,input().split())


dfs([],1)
