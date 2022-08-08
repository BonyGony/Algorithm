import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

public class BOJ_5567 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        int m = Integer.parseInt(br.readLine());

        List<List<Integer>> list = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            list.add(new ArrayList<>());
        }

        for (int i = 0; i < m; i++) {
            String[] inputs = br.readLine().split(" ");
            int a = Integer.parseInt(inputs[0]) - 1;
            int b = Integer.parseInt(inputs[1]) - 1;

            list.get(a).add(b);
            list.get(b).add(a);
        }

        int answer = 0;

        boolean[] visit = new boolean[n];
        Queue<int[]> queue = new LinkedList<>();

        visit[0] = true;
        queue.add(new int[]{0, 0});

        while (!queue.isEmpty() && queue.peek()[1] < 2) {
            int[] cur = queue.poll();

            for (int f : list.get(cur[0])) {
                if (!visit[f]) {
                    queue.add(new int[]{f, cur[1] + 1});
                    visit[f] = true;
                    answer++;
                }
            }
        }

        System.out.println(answer);
    }
}
