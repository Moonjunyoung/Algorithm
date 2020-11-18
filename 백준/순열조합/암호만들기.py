import itertools

def check(s): # 1. 자음이 두개이상 모음이 한개이상 있는지체크
    mo=0
    ja=0
    for i in s:
        if i =='a' or i=='e' or i=='i' or i=='o' or i=='u':
            mo+=1
        else:
            ja+=1

    if mo>=1 and ja>=2:
        return True
    else:
        return False

l,c=map(int,input().split())
string=list(map(str,input().split()))


answer_list=[]
com_list=list(itertools.combinations(string,l)) ##2. 조합사용 순서고려 x므로 무조건 사전순으로 알파벳이나옴
for i in com_list: 
    tmp=''
    for j in i:tmp+=j
    if check(tmp): ## 3. 단어조건을 만족시키면 
        tmp=list(tmp)
        tmp.sort() ##정렬후 추가
        a=""
        for z in tmp:a+=z
        answer_list.append(a)

answer_list.sort()
for i in answer_list:print(i)
