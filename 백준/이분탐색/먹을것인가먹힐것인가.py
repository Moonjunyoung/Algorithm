t=int(input())
def lower_bound(a_number,b_list): 
    global answer
    left=0
    right=len(b_list)-1
    result=-1
    while left<=right:
          mid=(left+right)//2
          if b_list[mid]<a_number:
             result=mid
             left=mid+1
          else:
              right=mid-1

    return result


while t!=0:
      answer=0
      a_len,b_len=map(int,input().split())
      a=list(map(int,input().split()))
      b=list(map(int,input().split()))
      b.sort()
      for i in range(len(a)):
          answer+=lower_bound(a[i],b)+1


      print(answer)

      t-=1