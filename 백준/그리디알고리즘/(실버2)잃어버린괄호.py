import re
expression=input()

temp = re.compile("(\D)").split(''+expression) # 정규 표현식을 사용하여 자름

idx=0
while idx<len(temp): # 1. 먼저 + 연산부터 처리해줌
      if temp[idx]=='+':
         a=int(temp[idx-1])
         b=int(temp[idx+1])
         temp[idx]=a+b
         temp.pop(idx-1)
         temp.pop(idx)
         idx=0
      idx+=1

idx=0
while idx<len(temp): # 2. 마이너스 연산을 해준다
      if temp[idx]=='-':
         a=int(temp[idx-1])
         b=int(temp[idx+1])
         temp[idx]=a-b
         temp.pop(idx-1)
         temp.pop(idx)
         idx=0
      idx+=1

print(temp[-1])

#  적절한괄호를 쳐서 최소 값이 되게하면된다. 이는 즉 먼저 더하기연산을 수행하고 그다음 빼기 연산을 수행하면된다.

