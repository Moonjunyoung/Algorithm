t=int(input())
t-=1
first_word=input()
word_list=[]
answer=0
for i in range(t):
    tmp=input()
    word_list.append(tmp)
# 1. 입력 받기

first_word_alpha = [0] * 26
# 첫번쨰 단어의 알파벳을 센다.
for i in first_word:first_word_alpha[ord(i)-65]+=1


# 2. 두개의 단어가 같은 종류의 문자로 이루어짐 dog = god (비슷한단어) ,
# God와 Good 단어개수차이가 1남 (추가또는 제거)

# 2-1 비교할 단어 목록들
for word in word_list:
    word_alpha=[0]*26
    for i in word:word_alpha[ord(i)-65]+=1 # 비교할단어

    many_word=0
    for i in range(26): # 2-2 단어수의 차이를 계산
        if first_word_alpha[i]>word_alpha[i]:
            many_word+=first_word_alpha[i]-word_alpha[i]

    small_word=0
    for i in range(26): #2-2 단어수의 차이를 계산
        if first_word_alpha[i]<word_alpha[i]:
            small_word+=word_alpha[i]-first_word_alpha[i]

    if many_word<=1 and small_word<=1: #
        answer+=1

print(answer)


