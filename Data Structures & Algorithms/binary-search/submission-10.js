class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number}
     */
    search(nums, target) {
        let l = 0
        let r = nums.length
        while (l < r) {
            let m = l + ((r - l) / 2) | 0;
            if (nums[m] > target) {
                // too big, shrink
                r = m
            } else {
                // too small, grow +1 to ensure we break loop
                // just make sure to return l - 1
                l = m + 1
            }
        }
        console.log(l);
        if (l > 0 && nums[l - 1] == target) return l - 1;
        else return -1;
    }
}
