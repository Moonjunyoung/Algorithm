def divide(n,x,y):
    global view,answer_blue,answer_white
    if n==0: ## 더이상 짜를수없으면 종료
        return

    if check(n,1,x,y)==True: ## 1. 해당 범위안에서 종이를 만들수있는지확인
        answer_blue+=1
        return

    if check(n,0,x,y)==True: ## 1.1 해당 범위안에서 종이를 만들수있는지확인
       answer_white+=1
       return




    divide(n//2,x,y) ## 절반으로 자른 범위의 1사분면으로 이동 
    divide(n//2,x,y+n//2) ##절반으로 자른 범위의 2사분면으로 이동
    divide(n//2,x+n//2,y)  ##절반으로 자른 범위의 3사분면으로 이동
    divide(n//2,x+n//2,y+n//2)  ##절반으로 자른 범위의 4사분면으로 이동




## 해당 영역안에서 종이가 만들어 질수있는지 확인하는 함수
def check(n,paper,x,y):
    global view
    for i in range(x,n+x):
        for j in range(y,n+y):
            if view[i][j]!=paper:
                return False

    return True


answer_blue=0
answer_white=0
n=int(input())
view=[[0]]*n
for i in range(n):view[i]=list(map(int,input().split()))

divide(n,0,0)


print(answer_white)
print(answer_blue)