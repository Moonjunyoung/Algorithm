def solution(brown, yellow):
    answer = []
    cnt = 1
    total = brown + yellow

    while True:

        garo = total // cnt # 가로 
        sero = cnt #세로를 구함



        check_garo = garo-2 # 2를 뻄
        check_sero = sero-2 #2를뻄

        if check_sero*check_garo==yellow: ##두개 곱이 노랑색이랑 같으면
            answer.append(garo)
            answer.append(sero)
            break



        cnt += 1

    return answer