class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int n = nums.size();
        vector<int> product(n+1, 1), ans(n);
        for (int i = 0; i < n; i++) {
            product[i+1] = product[i] * nums[i];
        }
        int d=1;
        for (int i = n-1; i>=0; i--) {
            ans[i] = product[i] * d;
            d *= nums[i];
        }
        return ans;
    }
};
