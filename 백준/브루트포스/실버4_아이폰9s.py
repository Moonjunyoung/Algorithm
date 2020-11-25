n=int(input())
phone=[]
unique_number=set()
for i in range(n):
    a=int(input())
    phone.append(a)
    unique_number.add(a)


answer=0
for i in unique_number:
    cnt=0
    start=0
    check = [0] * n
    for j in range(len(phone)): ##구간별 최대값구하기
        if i==phone[j]:continue
        if phone[start]==phone[j]: #지정한 값과 해당값이 값이 같으면 증가후 해당구간에 증가한값을넣음
            cnt+=1
            check[j]=cnt
        else: ##다를경우 현재구간부터 다시시작
            cnt=1
            check[j]=cnt
            start=j
    tmp=max(check)
    answer=max(answer,tmp)

print(answer)

