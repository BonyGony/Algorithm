public class LC_1480 {
    public static void main(String[] args) {
        runningSum(new int[]{1, 2, 3, 4});
        runningSum(new int[]{1, 1, 1, 1, 1});
        runningSum(new int[]{3, 1, 2, 10, 1});
    }
    public static int[] runningSum(int[] nums) {
        int[] sums = new int[nums.length];


        for (int idx = 0; idx < nums.length; idx++) {
            sums[idx] = sums[Math.max(0, idx - 1)] + nums[idx];
        }

        return sums;
    }
}
