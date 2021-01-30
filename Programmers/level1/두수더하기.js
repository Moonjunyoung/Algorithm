function solution(numbers) {
    const answer =new Set()
    for(let i=0;i<numbers.length;i++){
        for(let j=0;j<numbers.length;j++){
            if(i===j){
                continue;
            }
            else{
                answer.add(numbers[i]+numbers[j])
            }

        }
    }
    let tmp=[]
    for(const item of answer){
        tmp.push(item)
    }

    tmp.sort(function (a,b){
        if (a>b) return 1;
        if (a==b) return 0;
        if(a<b) return -1;
    })

    return tmp;
}
solution([5,0,2,7]	)