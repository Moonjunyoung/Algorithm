t=int(input())


while t!=0:
    word_len=int(input())
    answer_list=[]
    words=[]
    for i in range(word_len):
        a=input()
        words.append(a)

    for i,value in enumerate(words):
        flag=False
        for j in range(len(words)):
            if i==j:continue
            a=value+words[j]
            b=a[::-1]
            if a==b:
                answer_list.append(a)
                flag=True
                break
        if flag:
            break

    if len(answer_list)==0:
        print(0)
    else:
        for i in answer_list:print(i)




    t-=1