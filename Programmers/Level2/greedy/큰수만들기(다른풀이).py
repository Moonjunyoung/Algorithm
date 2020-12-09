def solution(number, k):
    stack=[]
    remove=0
    answer=""

    ## 1. 스택 맨 위에 있는 값보다 큰수가 나올떄 큰수 보다 작은값이 들어있는값은 모두 제거
    for i in range(len(number)):
        while stack and stack[-1]<int(number[i]) and remove<k: ## 1. 스택의 맨위에값이 현재숫자보다 작고 remove값이 k 보다 작을떄
            stack.pop()
            remove+=1


        if k==remove:
            stack.append(number[i:])
            break
        stack.append(int(number[i]))


    #2. remove가 안되어있을떄 remove를 시킴 ( 큰수가 중복이 되는 경우 처리가 안됨)
    while stack and k!=remove:
        stack.pop()
        remove+=1

    while stack:answer+=str(stack.pop(0))


    return answer