#include <string>
#include <vector>
#include <iostream>
#include <unordered_map>

using namespace std;

vector<int> solution(int n, vector<string> words) {
    vector<int> answer;   
    unordered_map<string,int>hash_map; //key value
 
    int turn=1;
    int cnt=1;
    
    hash_map[words[0]]=cnt; 
    cnt++;
    
    for(int i=1;i<words.size();i++){    
        if(cnt>n){
            cnt=1;
            turn++;
        }
        
       if(words[i][0] != words[i-1][words[i-1].size()-1] || hash_map[words[i]]){ //현재단어와 이전단어 끝이안맞는경우 or 아이템이 존재하는경우
          answer.push_back(cnt);
          answer.push_back(turn);
          return answer;
       }
       else{
        hash_map[words[i]]=cnt; 
        cnt++;
       }
        
    }
    
    return {0,0};
}