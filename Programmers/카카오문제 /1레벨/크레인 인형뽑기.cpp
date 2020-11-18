#include <string>
#include <vector>
#include <stack>
#include <iostream>
using namespace std;

int solution(vector<vector<int>> board, vector<int> moves) {
    int answer = 0;
    
    stack<int>st;
    
    //int board_size=board.size();
    
 for(int i=0;i<moves.size();i++){   
      for(int j=0;j<board[0].size();j++){
         int doll=board[j][moves[i]-1];
        
          if(doll!=0){ 
           if(!st.empty()){ //인형을 없앨수있는경우 인형이 존재하면 해당위치에서 뽑아버림 
             if(st.top()==doll){
               answer++; 
               st.pop();
             } //인형을없앰
             else{ //못없애는경우 그냥넣음 
                st.push(doll);  
             } 
            }
         else{ //스택이 빈경우
            st.push(doll);   
          }
              
        board[j][moves[i]-1]=0;
        break;
      }
  }
 }
    
    return answer*2;
}