def conversion(s):
    number=int(s)
    number_2=[]
    while number!=0:
          number_2.append(number%2)
          number=number//2
    tmp=""
    for string in number_2:tmp+=str(string)
    return tmp[::-1]
def solution(s):
    answer = []
    cnt=0
    result=0
    while s!='1':
        size=len(s)
        s=s.replace('0',"") #1. 0을 다제거
        size-=len(s) #2. 0을제거한후 길이
        result+=size #2. 0을제거한 길이 누적
        s=str(conversion(len(s))) #3.2진변환
        cnt+=1 #4. 이진변환 횟수 증가
        
 
    return [cnt,result]