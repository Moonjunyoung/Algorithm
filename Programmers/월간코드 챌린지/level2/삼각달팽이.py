def solution(n):
    answer = []
    map_list=[[0]]*n
    for i in range(n):map_list[i]=list([0]*n) #1.2차원 배열선언
    start=n
    cur=1
    cnt=1
    cur_x=0
    cur_y=0
    while start!=0:
        for i in range(start): ##start만큼 반복
            if cur==1: #2. 왼쪽 대각선으로 내려감 
                map_list[cur_x][cur_y]=cnt
                cur_x+=1
            elif cur==2: #2. 앞으로이동
                map_list[cur_x][cur_y]=cnt
                cur_y+=1
            elif cur==3: #2. 오른쪽 대각선으로 내려감
                map_list[cur_x][cur_y]=cnt
                cur_x-=1
                cur_y-=1
            cnt+=1
        
        # 3.다음위치 선정
        if cur==1:  
            cur_x-=1
            cur_y+=1
            cur=2
        elif cur==2:
            cur_x-=1
            cur_y-=2
            cur=3
        elif cur==3:
            cur_x+=2
            cur_y+=1
            cur=1
        
        start-=1
        
        
    for i in range(n):
        for j in range(n):
            if map_list[i][j]!=0:
                answer.append(map_list[i][j])
    
    
    return answer