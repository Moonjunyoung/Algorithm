#include <string>
#include <vector>

using namespace std;

int answer=0;

bool check(string a,string b){
    int idx=0;
    int cnt=0;
   
    while(idx<a.size()){
        if(a[idx]==b[idx]){
            cnt++;
        }
        idx++;
    }
    if(cnt==a.size()-1){
        return true;
    }
    return false;
}


void dfs(string begin,string target,vector<string>&words,int cnt){
    
    if(check(begin,target)){
        answer++;
        return;
    }
      if(cnt>words.size()){
        answer=0;
        return;
    }
    
    else{
        if(check(begin,words[cnt])){
            answer++;    
            dfs(words[cnt],target,words,cnt+1);
        }
        else{
            dfs(begin,target,words,cnt+1);
        }
    }
    
    
}


int solution(string begin, string target, vector<string> words) {
    
    
    bool flag=true;
    for(int i=0;i<words.size();i++){
        if(words[i]==target){
            flag=false;
        }
    }
    
    if(!flag){
        dfs(begin,target,words,0);
        
    }
    else{
        answer=0;
    }
    
    
    
    
    
    
    
    return answer;
}