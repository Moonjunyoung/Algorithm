duck_sound=input()
check=[False]*len(duck_sound)
sound=['q','u','a','c','k']
answer=0

while True:
      cnt = 0
      idx=0
      for i in range(len(duck_sound)):
          if sound[idx]==duck_sound[i] and check[i]==False:
             check[i]=True
             cnt+=1
             idx+=1
             idx%=5

      if cnt>=5 and cnt%5==0:
         answer+=1
      else:
          break

for i in range(len(duck_sound)):
    if check[i]==False:
        print(-1)
        exit(0)

if answer==0 or len(duck_sound)%5!=0:
    print(-1)
else:
    print(answer)