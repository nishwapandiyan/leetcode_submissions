import java.util.*;

public class Solution {
    public String longestWord(String[] words) {
        Arrays.sort(words); // Sort lexicographically
        Set<String> built = new HashSet<>();
        built.add(""); // empty string is the starting point
        String result = "";
        
        for (String word : words) {
            if (built.contains(word.substring(0, word.length() - 1))) {
                built.add(word);
                if (word.length() > result.length()) {
                    result = word;
                }
            }
        }
        
        return result;
    }
}
