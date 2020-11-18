dartResult="1S*2T*3S"
stack=[]
for idx in range(len(dartResult)):
    if dartResult[idx]=='S':
        if idx-1>=0 and idx-2>=0:
            a=dartResult[idx-2]+dartResult[idx-1]
            if a.isnumeric():
                stack.append(int(a))
                continue

        stack.append(int(dartResult[idx-1]))
    elif dartResult[idx]=='D':
        if idx-1>=0 and idx-2>=0:
            a = dartResult[idx - 2] + dartResult[idx - 1]
            if a.isnumeric():
                stack.append(pow(int(a),2))
                continue

        tmp=int(dartResult[idx-1])
        tmp=pow(tmp,2)
        stack.append(tmp)

    elif dartResult[idx]=='T':
        if idx-1>=0 and idx-2>=0:
            a = dartResult[idx - 2] + dartResult[idx - 1]
            if a.isnumeric():
                stack.append(pow(int(a), 3))

        tmp = int(dartResult[idx - 1])
        tmp = pow(tmp, 3)
        stack.append(tmp)
    elif dartResult[idx]=='*': ##별표면 이전값과 이이전값을 두배로만듬
        if len(stack)==1:
            number=stack.pop()*2
            stack.append(number)
        elif len(stack)>=2:
            number=stack.pop()*2
            number2=stack.pop()*2
            stack.append(number)
            stack.append(number2)

    elif dartResult[idx]=='#':
         if len(stack)>=1:
             number=stack.pop()*-1
             stack.append(number)

sum=0
for i in stack:sum+=i
print(sum)




