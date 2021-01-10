import heapq
def solution(jobs):
    answer = 0
    cur_time=0
    cur_task_end_time=0
    priority_task=[]
    check=[False]*len(jobs)
    job_count=0
    job_flag=False
    job_requse_time=0
    jobs.sort()

    while job_count<len(jobs): # 1. 모든 작업이 끝날떄까지 수행
          for i in range(job_count,len(jobs)):
              if job_flag:break #수행 중인 작업이존재하면 빠져나감
              start_time,spend_time=jobs[i]
              if cur_time>=start_time and check[i]==False: # 2. 현재시간이 해당작업을 시간보다 커야됨
                  heapq.heappush(priority_task,(spend_time,start_time)) # 2.1 작업이시간이 짧은거 순으로넣음
                  check[i]=True

          if len(priority_task)!=0 and job_flag==False: # 3. 작업이 가능한게 존재하면
              spend_time,start_time=heapq.heappop(priority_task)
              job_requse_time=start_time
              cur_task_end_time=cur_time+spend_time # 작업 종료시간을 정한다.
              job_flag=True

          if cur_task_end_time==cur_time and job_flag: # 4. 작업을 끝낼수있는시간이 되면 
             job_flag=False
             job_count+=1
             answer+=cur_time-job_requse_time # 현재시간에서 작업의요청시간을 뺸다
             continue

          cur_time+=1


    return answer//job_count