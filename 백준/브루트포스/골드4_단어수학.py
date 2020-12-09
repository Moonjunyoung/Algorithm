n=int(input())
word_list=[]
alpha=[0]*26

while n!=0:
    s=input()
    word_list.append(s)
    n-=1

for i in word_list: # 1. 단어들 가지고 최대 비용을 구함
    cnt=0
    for j in range(len(i)-1,-1,-1): # 2. 맨뒤에 숫자부터 10의 0승부터해서 해당 알파벳의숫자를 채움
        idx=ord(i[j])-65
        alpha[idx]+=pow(10,cnt) # 더하는 이유는 단어들중에 서로 같은게 존재할수있으므로
        cnt+=1

alpha.sort(reverse=True) ##역순으로 정렬 (그래야 큰게 맨앞으로 옴)

answer=0
cnt=9
for i in alpha:
    answer+=cnt*i
    cnt-=1

print(answer)