class Solution {
    public int romanToInt(String s) {
        int[] values = new int[128];
        values['I'] = 1;
        values['V'] = 5;
        values['X'] = 10;
        values['L'] = 50;
        values['C'] = 100;
        values['D'] = 500;
        values['M'] = 1000;
        int total = 0;

        for(int i=0;i<s.length();i++){
            int value = values[s.charAt(i)];
            if(i+1 < s.length() && value < values[s.charAt(i+1)]){
            total-=value;
            }
            else{
                total+=value;
            }
        }
        return total;
    }
}