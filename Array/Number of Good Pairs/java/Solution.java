class Solution {
    public int numIdenticalPairs(int[] nums) {
        int[] count = new int[101]; // since 1 <= nums[i] <= 100
        int result = 0;
        
        for (int num : nums) {
            result += count[num];
            count[num]++;         
        }
        
        return result;
    }
}
