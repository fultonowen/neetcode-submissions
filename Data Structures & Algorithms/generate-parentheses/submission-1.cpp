class Solution {
public:
    vector<string> generateParenthesis(int n) {
        vector<string> ans;
        std::string curr = "";
        
        backtrack(ans, curr, 0, 0, n);
        return ans;
    }

    void backtrack(vector<string>& sol, std::string curr, int leftCount, int rightCount, int n) {
    
        if (leftCount + rightCount == 2 * n) {
            sol.push_back(curr);
            return;
        }

        if (leftCount < n) {
            curr.push_back('(');
            backtrack(sol, curr, leftCount+1, rightCount, n);
            curr.pop_back();
        }

        if (rightCount < leftCount) {
            curr.push_back(')');
            backtrack(sol, curr, leftCount, rightCount+1, n);
            curr.pop_back();
        }
    }
};
