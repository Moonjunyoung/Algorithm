s=input()
word_list=[]

for i in range(len(s)):
    for j in range(i+1,len(s)):
        for z in range(j+1,len(s)):
            first=s[i:j]
            second=s[j:z]
            thrid=s[z:]

            if len(first+second+thrid)==len(s):
               word_list.append(first[::-1]+second[::-1]+thrid[::-1])

word_list.sort()
print(word_list[0])