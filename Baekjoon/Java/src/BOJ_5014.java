import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ_5014 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int F = Integer.parseInt(st.nextToken()); // 건물의 총 층 수
        int S = Integer.parseInt(st.nextToken()); // 현재 강호의 층
        int G = Integer.parseInt(st.nextToken()); // 이동 하려는 층
        int U = Integer.parseInt(st.nextToken()); // 위로 U층 만큼 이동
        int D = Integer.parseInt(st.nextToken()); // 아래로 D층 만큼 이동

        boolean[] visit = new boolean[F + 1];

        int answer = 0;

        while (S != G) {
            if (answer > 0 && visit[S]) {
                System.out.println("use the stairs");
                return;
            }

            visit[S] = true;
            if ((S < G || S - D <= 0) && S + U <= F) {
                S += U;
                answer++;
            } else if ((S > G || S + U > F) && S - D > 0) {
                S -= D;
                answer++;
            }
        }

        System.out.println(answer);
    }
}
