n=int(input())
vote=int(input())
voted_human=list(map(int,input().split()))
pictures={}

for i in range(vote):
    if voted_human[i] in pictures:  # 1. 게시된 사진에 있으면
       pictures[voted_human[i]] += 1
       continue

    if len(pictures)<n:
        if voted_human[i] not in pictures: # 1. 게시된 사진에없으면 추가
           pictures[voted_human[i]]=1

    else: #사진이 꽉찬경우
        # value 순으로 오름차순 정렬
        tmp=sorted(pictures.items(),key=lambda x:x[1])
        min_value=min(pictures.values())
        remove_list=[]
        # 제거할것들의 목록을 추가 
        for key,value in tmp:
            if min_value==value:
                remove_list.append(key)

        del pictures[remove_list[0]]

        if voted_human[i] not in pictures:  # 1. 게시된 사진에없으면 추가
            pictures[voted_human[i]] = 1


answer=sorted(pictures.items(),key=lambda x:x[0])
for key,value in answer:
    print(key,end=' ')
