import heapq
n=int(input())
number_list=[]
for i in range(n):
    tmp=int(input())
    heapq.heappush(number_list,tmp)

s=0

# 가장 작은것을 더해주고 넣고 반복하면댐
while len(number_list)!=1:
      a=heapq.heappop(number_list)
      b=heapq.heappop(number_list)
      s+=a+b
      heapq.heappush(number_list,a+b)

print(s)