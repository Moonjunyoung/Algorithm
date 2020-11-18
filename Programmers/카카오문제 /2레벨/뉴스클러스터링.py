## 69점 맞음  다음에 다시 풀예정 

def check2(a,b):
    for s1 in a:
        if s1 in b:
            continue
        else:
            return False
   
    return True

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



    
    intersection=set(a)&set(b)
    union= (len(a)+len(b))-len(intersection)
    
    
    if len(a)==0 and len(b)==0:
        return 65536

    if check2(a,b):
        answer = min(len(a),len(b)) / max(len(a),len(b))
        answer = int(65536 * answer)

    else:
        answer=len(intersection)/union
        answer=int(65536*answer)
        
    
    return answer