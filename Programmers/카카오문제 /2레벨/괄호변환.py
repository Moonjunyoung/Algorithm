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

def check(w): ## 올바른 괄호인지 판단
    stack=list(w)
    cnt=0

    for i in range(len(stack)):
        if stack[i]=='(':
            cnt+=1
        elif stack[i]==')':
            cnt-=1
        if cnt<0:
            return False

    return True

def dfs(w):
    open=0
    close=0
    u=""
    v=""
    for i in range(len(w)):## 1. 균형잡힌 괄호로 분리
        if w[i]=='(':open+=1
        elif w[i]==')':close+=1
        if open==close: #균형잡인 괄호면
             u=w[0:i+1]
             v=w[i+1:]
             break

    if check(u) and len(v)==0: ## v가 빈문자열이고 u가 올바른 문자열인경우
        return u

    if check(u)==True: ## u가 균형잡힌 괄호면 v에대해 재귀적으로 수행 (균형잡힌 문자열이나올떄까지)
        a=dfs(v)
        answer=u+a ## u는 올바른괄호 문자열
        return answer
    else: #u가 올바르지않은 괄호면 v에대해 재귀적으로 수행 v에 대해 재귀적으로 수행했을떄 나온결과는 올바른괄호
        tmp='(' # 문제 예시대로 빈문자열에 ( 붙이고
        tmp+=dfs(v) # v에대해 재귀적으로 수행한결과 올바른괄호가나오는데 그거에 대해 붙여주고
        tmp+=')' # 마지막으로 괄호를 닫음
        u=list(u) # 그리고 현재 u의 첫번쨰와 마지막 문자를 제거하고
        tmp+=re(u) # v와 u를 합친다.
        return tmp ## 합친값을 반환







def solution(p):
    answer = ''
    answer=dfs(p)
    print(answer)

    return answer



