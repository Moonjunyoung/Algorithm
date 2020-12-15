def dfs(start):
    global visited,string
    result=0

    for i in range(start,len(string)):
        if string[i]=='(' and visited[i]==False: # 1. 괄호일경우 방문
           visited[i]=True
           result+=int(string[i-1])*dfs(i+1)-1

        elif string[i]==')' and visited[i]==False: # 2. 닫인괄호를 만날경우 종료 시킴
             visited[i]=True
             return result
        elif visited[i]==False: ## 3. 괄호가 아니고 숫자일경우 카운팅
             visited[i]=True
             result+=1



    return result

string=input()
stack=[]
visited=[False]*50

print(dfs(0))