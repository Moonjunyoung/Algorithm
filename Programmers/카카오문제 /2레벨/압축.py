def solution(msg):
    alpha=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    dic={}
    answer=[]
    for idx,value in enumerate(alpha):dic[value]=idx+1
    left=0
    right=len(msg)
    start=26
    cnt=1
    c=""
    while left<=right:
        if left==right: # 마지막에 도달했을떄 
            answer.append(dic[c])
            break

        if c+msg[left] in dic: #1. 사전에 존재하는지 확인한다 
           c+=msg[left] # 2. 사전에 존재할경우 해당 문자를 추가한다. (새로만들어야하므로)
        else:#  3. 추가 된 문자가 사전에 없으면
            answer.append(dic[c])  
            c=c+msg[left] # 4. c값을 사전에 없는 문자값으로 만들어준다.
            dic[c]=start+1 
            start+=1
            c=msg[left] #5.그리고 c값 갱신됬으므로  추가되어 생긴 앞에 있는것을 삭제하고 현재값으로 다시 초기화


        left+=1



    return answer