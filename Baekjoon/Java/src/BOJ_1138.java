import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class BOJ_1138 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());

        int[] result = new int[N];
        Arrays.fill(result, Integer.MAX_VALUE);

        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int height = 1; height <= N; height++) {
            int personCnt = Integer.parseInt(st.nextToken());

            int index = 0, cnt = 0;
            while (cnt < personCnt || result[index] != Integer.MAX_VALUE) {
                if (result[index] > height) {
                    cnt++;
                }

                index++;
            }

            result[index] = height;
        }

        StringBuilder sb = new StringBuilder();
        for (int n : result) {
            sb.append(n).append(" ");
        }
        System.out.println(sb);
    }
}
