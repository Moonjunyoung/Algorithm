string=input()

answer=99999
for i in range(len(string)): # 1. 문자열의 길이 만큼 돌림 1~문자열 길이만큼 압축할예정
    j=0
    alpha_list = []
    cnt=1
    while j+(i+1)<=len(string): #2. 압축을할수있는 인덱스값인지 체크
        next=j+(i+1)
        tmp=string[j:next] # 3. 압축을 한 문자열값

        if len(alpha_list)!=0 and tmp in alpha_list[-1]:# 4. 가장위에 있는 값이랑 같으면 압축이가능해짐
            cnt+=1 
            alpha_list.pop() ##가장위에있는값 빼고 
            alpha_list.append(str(cnt)+str(tmp)) #5. 압축한 문자열 넣기
            j = j + (i + 1)
            continue
        cnt=1
        alpha_list.append(tmp) ## 일반 문자열을 그냥 넣음

        j=j+(i+1)

    ## 6.압축시키지 못한 남는 문자열을 다넣음
    for idx in range(j,len(string)):
        alpha_list.append(string[idx])

    tmp=""
    ## 7. 정답 체크
    for a in alpha_list:tmp+=a
    answer=min(answer,len(tmp))


print(answer)
