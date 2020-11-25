n=int(input())
li=[]
for i in range(n):
    a,b=map(int,input().split())
    li.append((a,b))


li=sorted(li,key=lambda x:x[1]) #color순으로 정렬


answer_list=[]


#2중 포문을 통해 거리가 가까운 점을 일일히 찾음
for i in li: 
    pos=i[0]
    color=i[1]
    dis=9999999999
    for j in li:
        if j[0]==pos and j[1]==color:continue
        if j[1]!=color:continue
        if j[1]==color:
            dis=min(dis,abs(pos-j[0]))

    answer_list.append(dis)


print(sum(answer_list))