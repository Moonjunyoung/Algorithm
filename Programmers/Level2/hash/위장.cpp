#include <string>
#include <vector>
#include <iostream>
#include <unordered_map>

using namespace std;

int solution(vector<vector<string>> clothes) {
    int answer = 0;
    
    unordered_map<string,int>hash_map; //해쉬맵 string= 옷이름 (key) int = 옷종류 개수 2
    
    
    for(int i=0;i<clothes.size();i++){
        for(int j=0;j<clothes[i].size();j++){
            if(j==1){ // //옷의 이름 =0 ,옷의종류=1    
                hash_map[clothes[i][1]]++; //key value
               
            }
        }
    }
 
    
    
    answer=1;
    for(auto & i:hash_map){ //해시맵요소 탐색
        answer+=answer*i.second; //옷을선택하는경우의수
    }
    
    

    //옷을 안입는경우를뺴줌
    return answer-1;
}