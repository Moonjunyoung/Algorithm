import collections

## 다른 사람 꺼 코드 참조

def check(s):
    for i in s:
        a=str(i)
        if a.isalpha():
            continue
        else:
            return False

    return True


def solution(str1, str2):
    answer = 0
    
    
    a=[]
    b=[]
    for idx in range(len(str1)-1):
        tmp=str(str1[idx:idx+2])
        if check(tmp):
            tmp=tmp.upper()
            a.append(tmp)

    for idx in range(len(str2)-1):
        tmp=str(str2[idx:idx+2])
        if check(tmp):
            tmp=tmp.upper()
            b.append(tmp)

     #1. 위에 까진 문자열 처리 부분
    
    
    a=collections.Counter(a) ## 2. a,b 안의 문자의 개수를 셈
    b=collections.Counter(b)
    
    intersection=a&b ##3.교집합
    union=a|b ##4. 합집합
    
    intersection=sum(list(intersection.values())) ##5.교집합 내부의 원소개수를셈
    union=sum(list(union.values())) ##5. 합집합 내부의 원소개수를 셈
    
    if union ==0 and intersection==0: ##둘의 개수가 0개이면 
        return 65536
    
    
    return int(intersection/union * 65536)