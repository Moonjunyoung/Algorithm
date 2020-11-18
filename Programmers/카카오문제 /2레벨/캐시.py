def solution(cacheSize, cities):
    answer = 0
    queue=[]
    

    #캐시사이즈가 없는경우
    if cacheSize==0:
        return len(cities)*5
    
    for s in cities:
        s=s.upper()
        if len(queue)!=cacheSize: #1. 캐시가 꽉차 있지않고
            if len(queue)==0: #2. 큐가 비어있으면 그냥넣는다
                queue.append(s)
                answer+=5 #캐시 미스

            else:# 2.1 큐가 비어있지않고
                if s in queue: #큐안에 존재하면
                    queue.remove(s)##해당값을삭제하고
                    queue.append(s) ##맨뒤에 넣음
                    answer+=1 #캐시 히트
                else:#큐안에 없으면
                    answer+=5 #캐시 미스
                    queue.append(s)
        else: #2.캐시가 꽉차있는경우
            if s in queue: #큐안에 존재하면
                queue.remove(s) #해당값을 삭제하고
                queue.append(s) #맨뒤에 넣음
                answer+=1
            else:
                queue.pop(0) ##가장 오래된것을 뺴고
                answer+=5
                queue.append(s)
    
    return answer