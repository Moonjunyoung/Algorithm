def distance(cur_x,cur_y,target_x,target_y):
    return abs(target_x-cur_x)+abs(target_y-cur_y)
consonant={'z':(0,0),'x':(0,1),'c':(0,2),'v':(0,3),'a':(1,0),'s':(1,1),'d':(1,2),'f':(1,3),'g':(1,4),'q':(2,0),'w':(2,1),'e':(2,2),'r':(2,3),'t':(2,4)}
vowel={'b':(0,4),'n':(0,5),'m':(0,6),'h':(1,5),'j':(1,6),'k':(1,7),'l':(1,8),'y':(2,5),'u':(2,6),'i':(2,7),'o':(2,8),'p':(2,9)}
l,r=map(str,input().split())
word=input()
cur_l_x,cur_l_y=consonant[l]
cur_r_x,cur_r_y=vowel[r]
cost=0
for i in word:
    target_x,target_y=0,0
    if i in consonant: # 자음 왼손검지
        target_x,target_y=consonant[i]
        cost+=distance(cur_l_x,cur_l_y,target_x,target_y)
        cur_l_x,cur_l_y=target_x,target_y
        cost+=1

    elif i in vowel: # 모음 오른손검지
         target_x,target_y=vowel[i]
         cost+=distance(cur_r_x,cur_r_y,target_x,target_y)
         cur_r_x,cur_r_y=target_x,target_y
         cost+=1

print(cost)