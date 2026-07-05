class Solution {
    public int longestConsecutive(int[] nums) {
        Set<Integer> set = new HashSet<>();
        if (nums.length < 2) return nums.length;

        int max = 1;
        for (int i : nums) {
            set.add(i);
        }
        for (int i : nums) {
            if (!set.contains(i - 1)) {
                int j = 1;
                while (set.contains(i + j)) {
                    j++;
                }
                max = Math.max(max, j);
            }
        }
        return max;
    }
}
