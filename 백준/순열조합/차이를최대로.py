import itertools
n=int(input())
number_list=list(map(int,input().split()))

number_list.sort()
permute_number_list=list(itertools.permutations(number_list,n))  
#=>순열(원소의 값이 같더라도 순서가 서로다르면 서로다른원소 취급함)
#순열 사용이유 => 리스트내에 숫자들의 순서가 바뀌는것을 고려하므로 순열을 사용 ()

answer=0



for i in permute_number_list:
    sum=0
    for j in range(n-1):
        sum+=abs(i[j]-i[j+1])

    answer=max(sum,answer)





print(answer)