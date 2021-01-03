# N과 M (5) N개의 자연수 중에서 M개를 고른 수열

def dfs(number):
    global n,m,number_list
    if len(number)==m:
        for i in number:
            print(i,end=' ')
        print()
        return

    for i in range(len(number_list)):
        if number_list[i] not in number:
            number.append(number_list[i])
            dfs(number)
            number.pop()


    return

n,m=map(int,input().split())
number_list=list(map(int,input().split()))
number_list.sort()
dfs([])
