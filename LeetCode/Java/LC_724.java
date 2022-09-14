import java.util.Arrays;

public class LC_724 {
    public static void main(String[] args) {
        pivotIndex(new int[]{1, 7, 3, 6, 5, 6});
        pivotIndex(new int[]{1, 2, 3});
        pivotIndex(new int[]{2, 1, -1});
    }

    public static int pivotIndex(int[] nums) {
        int leftSum = 0, rightSum = Arrays.stream(nums).sum();

        for (int idx = 0; idx < nums.length; idx++) {
            rightSum -= nums[idx];

            if (leftSum == rightSum) {
                return idx;
            }

            leftSum += nums[idx];
        }

        return -1;
    }
}
