import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.StringTokenizer;

public class BOJ_1461 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        List<Integer> left = new ArrayList<>(List.of(0));
        List<Integer> right = new ArrayList<>(List.of(0));

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            int bookIdx = Integer.parseInt(st.nextToken());

            if (Integer.compare(bookIdx, 0) == -1) {
                left.add(bookIdx);
            } else {
                right.add(bookIdx);
            }
        }

        Collections.sort(left);
        right.sort(Collections.reverseOrder());

        System.out.println(getMinimumMovement(left, right, M));
    }

    private static int getMinimumMovement(List<Integer> left, List<Integer> right, int M) {
        return Integer.compare(Math.abs(left.get(0)), right.get(0)) == -1 ?
                addSmallerSide(left, M) + addLagerSide(right, M)
                : addSmallerSide(right, M) + addLagerSide(left, M);
    }

    private static int addLagerSide(List<Integer> list, int M) {
        int result = 0;

        result += Math.abs(list.get(0));
        for (int i = M; i < list.size(); i += M) {
            result += Math.abs(list.get(i) * 2);
        }

        return result;
    }

    private static int addSmallerSide(List<Integer> list, int M) {
        int result = 0;

        for (int i = 0; i < list.size(); i += M) {
            result += Math.abs(list.get(i) * 2);
        }

        return result;
    }
}
