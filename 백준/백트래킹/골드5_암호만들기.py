# 2번쨰 품

def check_alpha_list(alpha):
    mo=0
    ja=0
    for i in alpha:
        if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
            mo+=1

        else:
            ja+=1

    if mo>=1 and ja>=2:
        return True

    return False

def dfs(alpha,cur):
    global alpha_list,l,c

    if len(alpha)==l:
        if check_alpha_list(alpha):
            print(alpha)
            return
        else:
            return

    for i in range(cur,len(alpha_list)):
        dfs(alpha+alpha_list[i],i+1)


    return

l,c=map(int,input().split())
alpha_list=list(map(str,input().split()))
alpha_list.sort()
dfs("",0)