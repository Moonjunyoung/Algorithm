def isPossible(distance): # 3. 해당거리에서 공유기를 c개이상 설치할수있는지확인
    global wires,c
    cur=wires[0]
    cnt=0
    for i in wires:
        if cur<=i: ##설치가가능하다
            cur=i+distance
            cnt+=1

    if cnt>=c:
        return True

    return False

# 1. c개의 공유기를 설치해야한다.
n,c=map(int,input().split())
wires=[]
for i in range(n):
    tmp=int(input())
    wires.append(tmp)

wires.sort()

#2. c개를 설치할수있는 최대거리를 구해봄
start=1
end=max(wires)
answer=0
while start<=end:
      distance=(start+end)//2
      if isPossible(distance):
          answer=max(answer,distance)
          start=distance+1 

      else:
          end=distance-1

print(answer)