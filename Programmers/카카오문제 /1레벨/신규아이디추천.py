def first_vaild(string):
    tmp=list(string)
    for i in range(len(tmp)):
        s=str(tmp[i])
        if s.isalpha():
            s=s.lower()
            tmp[i]=s

    return "".join(tmp)

def second_vaild(string):
    tmp=""
    for i in string:
        if str(i).isalpha() or str(i).isnumeric() or str(i)=='-' or str(i)=='_' or str(i)=='.':
           tmp+=i

    return tmp
def three_vaild(string):
    tmp=list(string)
    cnt=0
    a=""
    for i in range(len(tmp)):
        if tmp[i]=='.':
            cnt+=1
        else:
             if cnt>=2:
                a+='.'
                cnt=0

             if cnt>=1:
                a+='.'
                cnt=0
             a+=tmp[i]

    if cnt>=1:a+='.'

    return a

def four_vaild(string):
    tmp=list(string)
    a="".join(string)
    if tmp[0]=='.':
       a="".join(tmp[1:])

    if tmp[len(tmp)-1]=='.':
         a="".join(tmp[0:len(tmp)-1])

    if tmp[0]=='.' and tmp[len(tmp)-1]=='.':
         a="".join(tmp[1:len(tmp)-1])

    return a

def five_vaild(string):
    if len(string)==0:
        string+='a'

    return string

def six_vaild(string):
    a=""
    if len(string)>=16:
       a=four_vaild(string[0:15])
       return a

    return string

def seven_vaild(string):
    tmp=list(string)
    a=tmp[len(tmp)-1]
    if len(tmp)<=2:
       while len(tmp)<3:
             tmp.append(a)


    return "".join(tmp)





def solution(new_id):
    answer = ''
    new_id=first_vaild(new_id)
    new_id=second_vaild(new_id)
    new_id=three_vaild(new_id)
    new_id=four_vaild(new_id)
    new_id=five_vaild(new_id)
    new_id=six_vaild(new_id)
    new_id=seven_vaild(new_id)

    answer=new_id

    return answer