import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class BOJ_11497 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder answer = new StringBuilder();

        int T = Integer.parseInt(br.readLine());
        while (T-- > 0) {
            int N = Integer.parseInt(br.readLine());
            int[] logHeights = Arrays.stream(br.readLine().split(" "))
                    .mapToInt(Integer::parseInt).toArray();

            Arrays.sort(logHeights);

            int maxDiff = 0, left = 0, right = N - 1;
            int[] sortedLogs = new int[N];

            for (int i = 0; i < N; i++) {
                if (i % 2 == 0) {
                    sortedLogs[left++] = logHeights[i];
                } else {
                    sortedLogs[right--] = logHeights[i];
                }
            }

            for (int i = 0; i < N - 1; i++) {
                maxDiff = Math.max(maxDiff, Math.abs(sortedLogs[i] -sortedLogs[i + 1]));
            }

            answer.append(maxDiff).append("\n");
        }

        System.out.println(answer);
    }
}
