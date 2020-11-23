def check(number_list):
    global n,equal_number

    for i in range(len(number_list)-1):
        a=equal_number[i]
        if a=='<':
            if number_list[i]>number_list[i+1]:
                return False
        elif a=='>':
            if number_list[i] < number_list[i + 1]:
                return False

    return True


def dfs(number_list):
    global max_number,min_number,n,check_number
    if len(number_list)==n+1:
        if check(number_list):
            max_number=max(sum(number_list),max_number)
            min_number=min(sum(number_list),min_number)
            tmp=[]
            for i in number_list:tmp.append(i)
            ansewr_list.append((tmp,sum(number_list)))
        return

    else:
        for i in range(10):
            if check_number[i]==False:
                check_number[i]=True
                number_list.append(i)
                dfs(number_list)
                check_number[i]=False
                number_list.pop()




n=input()
equal_number=input().split(' ')
n=int(n)
max_number=0
min_number=999999999999
ansewr_list=[]
check_number=[False]*10

dfs([])

min_value=min(ansewr_list)
max_value=max(ansewr_list)
tmp=""
for i in max_value[0]:tmp+=str(i)
print(tmp)
tmp=""
for i in min_value[0]:tmp+=str(i)
print(tmp)