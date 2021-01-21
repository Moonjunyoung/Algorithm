n=int(input())
stack=[]
answer=0
for i in range(n):
    tmp=int(input())

    if len(stack)==0:
        stack.append(tmp)

    else:
        if stack[-1]>tmp: # 1. 현재 탑에 있는것보다 작은것이 들어오면 그냥 넣음
            stack.append(tmp)

        else:
            while len(stack)!=0 and stack[-1]<=tmp: # 2. 현재탑에잇는것이 들어오는것 보다 작을경우
                  stack.pop()
            stack.append(tmp)

    answer+= len(stack)-1

print(answer)