def sticker_area(r1,c1,r2,c2):
    global h,w,answer


    for i in range(2):
        for j in range(2):
            if (r1+r2)<=h and max(c2,c1)<=w:
                answer=max(answer,(r1*c1)+(r2*c2))

            if max(r1,r2)<=h and (c2+c1)<=w:
                answer=max(answer,(r1*c1)+(r2*c2))

            r2,c2=c2,r2
        r1,c1=c1,r1



import itertools
answer=0
h,w=map(int,input().split())
sticker_number=int(input())
sticker_list=[]
for i in range(sticker_number):
    r,c=map(int,input().split())
    sticker_list.append([r,c])

combi_list=list(itertools.combinations(sticker_list,2))

for i in combi_list:
    r1,c1=i[0]
    r2,c2=i[1]
    sticker_area(r1,c1,r2,c2)


print(answer)