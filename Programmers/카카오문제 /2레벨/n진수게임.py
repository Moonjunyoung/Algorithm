# 내 풀이에서 진법 변환과정에서 문제있음 53.5프로 
# 다른사람 conversion함수 참조


def conversion(n,num):
	if num==0:return "0"
	t="0123456789ABCDEF"
	ret=""
	while num>0:
		ret+=t[int(num%n)]
		num=int(num/n)

	return ret[::-1]




def solution(n, t, m, p):
    answer = ''
    answer_list=[]
    a=[]
    start_number=0
    while True:
        if t*m<=len(answer_list): ## m 은 멤버수 t = 표시할숫자 m * t면 표시할숫자를 만족할 개수가 됨
            while len(answer_list)!=t*m:answer_list.pop()
            cnt=1
            for s in answer_list:
                if cnt>m:cnt=1
                if cnt==p:a.append(s)
                cnt+=1
            break

        conversion_number=list(conversion(n,start_number)) #1. 진수변환
        while len(conversion_number)!=0:answer_list.append(conversion_number.pop(0))
        start_number+=1


    for tmp in a:answer+=str(tmp)

    return answer