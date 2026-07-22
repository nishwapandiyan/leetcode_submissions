class Solution {
    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> Pascal = new ArrayList();
        for(int i=0;i<numRows;i++){
            List<Integer> row = new ArrayList();
            for(int j=0;j<=i;j++){
                if(j==0 || j==i){
                    row.add(1);
                }
                else{
                    List<Integer>Previous = Pascal.get(i-1);
                    row.add(Previous.get(j)+Previous.get(j-1));
                }
            }
            Pascal.add(row);
        }
        return Pascal;
    }
}