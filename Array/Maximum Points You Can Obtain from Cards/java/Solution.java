class Solution {
    public int maxScore(int[] cardPoints, int k) {
        int n = cardPoints.length;

        int currSum = 0;

        for (int i = 0; i < k; i++) {
            currSum += cardPoints[i];
        }

        int maxSum = currSum;

        for (int i = 1; i <= k; i++) {
            currSum = currSum - cardPoints[k - i] + cardPoints[n - i];
            maxSum = Math.max(maxSum, currSum);
        }

        return maxSum;
    }
}