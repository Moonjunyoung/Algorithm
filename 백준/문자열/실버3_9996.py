
# 다른사람 코드 보고 배움

# 솔루션 
#  1. *를 기준으로 앞과 뒤를 split 하여 들어오는 문자열의 앞과 뒤를 비교하여 같아야하며
# 2. 들어오는 문자열의길이가 패턴스트링보다 커야한다.


n=int(input())
pattern_str=input().split('*')


front=pattern_str[0] ## *기준으로 앞에있는 문자
back=pattern_str[1] # *기준으로 뒤에있는문자

while n!=0:
    s=input()
    #입력으로 들어온 문자열의 front 와 back이 pattern_str과 같고  입력으로 들어온 문자값이 패턴스트링 길이보다 크거나 같을떄성립
    if s[:len(front)]==front and s[-len(back):]==back and len("".join(pattern_str))<=len(s):
        print("DA")
    else:
        print("NE")
    n-=1
