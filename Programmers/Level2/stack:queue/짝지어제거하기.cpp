#include <iostream>
#include<string>
#include<stack>

using namespace std;

int solution(string s)
{
    int answer = 0;
    
    stack<char>st;
    
    for(int i=0;i<s.size();i++){
        if(!st.empty() && s[i]==st.top()){//제거가능
            st.pop();
        }
        else{ //제거불가
            st.push(s[i]);
        }
    }
    
    if(st.empty()){
       answer=1; 
    }
    else{
        answer=0;
    }
      
    
    
    
    
    

    return answer;
}