import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class BOJ_15686 {
    private static int M;
    private static int answer = Integer.MAX_VALUE;
    private static List<Pos> houses, chickens;
    private static Pos[] comb;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        houses = new ArrayList<>();
        chickens = new ArrayList<>();
        comb = new Pos[M];

        for (int r = 0; r < N; r++) {
            st = new StringTokenizer(br.readLine());
            for (int c = 0; c < N; c++) {
                int value = Integer.parseInt(st.nextToken());

                if (value == 1) {
                    houses.add(new Pos(r, c));
                } else if (value == 2) {
                    chickens.add(new Pos(r, c));
                }
            }
        }

        getMinCheckinStreet(0, 0);

        System.out.println(answer);
    }

    private static void getMinCheckinStreet(int start, int depth) {
        if (depth == M) {
            int sum = 0;
            for (Pos house : houses) {
                int min = Integer.MAX_VALUE;
                for (Pos chicken : comb) {
                    min = Math.min(min, getDistance(house, chicken));
                }
                sum += min;
            }

            answer = Math.min(answer, sum);

            return;
        }

        for (int idx = start; idx < chickens.size(); idx++) {
            comb[depth] = chickens.get(idx);
            getMinCheckinStreet(idx + 1, depth + 1);
        }
    }

    private static int getDistance(Pos house, Pos chicken) {
        return Math.abs(house.getR() - chicken.getR())
                + Math.abs(house.getC() - chicken.getC());
    }

    private static class Pos {
        private final int r, c;

        public Pos(int r, int c) {
            this.r = r;
            this.c = c;
        }

        public int getR() {
            return r;
        }

        public int getC() {
            return c;
        }
    }

}
