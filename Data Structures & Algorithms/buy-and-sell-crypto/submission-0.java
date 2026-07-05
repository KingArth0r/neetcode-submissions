class Solution {
    public int maxProfit(int[] prices) {
        if (prices.length < 2) return 0;
        int max = 0;
        int left = 0;
        int right = 1;

        while (right < prices.length) {
            if (prices[right] > prices[left]) {
                max = Math.max(max, prices[right] - prices[left]);
                right++;
            } else {
                left = right;
                right++;
            } 
        }
        return max;
    }
}
