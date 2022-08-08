import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ_16974 {
    private static long[] hamburgerSize, pattyCnt;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        long X = Long.parseLong(st.nextToken());

        hamburgerSize = new long[N + 1];
        pattyCnt = new long[N + 1];

        hamburgerSize[0] = pattyCnt[0] = 1;

        for (int i = 1; i <= N; i++) {
            hamburgerSize[i] = 1 + hamburgerSize[i - 1] + 1 + hamburgerSize[i - 1] + 1;
            pattyCnt[i] = pattyCnt[i - 1] + 1 + pattyCnt[i - 1];
        }

        System.out.println(getEatenPattyCnt(N, X));
    }

    public static long getEatenPattyCnt(int n, long x) {
        if (n == 0) {
            return x == 0 ? 0 : 1;
        }

        if (x == 1) {
            return 0;
        } else if (x <= 1 + hamburgerSize[n - 1]) {
            return getEatenPattyCnt(n - 1, x - 1);
        } else if (x == 1 + hamburgerSize[n - 1] + 1) {
            return pattyCnt[n - 1] + 1;
        } else if (x <= 1 + hamburgerSize[n - 1] + 1 + hamburgerSize[n - 1]) {
            return pattyCnt[n - 1] + 1 + getEatenPattyCnt(n - 1, x - (1 + hamburgerSize[n - 1] + 1));
        } else {
            return pattyCnt[n - 1] + 1 + pattyCnt[n - 1];
        }
    }
}
