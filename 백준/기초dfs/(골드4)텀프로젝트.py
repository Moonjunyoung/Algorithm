import sys
sys.setrecursionlimit(111111)


#싸이클이 형성하는 지 찾는다


def dfs(start):
    global graph,check,done,cnt
    check[start]=True


    next=graph[start]

    if check[next]==False: ##방문하지 x 방문
        dfs(next)
    else:
        if done[next]==False:
            i=next
            while i!=start: ##싸이클이 형성되는지확인
                  cnt+=1
                  i=graph[i]
            cnt+=1

    done[start]=True
    #해당 정점이 수행이 완료됬다는것 (다음번 탐색시 영향 x 어차피 싸이클은 무조건 정점을 탐색하면서 발생하므로 다음번에 탐색할필요 x)





n=int(input())

while n!=0:
    member=int(input())
    graph=[0]*(member+1)


    cnt=0

    tmp=list(map(int,input().split()))

    done = [False] * (member + 1)
    check = [False] * (member + 1)

    for i in range(member):
        graph[i+1]=tmp[i]

    for i in range(1,member+1):
        if check[i]==False:
            dfs(i)


    print(member-cnt) ## cnt =싸이클이 형성된 사람수 즉 팀원수



    n-=1
