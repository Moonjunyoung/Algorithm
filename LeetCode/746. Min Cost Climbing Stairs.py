class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp=[0]*len(cost)
        dp[0]=cost[0]
        dp[1]=cost[1]
        for i in range(2,len(cost)):
            dp[i]=cost[i]+dp[i-1] # 한칸씩올라오는경우
            dp[i]=min(dp[i],cost[i]+dp[i-2]) # 두칸씩올라오는경우


        answer=min(dp[len(cost)-1],dp[len(cost)-2])
        return answer