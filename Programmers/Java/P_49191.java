public class P_49191 {
    public static void main(String[] args) {
        System.out.println(solution(5, new int[][]{{4, 3}, {4, 2}, {3, 2}, {1, 2}, {2, 5}}));
    }

    public static int solution(int n, int[][] results) {
        int answer = 0;
        boolean[][] resultArr = new boolean[n + 1][n + 1];

        for (int[] result : results) {
            resultArr[result[0]][result[1]] = true;
        }

        for (int i = 0; i <= n; i++) {
            for (int j = 0; j <= n; j++) {
                for (int k = 0; k <= n; k++) {
                    if (resultArr[j][i] && resultArr[i][k]) {
                        resultArr[j][k] = true;
                    }
                }
            }
        }

        for (int i = 1; i <= n; i++) {
            int cnt = 0;

            for (int j = 1; j <= n; j++) {
                if (resultArr[i][j] || resultArr[j][i]) {
                    cnt++;
                }
            }

            if (cnt == n - 1) {
                answer++;
            }
        }

        return answer;
    }
}
