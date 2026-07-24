class Solution {
    public int[] getSneakyNumbers(int[] nums) {
        int arr[] = new int[2];
        int freq[] = new int[101];
        int ind = 0;
        for(int i:nums){
            freq[i]++;
            if(freq[i] > 1) arr[ind++] = i;
        }
        return arr;
    }
}