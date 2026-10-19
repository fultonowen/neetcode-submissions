impl Solution {
    pub fn divide_array(mut nums: Vec<i32>, k: i32) -> Vec<Vec<i32>> {
        let capacity = nums.len() / 3;
        let mut ans : Vec<Vec<i32>> = Vec::with_capacity(capacity);
        nums.sort();
        for i in (2..nums.len()).step_by(3) {
            if nums[i] - nums[i-2] > k {
                return vec![];
            }
            ans.push(vec![nums[i-2], nums[i-1], nums[i]]);
        }
        ans
    }
}
