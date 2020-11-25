word=input()
find_word=input()


idx=0
answer=0

while idx< len(word):
     tmp= word[idx:idx+len(find_word)] #찾으려는 단어의글자만큼끊고 
     if tmp==find_word: ##글자가같으면 
         idx=idx+len(find_word) ##해당글자인덱스만큼뛴다
         answer+=1

     else: ##글자가 같지않으면 
          idx+=1 ##현재 인덱스한개추가

print(answer)