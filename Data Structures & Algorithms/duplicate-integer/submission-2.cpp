class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        std::set<int> seen;
        for (int& n : nums) {
            if (seen.find(n) != seen.end()) return true;
            auto _ = seen.insert(n);
        }
        return false;
    }
};
