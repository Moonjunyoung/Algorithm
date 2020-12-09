def dfs(li):
    global n,m,number_list,answer_list,check
    if len(li)==m:
        for i in li:
            print(i,end=' ')
        print()
        return


    tmp=-1 ##이전에 놧던값을 저장하기위함
    for i in range(len(number_list)):
        if tmp==number_list[i] or check[i]==True:
           continue
        tmp=number_list[i]
        check[i]=True
        li.append(number_list[i])
        dfs(li)
        li.pop()
        check[i]=False




n,m=map(int,input().split())
check=[False]*n
number_list=list(map(int,input().split()))
number_list.sort()
dfs([])