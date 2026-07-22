import java.util.Arrays;

class Solution {
    public void wiggleSort(int[] nums) {
        int n = nums.length;
        int[] sorted = nums.clone();
        Arrays.sort(sorted);

        int mid = (n + 1) / 2;  
        int j = mid - 1;        
        int k = n - 1;          

       
        for (int i = 0; i < n; i++) {
            nums[i] = (i % 2 == 0) ? sorted[j--] : sorted[k--];
        }
    }
}
