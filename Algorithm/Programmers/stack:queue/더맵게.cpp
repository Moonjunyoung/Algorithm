#include <string>
#include <vector>
#include <queue>
#include <iostream>


using namespace std;

int solution(vector<int> scoville, int K) {
    int answer = 0;

    priority_queue<int, vector<int>, greater<int>> pq; //최소힙
    
    for(int i=0;i<scoville.size();i++){
        pq.push(scoville[i]); //스코빌지수를 넣음
    }
    
    while(!pq.empty()){
        int top=pq.top();
        pq.pop();
        
        if(top<K){
            if(pq.empty()){ //만들수없는경우
                answer=-1;
                break;
            }
            else{ //만들수있는경우
            int mixed=top+pq.top()*2;
            pq.pop();
            
            pq.push(mixed); //섞은음식을 넣음  
            answer++;
            }
        }
        
        else{
            break;
        }
        
        
    }
    

        
        
    return answer;
}