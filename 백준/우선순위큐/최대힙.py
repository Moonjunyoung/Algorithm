import heapq
from sys import stdin

n=int(stdin.readline())
number_list=[]

while n!=0:
      number=int(stdin.readline())
      if number==0: #배열에서 가장 큰값을 출력한다
          if len(number_list)==0: # 배열내에 아무것도 없으면 0출력
              print(0)
          else:
              print(heapq.heappop(number_list)[1]) # 최대값 출력

      else:
          heapq.heappush(number_list,[-number,number]) ## -는 우선순위 +는 값

      n-=1