import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class BOJ_5972 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        List<List<Road>> roads = initializeList(N);

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int A_i = Integer.parseInt(st.nextToken());
            int B_i = Integer.parseInt(st.nextToken());
            int C_i = Integer.parseInt(st.nextToken());

            roads.get(A_i).add(new Road(B_i, C_i));
            roads.get(B_i).add(new Road(A_i, C_i));
        }

        System.out.println(getMinStover(N, roads));
    }

    private static int getMinStover(int N, List<List<Road>> roads) {
        PriorityQueue<Road> pq = new PriorityQueue<>();
        pq.add(new Road(1, 0));

        int[] dist = new int[N + 1];
        Arrays.fill(dist, Integer.MAX_VALUE);
        dist[1] = 0;

        boolean[] visit = new boolean[N + 1];

        while (!pq.isEmpty()) {
            Road cur = pq.poll();

            if (visit[cur.dest]) {
                continue;
            }
            visit[cur.dest] = true;

            for (Road next : roads.get(cur.dest)) {
                if (dist[next.dest] > dist[cur.dest] + next.dist) {
                    dist[next.dest] = dist[cur.dest] + next.dist;

                    pq.offer(new Road(next.dest, dist[next.dest]));
                }
            }
        }

        return dist[N];
    }

    public static List<List<Road>> initializeList(int N) {
        List<List<Road>> temp = new ArrayList<>();

        for (int i = 0; i <= N; i++) {
            temp.add(new ArrayList<>());
        }

        return temp;
    }

    public static class Road implements Comparable<Road> {
        int dest, dist;

        public Road(int dest, int dist) {
            this.dest = dest;
            this.dist = dist;
        }

        @Override
        public int compareTo(Road o) {
            return this.dist - o.dist;
        }
    }
}
