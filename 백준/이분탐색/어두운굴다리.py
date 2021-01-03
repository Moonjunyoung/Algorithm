def isPossible(height):
    global garo_pos,n
    cur_pos=0
    for i in garo_pos:
        if cur_pos+height>=i:
            cur_pos=i+height #다음에 설치할곳의 위치
        else:
            return False

    if cur_pos>=n: ##가로등위치내에 설치가 다된경우
        return True

    return False

n=int(input())
m=int(input())
garo_pos=list(map(int,input().split()))

start=1
end=n
answer=99999999
while start<=end:
      height=(start+end)//2
      if isPossible(height):
          answer=min(answer,height)
          end=height-1
      else:
          start = height + 1


print(answer)