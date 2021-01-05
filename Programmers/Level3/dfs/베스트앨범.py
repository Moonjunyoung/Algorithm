import operator


def sort_1(li):
    # -x[1]은 해당 장르의 노래리스트들을 큰순으로 정렬 ,그다음 고유번호가낮은순으로 정렬
    tmp = sorted(li, key=lambda x: (-x[1], x[0]))
    return tmp


def solution(genres, plays):
    answer = []
    total_play = {}
    genre_play = {}

    # 1. key = 장르 value = 해당장르의 음악들
    for i in range(len(genres)):
        if genres[i] not in genre_play:
            genre_play[genres[i]] = [[i, plays[i]]]
        else:
            genre_play[genres[i]].append([i, plays[i]])

    # 2. key= 장르 value = 해당장르의 총 음악재생횟수
    for i in range(len(genres)):
        if genres[i] not in total_play:
            total_play[genres[i]] = plays[i]
        else:
            total_play[genres[i]] += plays[i]

    # 3. 해당 장르의 총 음악 재생횟수 기준으로 오름차순정렬 (속한 노래가 많이 재생된장르)
    total_play = sorted(total_play.items(), key=operator.itemgetter(1), reverse=True)

    # 4. 속한노래가 많이 재생된장르 순으로 정렬되었으므로 이제 장르내에서 많이 재생된노래와 고유번호
    #낮은순으로 정렬을 시
    for i in total_play:
        tmp = sort_1(genre_play[i[0]])
        # 5. 베스트 앨범은 2개만 뽑아야한다 , 만약 2개미만일경우는 한개만 추가 
        if len(tmp) >= 2:
            answer.append(tmp[0][0])
            answer.append(tmp[1][0])
        else:
            answer.append(tmp[0][0])

    return answer