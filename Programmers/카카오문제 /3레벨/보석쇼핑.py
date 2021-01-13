def solution(gems):
    answer = []
    answer_gem = set(gems)
    left=0
    right=0
    dic={gems[0]:1}

    while left <len(gems) and right<len(gems):
          # 1. 정답을 갱신할수있는 구간이면 갱신후 범위를 더좁힘
          if len(dic)==len(answer_gem):
             answer.append([left+1,right+1,right-left])
             dic[gems[left]]-=1
             if dic[gems[left]]==0:
                del dic[gems[left]]
             left+=1

          # 2. 정답을 갱신할수없을경우 right포인터값을 늘리면서 정답을 찾으러감
          else:
              right+=1
              if right==len(gems):break
              if gems[right] not in dic:
                 dic[gems[right]]=1
              elif gems[right] in dic:
                   dic[gems[right]]+=1




    # 3. 구간이 짧은순으로 우선정렬 , 2. left가가까운것으로
    answer = sorted(answer, key=lambda x: (x[2], x[0]))
    return answer[0][0], answer[0][1]