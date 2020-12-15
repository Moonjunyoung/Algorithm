def dfs(depth,start,number):
    global n,number_list,answer,visited

    if depth==n: ## 중복 조합구할시 set으로 처리 x
        if visited[number]==False: ##이미 만든조합이 아닌경우
            visited[number]=True
            answer+=1
        return

    for i in range(start,4): # 00 01 02 03 , 10 => 작은게 큰거 보다 앞에있어서 안됨
        dfs(depth+1,i,number+number_list[i])


    return




n=int(input())
number_list=[1,5,10,50]
visited=[False]*10000
answer=0
dfs(0,0,0)
print(answer)