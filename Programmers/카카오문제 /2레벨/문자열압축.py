# 2번 풀었음
def solution(s):
    answer = 9999999

    for i in range(1,len(s)+1): ## 1. 문자열의 길이만큼 자를수있다.
        idx=0
        tmp_list=[]
        cnt=1
        while idx<len(s):
              string=s[idx:i+idx]
              if len(tmp_list)!=0 and tmp_list[-1]==string: # 2. 압축을 시킬수있으면
                 cnt+=1

              else: # 3. 압축불가능한경우 
                  if cnt > 1: # 4.압축시킬수있는 문자열이 존재하지는지 확인 존재하면 넣음
                      tmp_list.append(str(cnt) + tmp_list.pop())
                  
                  #초기화
                  tmp_list.append(string)
                  cnt=1

              idx+=i

        # 압축시킬수있는 문자열이 남아있으면 넣음
        if cnt>1:
           tmp_list.append(str(cnt) + tmp_list.pop())

        answer=min(answer,len("".join(tmp_list)))



    return answer




