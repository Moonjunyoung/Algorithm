from collections import deque


def prime_list(n):
    sieve = [True] * n
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:
            for j in range(i + i, n, i):  # i 이후, i 의 배수를 False 판정
                sieve[j] = False
    return [i for i in range(2, n) if sieve[i] == True]  # 소수 목록


prime_number=[]
# 1. 소수를 생성하는 코드 
tmp=prime_list(9999)
for i in tmp:
    if i>=1000:
        prime_number.append(i)


t=int(input())

while t!=0:
    answer=999999999
    check = [False] * 10001
    a,b=map(int,input().split())
    queue=deque()
    queue.append([a,0])
    check[a]=True
    flag=False

    # 2. 소수변환과정 원하는 소수까지 bfs를 이용하여 최소 비용을 구함
    while queue:
        cur_number, cur_cnt=queue.popleft()
        if cur_number==b: # 3.원하는 소수가 나오면 해당 소수까지 이동비용을 구함
            print(cur_cnt)
            flag=True
            break

        cur_number=str(cur_number)
        for i in range(4):
            for j in range(10):
                new_number=cur_number[:i]+str(j)+cur_number[i+1:] # 4. 현재 숫자로부터 해당 자리의 한글자만바꿈
                new_number=int(new_number)
                if new_number<1000 or new_number>=10000:continue # 4-1 1000미만 10000이상인경우 다음으로넘김
                if new_number not in prime_number:continue # 4-2 소수가 아니여도 넘김
                if check[new_number]==False: # 4-3 미방문일시만 방문
                    check[new_number]=True
                    queue.append([new_number,cur_cnt+1]) #갱신

    if flag==False:
        print('Impossible')

    t-=1