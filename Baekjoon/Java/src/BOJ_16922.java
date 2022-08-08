import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.Set;

public class BOJ_16922 {
    public static final int[] nums = {1, 5, 10, 50};
    public static Set<Integer> set = new HashSet<>();
    static int cnt = 0;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());

        permutation(N, 0, 0, 0);

        System.out.println(set.size());
    }

    public static void permutation(int N, int depth, int idx, int sum) {
        if (depth == N) {
            set.add(sum);
            return;
        }

        for (int i = idx; i < 4; i++) {
            permutation(N, depth + 1, i, sum + nums[i]);
        }
    }
}
