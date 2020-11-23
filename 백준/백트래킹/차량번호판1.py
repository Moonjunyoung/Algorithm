def dfs(string,cur):
    global s,answer,alpha

    if len(s)==len(string):
        answer+=1
        return

    if cur>=len(s):
        return

    if s[cur]=='d':
        for i in range(10):
            if len(string)>=1 and string[cur-1]==str(i):
                continue
            else:
                dfs(string+str(i),cur+1)

    elif s[cur]=='c':
          for i in range(26):
              if len(string) >= 1 and string[cur-1]==alpha[i]:
                  continue
              else:
                  dfs(string+alpha[i],cur+1)






s=input()
answer=0
alpha=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']


dfs("",0)
print(answer)