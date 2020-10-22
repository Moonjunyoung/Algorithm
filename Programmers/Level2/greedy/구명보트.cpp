#include <string>
#include <vector>

#include <algorithm>
#include <functional>
#include <iostream>

using namespace std;



int solution(vector<int> people, int limit) {
    int answer = 0;
   
    
    sort(people.begin(), people.end()); //오름차순정렬

    int left=0;
    int right=people.size()-1;
    
    while(left<=right){
        if(people[left]+people[right]>limit){ //가장가벼운사람 + 가장무거운사람 
            right--;
        }else{ //인원이초과안한경우 한쌍을이룸
            left++;
            right--;
        }
         answer++;
    }
    
    
    
    
    return answer;
}