public class Solution {
    public String frequencySort(String s) {
        
        int[] freq = new int[128];  
        for (char c : s.toCharArray()) {
            freq[c]++;
        }
        int maxFreq = 0;
        for (int f : freq) {
            if (f > maxFreq) maxFreq = f;
        }
        StringBuilder[] buckets = new StringBuilder[maxFreq + 1];
        for (int i = 0; i <= maxFreq; i++) {
            buckets[i] = new StringBuilder();
        }

        for (int i = 0; i < 128; i++) {
            if (freq[i] > 0) {
                buckets[freq[i]].append((char)i);
            }
        }
        StringBuilder result = new StringBuilder();
        for (int i = maxFreq; i > 0; i--) {
            if (buckets[i].length() > 0) {
                for (char c : buckets[i].toString().toCharArray()) {
                    result.append(String.valueOf(c).repeat(i));
                }
            }
        }

        return result.toString();
    }
}
