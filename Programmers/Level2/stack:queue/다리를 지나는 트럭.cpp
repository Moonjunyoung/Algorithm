#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <iostream>

using namespace std;


 //테스트케이스 일부 실패 다시풀어야함

 
int solution(int bridge_length, int weight, vector<int> truck_weights) {
    int answer = 0;
    int bridge_weight=0; //다리 하중무게
    int time=0; //시간
    
    stack<pair<int,int>>bridge;
    
    
    int next_time=0;
    
      
    for(int i=0;i<truck_weights.size();i++){
        if(truck_weights[i]+bridge_weight<=weight){ //다리에 들어갈수있는조건
            bridge.push(make_pair(truck_weights[i],++time)); //다리에 들어갔음
            bridge_weight+=truck_weights[i]; //가중치 증가.
            next_time=time+bridge_length;  //다리에 차가 꽉찼을떄 다음시간을갱신하기위함
        }
        else{ //못들어가는조건
            
            while(true){
                if(next_time==time){ //다음 차가 들어가는시간이되면
                    bridge_weight-=bridge.top().first;
                    bridge.push(make_pair(truck_weights[i],time)); //다리에 들어갔음                
                    next_time=time+bridge_length;
                    bridge_weight+=truck_weights[i];
                    
                    break;
                }
                time++;
            }
        }
    }    

  
    time=bridge.top().second+bridge_length;
    
 
    
    
    
    
    
    return time;
}