import itertools



while True:
    a=list(map(int,input().split()))
    n=a[0]
    if n==0:break
    lotto_number=a[1:]
    tmp_number=[]

    lotto_combination=list(itertools.combinations(lotto_number,6)) ##1. 조합사용 
    #6개를 뽑아야하는데 총 숫자는 그이상이 들어오는데 값이 다다름  즉 원소들의 조합을 이용해서 만들수있음 
    for i in lotto_combination:
        for j in i:
            print(j,end=' ')
        print()

    print()

