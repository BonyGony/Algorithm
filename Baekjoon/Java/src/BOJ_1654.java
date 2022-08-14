import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class BOJ_1654 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int K = Integer.parseInt(st.nextToken());
        int N = Integer.parseInt(st.nextToken());

        int[] lanLens = new int[K];
        int maxLan = 0;

        for (int i = 0; i < K; i++) {
            lanLens[i] = Integer.parseInt(br.readLine());
            maxLan = Math.max(maxLan, lanLens[i]);
        }

        long low = 1, high = maxLan;
        while (low <= high) {
            long mid = (low + high) / 2, sum = 0;

            sum = Arrays.stream(lanLens)
                    .mapToLong(lanLen-> lanLen / mid).sum();

            if (sum >= N) {
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }

        System.out.println(high);
    }
}
