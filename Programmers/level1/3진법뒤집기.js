function solution(n) {;
    let answer=""

    while (n!=0){
        let tmp=n%3
        answer+=tmp.toString()
        n=n/3
        n=Math.floor(n)
    }
    let answer_number=0;
    for(let i=answer.length-1;i>=0;i--){
        answer_number+=Math.pow(3,(answer.length-1)-i)*parseInt(answer[i])
    }


    return answer_number;
}

solution(45)