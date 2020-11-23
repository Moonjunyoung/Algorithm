def dfs(number_list,start):
    global k,cards,answer_list,check
    if k==len(number_list):
        tmp=""
        for i in number_list:tmp+=i
        answer_list.add(int(tmp))
        return




    for i in range(len(cards)):
        if check[i]==False: # =>체크 배열로 해당 배열이 체크된지 확인 (중복된수를 못오게해야되므로)
            check[i]=True # 1.방문 
            number_list.append(str(cards[i]))
            dfs(number_list,i)
            number_list.pop()
            check[i]=False # => 탐색후 탐색한 위치를 False값으로 만들어줌


card=int(input())
k=int(input())
cards=[]
for i in range(card):
    tmp=int(input())
    cards.append(tmp)

answer_list=set()
check=[0]*card
dfs([],0)
answer_list=sorted(answer_list)
print(len(answer_list))