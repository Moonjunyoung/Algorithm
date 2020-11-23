def dfs(lotto_list,cur):
    global lotto_number

    if len(lotto_list)==6:
        for i in lotto_list:print(i,end=' ')
        print()
        return

    if cur >= len(lotto_number):
        return

    else:
        lotto_list.append(lotto_number[cur])
        dfs(lotto_list,cur+1)
        lotto_list.pop()
        dfs(lotto_list,cur+1)





while True:
    a=list(map(int,input().split()))
    n=a[0]
    if n==0:break
    lotto_number=a[1:]

    dfs([],0)
    print()