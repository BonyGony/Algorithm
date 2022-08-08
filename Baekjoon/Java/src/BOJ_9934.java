import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class BOJ_9934 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int K = Integer.parseInt(br.readLine()) - 1;
        int[] inputs = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();

        List<List<int[]>> list = new ArrayList<>();

        list.add(new ArrayList<>());
        int rootNodIdx = inputs.length / 2;
        list.get(0).add(new int[]{inputs[rootNodIdx], rootNodIdx});

        for (int k = 0; k < K; k++) {
            int level = K - k - 1;
            list.add(new ArrayList<>());

            for (int[] parent : list.get(k)) {
                int move = (int) Math.pow(2, level);
                int leftIdx = parent[1] - move;
                int rightIdx = parent[1] + move;

                list.get(k + 1).add(new int[]{inputs[leftIdx], leftIdx});
                list.get(k + 1).add(new int[]{inputs[rightIdx], rightIdx});
            }
        }

        StringBuilder answer = new StringBuilder();
        for (List<int[]> nodes : list) {
            for (int[] node : nodes) {
                answer.append(node[0]).append(" ");
            }
            answer.append("\n");
        }

        System.out.println(answer);
    }
}
