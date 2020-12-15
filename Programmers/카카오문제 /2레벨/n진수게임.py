## 2번 풀었음


def conversion_number(number,base,number_list):
    tmp_number='0123456789ABCDEF'
    tmp_list=[]
    while number!=0:
          a=number%base
          a=tmp_number[a]
          tmp_list.append(a)
          number=number//base

    if len(tmp_list)==0:
        number_list.append(number)
        return

    tmp_list.reverse()
    for i in tmp_list:number_list.append(i)

def find_answer(p,m,number_list,c):
    answer_list=[]
    cnt=1
    idx=0
    while idx<c:
          if cnt>m:
             cnt=1

          if cnt==p:
              answer_list.append(number_list[idx])

          idx+=1
          cnt+=1

    return answer_list



def solution(n, t, m, p):
    answer = ''
    number_list=[]
    start_number=0
    while t*m>len(number_list): # t*m = 게임을 진행할동안의숫자
          conversion_number(start_number,n,number_list)
          start_number+=1

    answer_list=find_answer(p,m,number_list,t*m)
    for i in answer_list:answer+=str(i)
    return answer

