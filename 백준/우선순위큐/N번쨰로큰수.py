import heapq

n=int(input())
number_list=[]
min_number=0
for i in range(n):
    if i==0:
        tmp=list(map(int,input().split()))
        for i in tmp:heapq.heappush(number_list,i)
        min_number=number_list[0]
        # 1. 현재 리스트의 원소중 가장 작은것 저장

    else:
         tmp=list(map(int,input().split()))
         for i in tmp:
             # 2. 입력으로 들어온 리스트의 값보다 최소값이 작으면 현재 리스트에서 최소값을 뺸다음 최소값을 다시갱신시킴
             if min_number<i:
                 heapq.heappop(number_list)
                 heapq.heappush(number_list,i)
                 min_number=number_list[0]

number_list.sort(reverse=True)
print(number_list[n-1])