import java.util.*;

class Solution {
    public String simplifyPath(String path) {
        String[] parts = path.split("/");
        Deque<String> stack = new ArrayDeque<>();

        for (String part : parts) {
            if (part.equals("") || part.equals(".")) {
                continue; 
            } else if (part.equals("..")) {
                if (!stack.isEmpty()) stack.pop();
            } else {
                stack.push(part);
            }
        }

        StringBuilder sb = new StringBuilder();
        while (!stack.isEmpty()) {
            sb.insert(0, "/" + stack.pop());
        }

        return sb.length() > 0 ? sb.toString() : "/";
    }
}
