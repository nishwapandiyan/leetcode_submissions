class Solution {
    public int maxFreqSum(String s) {
        int freq[] = new int[26];
        int vmax = 0, cmax = 0;
        for(char c: s.toCharArray()){
            freq[c-'a']++;
            if(c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u'){
                if(freq[c-'a'] > vmax) vmax = freq[c - 'a'];
            }
            else{
                if(freq[c-'a'] > cmax) cmax = freq[c-'a'];
            }
        }
        return vmax + cmax;
    }
}