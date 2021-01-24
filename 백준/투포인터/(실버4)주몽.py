n=int(input())
m=int(input())
li=list(map(int,input().split()))

li.sort()
left=0
right=len(li)-1
answer=0
while left<right:
      if li[left]+li[right]<m:
          left+=1

      elif li[left]+li[right]==m:
           answer+=1
           left+=1
           right-=1

      elif li[left]+li[right]>m:
           right-=1

print(answer)