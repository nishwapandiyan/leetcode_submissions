class Solution {
    public int[] dailyTemperatures(int[] nums) {
        int arr[] = new int[nums.length];
        Stack<Integer> stack = new Stack<>();
        for(int i=0; i<nums.length; i++){
            while(!stack.isEmpty() && nums[stack.peek()] < nums[i])
            arr[stack.peek()] = i-stack.pop();
            stack.push(i);
        }
        return arr;
    }
}