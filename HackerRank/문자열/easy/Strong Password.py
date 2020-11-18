#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumNumber function below.
def minimumNumber(n, password):
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"
    check = [0, 0, 0, 0]
    answer = 0


    ## 해당 패스워드가 위 조건을 만족하는지 체크
    for str in password:
        if str in numbers:
            check[0] = 1
        elif str in lower_case:
            check[1] = 1
        elif str in upper_case:
            check[2] = 1
        elif str in special_characters:
            check[3] = 1
            

    ## 만족 안하는값들을 더해줌        
    cnt = 0
    for num in check:
        if num==0:
            cnt+=1

    ##패스워드 길이가 6보다 작은경우
    if (n < 6):
        answer += cnt ## 필요한값들을 더해주고
        n += cnt
        while (n < 6): ##문자열이 채워질떄까지 필요한 문자수를 더함
            answer+=1
            n += 1


    else:
        answer += cnt

    return answer
