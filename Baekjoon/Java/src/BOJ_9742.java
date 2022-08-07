import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.StringTokenizer;

public class BOJ_9742 {
    public static final int[] factorial = {1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st;
        String input = "";
        StringBuilder answer = new StringBuilder();

        while ((input = br.readLine()) != null) {
            st = new StringTokenizer(input);
            String str = st.nextToken();
            int n = Integer.parseInt(st.nextToken());

            answer.append(str).append(" ").append(n).append(" = ");

            if (n > factorial[str.length()]) {
                answer.append("No permutation");
            } else {
                List<String> origin = new ArrayList<>(Arrays.asList(str.split("")));
                List<String> result = new ArrayList<>();

                while (origin.size() > 0) {
                    int idx = 0;

                    if (n >= factorial[origin.size() - 1]) {
                        idx = (int) Math.ceil((double) n / factorial[origin.size() - 1]) - 1;
                        n = n - (n - 1) / factorial[origin.size() - 1] * factorial[origin.size() - 1];
                    }

                    result.add(origin.remove(idx));
                }

                StringBuilder sb = new StringBuilder();
                for (String s : result) {
                    sb.append(s);
                }
                answer.append(sb);
            }
            answer.append("\n");
        }

        System.out.println(answer);
    }
}
