def check_string(s):
    mo=0
    ja=0
    for i in s:
        if i =='a' or i=='e' or i=='i' or i=='o' or i=='u':
            mo+=1
        else:
            ja+=1

    if mo>=1 and ja>=2:
        return True
    else:
        return False


def dfs(cur,s):
    global l,c,string
    if len(s)==l: ## 1. 단어 완성시 암호가 될수 있는지 확인
        if check_string(s):
            print(s)
            return

    for i in range(cur,c):  # 2. 무조건 선택한 경우 다음의 것만 골라야함
        tmp=s
        dfs(i+1,s+string[i])
        s=tmp



    return



l,c=map(int,input().split())
string=list(map(str,input().split()))
string.sort()
check=[False]*c

dfs(0,"")




