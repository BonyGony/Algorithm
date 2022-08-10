import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class BOJ_4963 {
    public static int[] dx = {1, 0, -1, 0, 1, 1, -1, -1};
    public static int[] dy = {0, 1, 0, -1, 1, -1, 1, -1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder answer = new StringBuilder();

        while (true) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int w = Integer.parseInt(st.nextToken());
            int h = Integer.parseInt(st.nextToken());

            if (w == 0 && h == 0) break;

            int[][] map = new int[h][w];
            for (int i = 0; i < h; i++) {
                st = new StringTokenizer(br.readLine());

                for (int j = 0; j < w; j++) {
                    map[i][j] = Integer.parseInt(st.nextToken());
                }
            }

            answer.append(findLand(map)).append("\n");
        }

        System.out.println(answer);
    }

    private static int findLand(int[][] map) {
        int cnt = 0, h = map.length, w = map[0].length;
        boolean[][] visit = new boolean[h][w];

        for (int i = 0; i < h; i++) {
            for (int j = 0; j < w; j++) {
                if (map[i][j] != 0 && !visit[i][j]) {
                    checkLand(i, j, map, visit);
                    cnt++;
                }
            }
        }

        return cnt;
    }

    private static void checkLand(int i, int j, int[][] map, boolean[][] visit) {
        Queue<int[]> queue = new LinkedList<>();
        queue.add(new int[]{i, j});

        int h = map.length, w = map[0].length;
        visit[i][j] = true;

        while (!queue.isEmpty()) {
            int[] cur = queue.poll();

            for (int d = 0; d < 8; d++) {
                int nx = cur[0] + dx[d];
                int ny = cur[1] + dy[d];

                if (nx < 0 || ny < 0 || nx >= h || ny >= w) continue;
                if (visit[nx][ny] || map[nx][ny] == 0) continue;

                queue.add(new int[]{nx, ny});
                visit[nx][ny] = true;
            }
        }
    }
}
