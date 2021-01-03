def dfs(total):
    global number,answer
    if total>number:
        return

    if total==number:
        answer+=1
        return

    for i in range(1,4):
        dfs(total+i)

    return


n=int(input())
while n!=0:
    answer=0
    number=int(input())
    dfs(0)
    print(answer)


    n-=1