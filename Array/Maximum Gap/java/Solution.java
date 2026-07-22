class Solution {
    public int maximumGap(int[] nums) {
        if (nums.length < 2) return 0;

      
        radixSort(nums);

        int maxGap = 0;
        for (int i = 1; i < nums.length; i++) {
            maxGap = Math.max(maxGap, nums[i] - nums[i - 1]);
        }
        return maxGap;
    }

    private void radixSort(int[] nums) {
        int max = Integer.MIN_VALUE;
        for (int num : nums) {
            if (num > max) max = num;
        }

        int exp = 1;
        int n = nums.length;
        int[] aux = new int[n];

        while (max / exp > 0) {
            int[] count = new int[10];

           
            for (int num : nums) {
                count[(num / exp) % 10]++;
            }

            for (int i = 1; i < 10; i++) {
                count[i] += count[i - 1];
            }

            for (int i = n - 1; i >= 0; i--) {
                int digit = (nums[i] / exp) % 10;
                aux[--count[digit]] = nums[i];
            }

            System.arraycopy(aux, 0, nums, 0, n);
            exp *= 10;
        }
    }
}
