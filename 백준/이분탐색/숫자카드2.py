import bisect

n=int(input())
card_list=list(map(int,input().split()))
card_list.sort()

n1=int(input())
find_card_list=list(map(int,input().split()))

# 입력
for i in find_card_list:
    upper_bound_index=bisect.bisect_right(card_list,i) ## 해당 숫자를 삽입할 위치 오른쪽을 찾는다.
    lower_bound_index=bisect.bisect_left(card_list,i) ##해당 숫자를 삽입할 위치 왼쪽을 찾는다.
    print(upper_bound_index-lower_bound_index,end=' ')








