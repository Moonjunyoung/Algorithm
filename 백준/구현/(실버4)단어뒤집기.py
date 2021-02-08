str=input()

stack=[]
flag=False
for i in str:
    # 1. 공백이 나오고 태그가 아닌경우 출력
    if i==' ' and flag==False:
       print("".join(stack[::-1]),end=' ')
       stack=[]

    # 2. 태그가 나온경우 스택값이 존재하면 출력 태그가나왓으므로 flag True활성화 그냥 출력함
    elif i=='<':
        if len(stack):
            print("".join(stack[::-1]), end='')
            stack = []

        flag=True
        print(i,end='')

    # 3. 닫힌태그가 나온경우 flag =False
    elif i=='>':
         flag=False
         print(i, end='')

    # 4. 그냥 문자인경우 태그활성화일시 (flag) 그냥 출력 , 아닐경우 그냥 스택에넣음
    else: 
         if flag:
            print(i,end='')
         else:
             stack.append(i)


if len(stack):
    print("".join(stack[::-1]), end=' ')
