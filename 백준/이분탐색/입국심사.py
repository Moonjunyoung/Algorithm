def isPossibe(time):
    global wait_list,m
    cnt=0
    for i in wait_list:
        cnt+=time//i # 1. 주어진시간에 해당 심사대에 사람이 몇명들어가는지 확인


    if cnt>=m: # 2 .주어진시간에 사람들이 전부다 들어간경우
        return True
    else:
        return False

n,m=map(int,input().split())
wait_list=[]
for i in range(n):
    tmp=int(input())
    wait_list.append(tmp)


wait_list.sort()
start=1
end=max(wait_list)*m # 가장 최악의 시간
answer=max(wait_list)*m
while start<=end:
      time=(start+end)//2
      if isPossibe(time):
          answer=min(answer,time)
          end=time-1
      else:
          start=time+1

print(answer)