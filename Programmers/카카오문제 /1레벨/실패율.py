def solution(n,stages):
    answer = []    
    human=len(stages)

    dic={}
    for i in range(1,n+1):dic[i]=0 #1. 1~n+1 스테이지 범위로 dictionary만들어줌
    for i in stages:
        if i==n+1:continue
        dic[i]+=1
    
    
    for i in dic:
        if human !=0: ## 2. 사람이 존재하면 실패율 계산
            answer.append((i,dic[i]/human))
        elif human==0 and dic[i]!=0: # 2.1 사람이 존재안하고 스테이지값이 존재하는경우 (전부다 못꺰 )
            answer.append((i,1))
        elif human==0: # 2.2 사람이 존재하지않고 스테이지 값도 없는경우 도달한사람이 없다는 것
             answer.append((i,0))
        
        human -= dic[i]
    
    
    
    answer=sorted(answer,key=(lambda x:x[1]),reverse=True)    
    tmp=[]
    for i in answer:
        tmp.append(i[0])
    return tmp