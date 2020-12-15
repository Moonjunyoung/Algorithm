def check_answer():
    global view_tmp

    garo_sum_1=view_tmp[0]+view_tmp[1]+view_tmp[2]
    garo_sum_2=view_tmp[3]+view_tmp[4]+view_tmp[5]
    garo_sum_3=view_tmp[6]+view_tmp[7]+view_tmp[8]

    if garo_sum_1!=garo_sum_2:return False
    if garo_sum_2!=garo_sum_3:return False

    sero_sum_1=view_tmp[0]+view_tmp[3]+view_tmp[6]
    sero_sum_2=view_tmp[1]+view_tmp[4]+view_tmp[7]
    sero_sum_3=view_tmp[2]+view_tmp[5]+view_tmp[8]
    if sero_sum_1!=sero_sum_2:return False
    if sero_sum_2!=sero_sum_3:return False


    s=0
    s1=0
    s+=view_tmp[0]+view_tmp[4]+view_tmp[8]
    s1+=view_tmp[2]+view_tmp[4]+view_tmp[6]

    if s!=s1:return False


    return True
def dfs(depth):
    global check,view_tmp,answer,view
    if depth==9:
        if check_answer():
            sum=0
            for i in range(9):sum+=abs(view[i]-view_tmp[i])
            answer=min(answer,sum)
            return

    for i in range(9):
        if check[i]==False:
            check[i]=True
            view_tmp[depth]=i+1
            dfs(depth+1)
            check[i]=False
            view_tmp[depth]=0


check=[False]*9
view=[0]*9
tmp=[0]*3
answer=999999999
view_tmp=[0]*9
for i in range(3):
    tmp[i]=list(map(int,input().split()))


idx=0
for i in range(3):
    for j in range(3):
        view[idx]=tmp[i][j]
        idx+=1

dfs(0)

print(answer)