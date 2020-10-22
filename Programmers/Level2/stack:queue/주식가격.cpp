#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> prices) {
    
    vector<int>answer;
    
    for(int i=0;i<prices.size();i++){
        int price=prices[i];
        int cnt=0;
    
        for(int j=i+1;j<prices.size();j++){
            if(prices[j]>=price){ //주식가격이 작으면 상승세이므로
                cnt++;
            }
            else{
                cnt++;
                break;
            }
        }
        answer.push_back(cnt);
        
    }
    
    
    
    
    
    return answer;
}