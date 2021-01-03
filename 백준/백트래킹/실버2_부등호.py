import sys

# 2번쨰 푸는중
def check_correct_number(number):
    global equal_number
    number=list(number)

    for i in range(len(number)-1):
        if equal_number[i]=='<':
           if int(number[i])>int(number[i+1]):
               return False

        if equal_number[i]=='>':
            if int(number[i])<int(number[i+1]):
                return False

    return True


def dfs(depth,number):
    global n,max_number,min_number,visited,max_answer,min_answer
    if depth==n+1:
        if check_correct_number(number):
           if max_number<int(number):
               max_number=int(number)
               max_answer=number

           if min_number>int(number):
               min_number=int(number)
               min_answer=number
        return

    for i in range(10):
        if visited[i]==False:
            visited[i]=True
            dfs(depth+1,number+str(i))
            visited[i]=False

    return

max_number=0
min_number=999999999999
max_answer=""
min_answer=""
n=int(input())
visited=[False]*(10)
equal_number=input().split(' ')


dfs(0,"")


print(max_answer)
print(min_answer)