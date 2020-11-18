#include <vector>
#include <iostream>
#include <set>
using namespace std;

int solution(vector<int> nums)
{
    int answer = 0;
     set<int>poketmon;
    
    for(int i=0;i<nums.size();i++){
        poketmon.insert(nums[i]);
    } //중복 필터링
    
    
    if(nums.size()/2<poketmon.size()){
        answer=nums.size()/2;
    }
    else{
        answer=poketmon.size();
    }
    
    return answer;
}