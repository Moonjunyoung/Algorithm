n = int(input())

stack=[]
answer_list=[]
cnt=1
for _ in range(n):
    number=int(input())
    while True:
        if len(stack) == 0: ##초기값이 0일떄  추가
            stack.append(cnt)
            answer_list.append('+')
            cnt+=1

        else:
            if stack[-1]>number: #1 .스택의 맨위에 있는값이 number값보다 큰경우 (스택수열을 만들수가없음)
                print('NO')
                exit(0)

            if stack[-1]<number: # 2. 맨위에 값이 작다면 해당 숫자가 나올떄까지 push
               stack.append(cnt)
               answer_list.append('+')
               cnt+=1

            elif stack[-1]==number: # 3. 탑 값이 같아지면 숫자를 Pop
                 stack.pop()
                 answer_list.append('-')
                 break


for i in answer_list:print(i)