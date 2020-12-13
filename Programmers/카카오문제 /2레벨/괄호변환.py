# 2번 풀었음 

def check_u(p):
    cnt=0
    for i in p:
        if cnt<0:
            return False
        if i=='(':
            cnt+=1
        else:
            cnt-=1

    if cnt < 0:
        return False
    return True

def re(s):
    stack=[]
    s.pop(0)
    s.pop()
    for i in s:
        if i=='(':
            stack.append(')')
        else:
            stack.append('(')

    tmp=""
    while len(stack)!=0:tmp+=stack.pop(0)

    return tmp

def check(p):
    cnt=0
    idx=0
    while idx<len(p):
          if p[idx]=='(':
              cnt+=1
          else:
              cnt-=1
          if cnt==0:
              idx += 1
              break
          idx+=1

    return p[:idx],p[idx:]

def dfs(p):
    u,v=check(p)
    if p=="":
        return ""

    if check_u(u): # u가 올바른 문자열이면 v에대해 재귀적으로 수행
        return u+dfs(v)

    else:
        tmp='('
        tmp+=dfs(v)
        tmp+=')'
        u=list(u)
        tmp+=re(u)
        return tmp



def solution(p):
    answer = ''

    print(dfs(p))

    return answer

