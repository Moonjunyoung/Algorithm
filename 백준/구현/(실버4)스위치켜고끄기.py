n=int(input())
tmp=list(map(int,input().split()))
switch=[0]*(n+1)
for i in range(1,n+1):switch[i]=tmp[i-1]

student=int(input())

while student!=0:
      sex,number=map(int,input().split())
      if sex==1: #남학생인경우
          for i in range(1,len(switch)):
              if i%number==0:
                  if switch[i]==1:
                      switch[i]=0
                  else:
                      switch[i]=1
      elif sex==2: #여학생인경우
           left=number-1
           right=number+1
           check=[False]*(n+1)
           check[number]=True
           while left>0 and right<=n:
                 if switch[left]==switch[right]:
                    check[left]=True
                    check[right]=True
                 else:
                     break
                 left=left-1
                 right=right+1

           for i in range(1,n+1):
               if check[i]==True:
                   if switch[i]==1:
                       switch[i]=0
                   else:
                       switch[i]=1
      student-=1

for i in range(1,n+1):
    print(switch[i],end=' ')
    if i%20==0:
        print()