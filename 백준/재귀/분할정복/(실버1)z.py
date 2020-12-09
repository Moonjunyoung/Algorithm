def z(x,y,n):
    global r,c,answer
    if n==1: ## 1. 더이상 쪼갤수없을떄 해당 범위면
        if x==r and y==c:
            print(answer)
            exit(0)
        else:
            answer+=1
        return
    else: # 2. 4등분했을떄 해당범위가 정답 범위 안에없을경우 쪼갠만큼 곱해서 쪼갠범위 탈출
        if r>=x+n:
            answer+=n*n
            return
        elif c>=y+n:
            answer+=n*n
            return



    div=n//2
    z(x,y,div) #1사분면
    z(x,y+div,div) #2사분면
    z(x+div,y,div) #3사분면
    z(x+div,y+div,div) #4사분면



    return

answer=0
n,r,c=map(int,input().split())
z(0,0,2**n)