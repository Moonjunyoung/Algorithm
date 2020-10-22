

#include <iostream>
#include <algorithm>
#include <functional>
#include <vector>
#include <string>



bool solution(vector<string> phone_book) {
    bool answer = true;
    sort(phone_book.begin(),phone_book.end()); //정렬을해야 문자길이가 가장작은게 맨앞에 올수밖에없음

    for(int i=1;i<phone_book.size();i++){
        for(int j=0;j<phone_book[i].size();j++){
            string tmp=phone_book[i].substr(j,phone_book[0].length()); 
            //핵심부분 가장작은 접두어 길이끼리 짤라서 비교
            if(tmp==phone_book[0]){
                return false;
            }
        }
    }
