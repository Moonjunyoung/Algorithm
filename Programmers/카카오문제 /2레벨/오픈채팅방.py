def solution(record):
    answer = []
    user_name={}
    
    # 1. 딕셔너리에 enter와 change 명령어가 들어올떄마다 유저 id를갱신
    for s in record:
        tmp=s.split(' ')

        if tmp[0]=='Enter':
            user_name[tmp[1]]=tmp[2]

        elif tmp[0]=='Change':
            user_name[tmp[1]]=tmp[2]

    #2. 갱신된 유저 id가지고 이제 채팅방 내용 출력
    for s in record:
        tmp=s.split(' ')
        if tmp[0]=='Enter':
            answer.append(user_name[tmp[1]]+"님이 들어왔습니다.")
        elif tmp[0]=='Leave':
            answer.append(user_name[tmp[1]]+"님이 나갔습니다.")
    
    return answer