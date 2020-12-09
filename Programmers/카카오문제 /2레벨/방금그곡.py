def conversion(melody): # 문자처리를 쉽게하기위해 소문자로 바꿔줌
    melody=melody.replace('C#','c')
    melody=melody.replace('D#','d')
    melody=melody.replace('F#','f')
    melody=melody.replace('G#','g')
    melody=melody.replace('A#','a')

    return melody

def time_to_min(time): # 1. 시간을 분으로 바꾼다.
    hour,min_t=time.split(':')
    hour=int(hour)*60
    min_t=int(min_t)
    return hour+min_t

def convert_time_melody(melody,time): ## 1. 멜로디를 해당 시간 만큼 만들고 그거만큼 잘라버린다. 
    tmp=(time//len(melody))+1
    melody=melody*tmp
    return melody[:time]

def find_answer(my_melody,target_melody): # 부분문자열에 답이 있는지 확인한다.
    idx=0
    while idx< len(target_melody):
          tmp=target_melody[idx:len(my_melody)+idx]
          if tmp==my_melody:
              return True

          idx+=1
    return False




def solution(m, musicinfos):
    m=conversion(str(m))
    title=[]
    title_time=[]

    for i in musicinfos:
        start_time,end_time,music_name,melody=i.split(',')
        time=abs(time_to_min(str(start_time))-time_to_min(str(end_time)))

        melody = conversion(melody)
        melody=convert_time_melody(melody,time)

        if find_answer(m,melody):
            title.append(music_name)
            title_time.append(time)

           
    if len(title)==0:
            return "(None)"
    elif len(title)==1:
            return title[0]
    else: ## 정답이 여러개인경우 가장 큰 시간값의 노래제목을 출력
        idx=title_time.index(max(title_time))
        return title[idx]




