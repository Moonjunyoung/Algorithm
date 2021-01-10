def isPossible(day,stone,k):

    cnt=0

    # 해당 날에 돌을 건널수있는지 확인함 (연속적으로 k번밟은경우는 점프를 못함)
    for i in range(len(stone)):
        if stone[i]-(day-1)<=0:
            cnt+=1
        else:
            cnt=0

        if cnt==k:
            return False



    return True

def solution(stones, k):
    answer = 0
    left=1
    right=max(stones)
    while left<=right:
          mid=(left+right)//2
          if isPossible(mid,stones,k):
              answer=mid
              left=mid+1
          
          # 탐색범위를 좁힌다.
          else:
              right=mid-1

    return answer


solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1],3)