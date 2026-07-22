import java.util.*;

class Solution {
    public List<List<Integer>> getSkyline(int[][] buildings) {
        List<int[]> points = new ArrayList<>();

      
        for (int[] b : buildings) {
            points.add(new int[]{b[0], -b[2]});
            points.add(new int[]{b[1], b[2]}); 
        }

       
        Collections.sort(points, (a, b) -> {
            if (a[0] != b[0]) return a[0] - b[0];
            return a[1] - b[1];
        });


        PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());
        pq.add(0);
        int prevMax = 0;

        List<List<Integer>> result = new ArrayList<>();

        for (int[] p : points) {
            int x = p[0];
            int h = p[1];

            if (h < 0) { 
                pq.add(-h);
            } else { 
                pq.remove(h);
            }

            int currMax = pq.peek();
            if (currMax != prevMax) {
                result.add(Arrays.asList(x, currMax));
                prevMax = currMax;
            }
        }

        return result;
    }
}
