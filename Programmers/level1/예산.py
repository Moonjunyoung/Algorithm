def solution(d, budget):
    answer = 0
    d.sort()
    s=0
    idx=0
    while idx<len(d):
          if s+d[idx]>budget:
              break
          s+=d[idx]
          idx+=1

    return idx