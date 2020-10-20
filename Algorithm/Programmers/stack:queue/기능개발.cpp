// 문제가 개편되었습니다. 이로 인해 함수 구성이나 테스트케이스가 변경되어, 과거의 코드는 동작하지 않을 수 있습니다.
// 새로운 함수 구성을 적용하려면 [코드 초기화] 버튼을 누르세요. 단, [코드 초기화] 버튼을 누르면 작성 중인 코드는 사라집니다.
#include <string>
#include <vector>
#include <iostream>

using namespace std;

vector<int> solution(vector<int> progresses, vector<int> speeds) {
   
    vector<int>rest_day;   
    vector<int>answer;
    
    for(int i=0;i<progresses.size();i++){
        int rest=100-progresses[i];
       
        if(rest%speeds[i]==0){
             rest_day.push_back(rest/speeds[i]);
        }
        else{ 
          rest_day.push_back(rest/speeds[i]+1); //남은일수       
        }
     }
    
    vector<int>queue;

    
    queue.push_back(rest_day[0]);
    
    for(int i=1;i<rest_day.size();i++){
        if(queue.front()>=rest_day[i]){
            queue.push_back(rest_day[i]);
        }
        else{
            answer.push_back(queue.size());
            queue.clear();
            queue.push_back(rest_day[i]);
        }
    }
    
    if(queue.size()!=0){
        answer.push_back(queue.size());
    }
    
    
        
    
    return answer;
}