answer = 9999

def check_answer(cur_word,tar_word):
    cnt=0
    for i in range(len(cur_word)):
        if cur_word[i]!=tar_word[i]:
            cnt+=1

    if cnt==1:
        return True

    return False

def dfs(start,target,words,visited,depth):
    global answer

    if start==target:
        answer=min(answer,depth)
        return

    for i in range(len(words)):
        if visited[i]==False and check_answer(start,words[i]):
           visited[i]=True
           dfs(words[i],target,words,visited,depth+1)
           visited[i]=False



    return 

def solution(begin, target, words):

    visited=[False]*len(words)
    dfs(begin,target,words,visited,0)

    if answer==9999:
        return 0

    return answer

