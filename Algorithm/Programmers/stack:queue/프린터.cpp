#include <vector>
#include <algorithm>
#include <string>
#include <queue>
#include <functional>
#include <iostream>
using namespace std;

int solution(vector<int> priorities, int location) {
  
   priority_queue<int> pq; //우선순위큐 priorities (우선순위를 담는다.)
   queue<pair<int,int>>q; // first = loc ,second = priorities
    
   for(int i=0;i<priorities.size();i++){
       q.push(make_pair(i,priorities[i])); //loc와 우선순위를넣음
       pq.push(priorities[i]); //우선순위를 맞춰줌
   }
   
   
    int rank=0;

    
    while(!q.empty()){
        int loc=q.front().first; //location
        int prioritie=q.front().second; //우선순위
        q.pop();
        
        if(prioritie==pq.top()){ //우선순위가맞으면
            rank++; 
            pq.pop();
            if(loc==location){ //찾고자하는 위치면
                break;
            }
        }
        else{ //우선순위가 틀리면 맨뒤로
            q.push(make_pair(loc,prioritie));
        }
    }
        
    
    
    
    
    return rank;
}