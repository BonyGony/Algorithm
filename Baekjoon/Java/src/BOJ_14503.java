import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class BOJ_14503 {
    private static final int[] dx = {-1, 0, 1, 0};
    private static final int[] dy = {0, 1, 0, -1};

    private static int N, M;
    private static int[][] map;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        int r = Integer.parseInt(st.nextToken());
        int c = Integer.parseInt(st.nextToken());
        int d = Integer.parseInt(st.nextToken());

        map = new int[N][M];

        for (int i = 0; i < N; i++) {
            map[i] = Arrays.stream(br.readLine().split(" "))
                    .mapToInt(Integer::parseInt).toArray();
        }

        System.out.println(getRobotCleanSpace(r, c, d));
    }

    private static int getRobotCleanSpace(int initialR, int initialC, int d) {
        int cnt = 0;

        Queue<int[]> queue = new LinkedList<>();
        queue.add(new int[]{initialR, initialC});

        boolean[][] visit = new boolean[N][M];
        visit[initialR][initialC] = true;

        while (!queue.isEmpty()) {
            int[] cur = queue.poll();
            int r = cur[0], c = cur[1];

            if (isSpace(r, c)) {
                changeToCleaned(r, c);
                cnt++;
            }

            boolean canClean = false;
            for (int k = 0; k < 4; k++) {
                d = getLeft(d);

                int nx = r + dx[d];
                int ny = c + dy[d];

                if (isValid(visit, nx, ny) && map[nx][ny] == 0) {
                    queue.offer(new int[]{nx, ny});
                    visit[nx][ny] = true;

                    canClean = true;

                    break;
                }
            }

            if (!canClean) {
                int nd = getBack(d);

                int nx = r + dx[nd];
                int ny = c + dy[nd];

                if (isValid(nx, ny) && map[nx][ny] != 1) {
                    queue.offer(new int[]{nx, ny});
                    visit[nx][ny] = true;
                }
            }
        }

        return cnt;
    }

    private static boolean isSpace(int r, int c) {
        return map[r][c] == 0;
    }

    private static void changeToCleaned(int r, int c) {
        map[r][c] = -1;
    }

    private static int getBack(int d) {
        return (d + 2) % 4;
    }

    private static int getLeft(int d) {
        return (d + 3) % 4;
    }

    private static boolean isValid(int r, int c) {
        return 0 <= r && r < N && 0 <= c && c < M;
    }

    private static boolean isValid(boolean[][] visit, int r, int c) {
        return isValid(r, c) && !visit[r][c];
    }
}
