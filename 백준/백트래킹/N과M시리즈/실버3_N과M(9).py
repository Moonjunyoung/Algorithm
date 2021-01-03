# N과 M (9) N개의 자연수와 자연수 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오. N개의 자연수는 모두 다른 수이다.

# 나중에 한번 다시 풀어보기 


def dfs(number):
    global n,m,number_list,visited
    if len(number)==m:
        for i in number:
            print(i,end=' ')
        print()
        return

    tmp=-1
    for i in range(len(number_list)):
        if visited[i]==True:continue
        if tmp!=number_list[i]: # 이전에 선택한값이 아닌경우
            visited[i]=True
            number.append(number_list[i])
            tmp=number_list[i]
            dfs(number)
            number.pop()
            visited[i]=False



    return

n,m=map(int,input().split())
visited=[False]*n
number_list=list(map(int,input().split()))
number_list.sort()
dfs([])
