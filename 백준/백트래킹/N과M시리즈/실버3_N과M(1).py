# N과 M (1) 1부터 N까지 자연수중에서 중복없이 M개를 고른 수열
def dfs(number):
    global n,m
    if len(number)==m:
        for i in number:
            print(i,end=' ')
        print()
        return

    for i in range(1,n+1):
        if i not in number: # i가 없을경우 넣음
            number.append(i)
            dfs(number)
            number.pop()

    return

n,m=map(int,input().split())


dfs([])
