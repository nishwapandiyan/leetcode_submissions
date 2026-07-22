class Solution {
    List<String> res = new ArrayList<>();
    public List<String> restoreIpAddresses(String s) {
        backtrack(s, 0, "", 0);
        return res;
    }

    void backtrack(String s, int idx, String curr, int dots) {
        if (dots == 4 && idx == s.length()) {
            res.add(curr.substring(0, curr.length() - 1));
            return;
        }
        if (dots > 4) return;

        for (int i = 1; i <= 3 && idx + i <= s.length(); i++) {
            String part = s.substring(idx, idx + i);
            if ((part.startsWith("0") && part.length() > 1) || Integer.parseInt(part) > 255) continue;
            backtrack(s, idx + i, curr + part + ".", dots + 1);
        }
    }
}
