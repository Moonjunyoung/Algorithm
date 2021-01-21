n,p=map(int,input().split())

lines=[0]*7
for i in range(len(lines)):lines[i]=list()
answer=0
for i in range(n):
    line,p_number=map(int,input().split())

    if len(lines[line])==0: # 1. 누른게 없으면
       lines[line].append(p_number)
       answer+=1

    else:
         a=lines[line] # 2.누른게있따면
         p_n=a[-1]
         if p_n<p_number : # 현재 누르고 있는 플룻넘버보다 크면
             lines[line].append(p_number)
             answer+=1
         elif p_n>p_number: #현재 누르고 있는 플룻 넘버보다 작으면
              while len(a)!=0 and a[-1]>p_number:
                    lines[line].pop()
                    answer+=1

              if len(a)!=0 and a[-1]==p_number:continue # <- 이부분 예외처리해야됨 멜로디가 이미 존재하는경우
              lines[line].append(p_number)
              answer+=1

         else: #같으 면 conitnue
             continue


print(answer)