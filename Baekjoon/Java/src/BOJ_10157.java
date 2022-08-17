import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ_10157 {
    private static final int[] dr = {-1, 0, 1, 0};
    private static final int[] dc = {0, 1, 0, -1};

    private static int C, R;
    private static boolean[][] visit;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        C = Integer.parseInt(st.nextToken());
        R = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(br.readLine());

        if (K > C * R) {
            System.out.println(0);
            return;
        }

        visit = new boolean[R + 1][C + 1];

        int r = R, c = 1, d = 0, cnt = 1;
        while (cnt < K) {
            visit[r][c] = true;

            int nr = r + dr[d];
            int nc = c + dc[d];

            if (!isValid(nr, nc)) {
                d = rotate(d);

                nr = r + dr[d];
                nc = c + dc[d];
            }

            r = nr;
            c = nc;
            cnt++;
        }

        System.out.println(c + " " + (R - r + 1));
    }

    private static int rotate(int d) {
        return (d + 1) % 4;
    }

    private static boolean isValid(int r, int c) {
        return 0 < r && r <= R && 0 < c && c <= C && !visit[r][c];
    }
}
