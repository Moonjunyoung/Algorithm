## 존나아슬아슬하게 해서 통과

def check_answer(string):
    for i in range(len(string)-1):
        if string[i]==string[i+1]:
            return False

    return True


def dfs(string):
    global visit,s,answer,a
    if len(string)== len(s):
        if check_answer(string)==True:
            if string not in a:
                a.add(string)
                answer+=1
        return


    for i in range(len(s)):
        if visit[i]==False:
            tmp=""
            tmp+=string
            visit[i]=True
            tmp+=s[i]
            dfs(tmp)
            visit[i]=False




s=input()
s=list(s)
a=set()
visit=[False]*len(s)
answer=0
dfs("")
print(answer)