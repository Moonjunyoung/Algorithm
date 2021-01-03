import copy
def dfs(number_list,n,total):
    global answer,energy_list,visited
    if n==2:
        answer=max(total,answer)
        return
    else:
        tmp_list = copy.deepcopy(number_list)
        for i in range(len(tmp_list)):
            if i==0 or i==len(tmp_list)-1:continue
            k=total+(tmp_list[i-1]*tmp_list[i+1])
            tmp_list.pop(i)
            dfs(tmp_list,n-1,k)
            tmp_list = copy.deepcopy(number_list)




    return
n=int(input())
answer=0
visited=[False]*n
energy_list=list(map(int,input().split()))
number_list=[]
for i in energy_list:number_list.append(i)
dfs(number_list,n,0)
print(answer)