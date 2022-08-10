import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class BOJ_5212 {
    public static final int[] dx = {1, 0, -1, 0};
    public static final int[] dy = {0, 1, 0, -1};

    public static int R, C;
    public static char[][] map;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        R = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());

        map = new char[R][C];
        for (int i = 0; i < R; i++) {
            String str = br.readLine();

            for (int j = 0; j < C; j++) {
                map[i][j] = str.charAt(j);
            }
        }

        map = after50Years();

        System.out.println(getArea());
    }

    private static String getArea() {
        int minI = R, minJ = C, maxI = 0, maxJ = 0;

        for (int i = 0; i < R; i++) {
            for (int j = 0; j < C; j++) {
                if (map[i][j] == 'X') {
                    minI = Math.min(minI, i);
                    minJ = Math.min(minJ, j);
                    maxI = Math.max(maxI, i);
                    maxJ = Math.max(maxJ, j);
                }
            }
        }

        StringBuilder result = new StringBuilder();
        for (int i = minI; i <= maxI; i++) {
            for (int j = minJ; j <= maxJ; j++) {
                result.append(map[i][j]);
            }
            result.append("\n");
        }

        return result.toString();
    }

    private static char[][] after50Years() {
        char[][] temp = new char[R][C];

        for (int i = 0; i < R; i++) {
            for (int j = 0; j < C; j++) {
                temp[i][j] = map[i][j];

                if (map[i][j] == 'X' && count(i, j) >= 3) {
                    temp[i][j] = '.';
                }
            }
        }

        return temp;
    }

    private static int count(int i, int j) {
        int cnt = 0;

        for (int d = 0; d < 4; d++) {
            int nx = i + dx[d];
            int ny = j + dy[d];

            if (nx < 0 || ny < 0 || nx >= R || ny >= C || map[nx][ny] == '.') {
                cnt++;
            }
        }

        return cnt;
    }
}
