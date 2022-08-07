import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class BOJ_14916 {
    public static final int INF = 999_999;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());

        int[] dp = new int[N + 1];
        dp[1] = dp[3] = INF;

        for (int i = 2; i <= N; i++) {
            dp[i] = Math.min(dp[i - 2] + 1, dp[i]);
            if (i >= 5) {
                dp[i] = Math.min(dp[i - 5] + 1, dp[i]);
            }
        }

        System.out.println(dp[N] >= INF ? -1 : dp[N]);
    }
}
