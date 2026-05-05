class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int maxProfit = 0;
        int profit;
        int left = 0, right;
        for (right = 1; right < prices.size(); right++) {
            profit = prices[right] - prices[left];
            maxProfit = std::max(maxProfit, profit);
            while (prices[right] - prices[left] <0) {
                left++;
            }
        }
        return maxProfit;
    }
};
