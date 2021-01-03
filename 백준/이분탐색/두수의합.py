def binary_search(value,idx):
    global number_list,x
    start=idx+1
    end= len(number_list)-1
    while start<=end:
          mid=(start+end)//2
          total=value+number_list[mid]
          if total==x:
              return True

          if total<x:
               start=mid+1
          elif total>x:
               end=mid-1

    return False


n=int(input())
number_list=list(map(int,input().split()))
x=int(input())
answer=0
number_list.sort()

for i in range(len(number_list)):
    if binary_search(number_list[i],i):
        answer+=1

print(answer)