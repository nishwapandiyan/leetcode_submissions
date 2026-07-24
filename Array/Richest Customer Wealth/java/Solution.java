class Solution {
    public int maximumWealth(int[][] accounts) {
        int max_wealth = 0;
        for(int[] ch : accounts){
             int sum =0;
            for (int row : ch){
                 sum+=row;
            }
            if (sum > max_wealth){
                max_wealth = sum;
            }

        }
        return max_wealth;
    }
}