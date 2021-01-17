def max_left_weight(cur):
    global gidung,min_left

    idx=cur

    max_height=0
    while idx>=min_left:
          if gidung[idx]>max_height:
             max_height=gidung[idx]

          idx-=1

    return max_height

def max_rights_weight(cur):
    global gidung,max_right

    idx=cur
    max_height=0
    while idx<=max_right:
          if gidung[idx]>max_height:
             max_height=gidung[idx]

          idx+=1

    return max_height


n=int(input())


gidung={}
min_left=9999
max_right=0
while n!=0:
      pos,height=map(int,input().split())
      if pos not in gidung:
          gidung[pos]=height
      min_left=min(pos,min_left)
      max_right=max(pos,max_right)
      n-=1


for i in range(min_left,max_right+1):
    if i not in gidung:gidung[i]=0


left=min_left
right=max_right

answer=0
while left<=right:
      max_h=min(max_left_weight(left),max_rights_weight(left))

      if max_h==0:
         answer+=gidung[left]
      else:
          answer+=max_h


      left+=1



print(answer)