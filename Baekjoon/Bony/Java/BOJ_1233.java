import java.io.*;
import java.util.*;

public class Hello {
    public static void main(String[] args) {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] nums = br.readLine().split(" ");

        int min = 100;
        int index = -1;
        int s1 = Integer.parseInt(nums[0]);
        int s2 = Integer.parseInt(nums[1]);
        int s3 = Integer.parseInt(nums[2]);
        int[] result = new int[s1 + s2 + s3 + 13];

        Arrays.fill(result, 100);

        for (int i = 1; i <= s1; i++) {
            for (int j = 1; j <= s2; j++) {
                for(int k = 1; k <= s3; k++){
                    result[i + j + k]--;
                }
            }
        }
        for(int n = 0; n < result.length; n++){
            if(min > result[n]){
                min = result[n];
                index = n;
            }
        }

        System.out.println(index);
    }
}
