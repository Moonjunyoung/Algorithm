def check_number(number):
    global b
    if int(number)<=int(b):
        return True

    return False

def dfs(number):
    global a,answer,b
    if len(number) ==len(a):
        if number[0]=='0':return
        if check_number(number):
           answer=max(answer,int(number))
           return

    for i in range(len(a)):
        if check[i]==False:
            check[i]=True
            dfs(number+a[i])
            check[i]=False


    return
a,b=map(str,input().split())
answer=-1
check=[False]*len(a)
dfs("")
print(answer)