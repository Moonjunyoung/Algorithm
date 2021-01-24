import itertools
t=int(input())

while t!=0:
      number=int(input())
      s=0
      idx=1
      number_list=[]
      while True:
            s+=idx
            if s>number:break
            number_list.append(s)
            idx+=1

      number_list=list(itertools.combinations_with_replacement(number_list,3))
      flag=False
      for i in number_list:
          s=0
          for j in i:
              s+=j
          if s==number:
             flag=True
             break

      if flag:
          print(1)
      else:
          print(0)

      t-=1