import heapq

def solution(scoville, K):
    answer = 0
    food_list=[]
    for i in scoville:heapq.heappush(food_list,i)

    while True: # 가장 작은 음식의 스코빌지수가 K보다 작을떄 반복
          if len(food_list) >=2 and food_list[0] < K:
             min_food1=heapq.heappop(food_list)
             min_food2=heapq.heappop(food_list)
             mix_food=min_food1+min_food2*2
             heapq.heappush(food_list,mix_food)
             answer+=1
          else:
              break

    
    if food_list[0]<K:
        return -1
    else:
        return answer