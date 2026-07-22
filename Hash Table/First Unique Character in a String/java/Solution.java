public class Solution {
    public int firstUniqChar(String s) {
        int[] count = new int[26];
        for (char c : s.toCharArray()) {
            count[c - 97]++;
        }
        for (int i = 0; i < s.length(); i++) {
            if (count[s.charAt(i) - 97] == 1) {
                return i;
            }
        }
        return -1;
    }
}
