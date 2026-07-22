class Solution {
    public String convertDateToBinary(String date) {
        String[] dateParts = date.split("-");
        String yearBinary = Integer.toBinaryString(Integer.parseInt(dateParts[0]));
        String monthBinary = Integer.toBinaryString(Integer.parseInt(dateParts[1]));
        String dayBinary = Integer.toBinaryString(Integer.parseInt(dateParts[2]));
        return yearBinary + "-" + monthBinary + "-" + dayBinary;
    }
}
