import copy

# 백트래킹 문제 나중에 다시풀어보기

def dfs(start,check,tickets,answer,temp):

    if len(temp) ==len(tickets)+1: ## 1. 모두 이동한경우 (무조건 정답일수밖에없음)
        answer=copy.copy(temp)
        return answer



    for i in range(len(tickets)):
        if tickets[i][0]==start and check[i]==False:
            check[i]=True
            temp.append(tickets[i][1])
            a=dfs(tickets[i][1],check,tickets,answer,temp)
            if a!=False: ## 2. 올바르지 않은 경로는 무조건 False를 반환하므로
                return a

            check[i]=False
            temp.pop()


    return False

def solution(tickets):
    answer = []
    temp=[]
    check=[False]*len(tickets)
    tickets.sort() ## 1. 알파벳을 사전순으로 고려하므로 정렬을 했음

    temp.append('ICN') # ICN 부터 출발함
    answer=dfs('ICN',check,tickets,answer,temp)



    return answer



#solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]])
solution([['ICN', 'A'], ['A', 'C'], ['A', 'D'], ['D', 'B'], ['B', 'A']])