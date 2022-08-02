import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class BOJ_13414 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int K = Integer.parseInt(st.nextToken());
        int L = Integer.parseInt(st.nextToken());

        Set<String> set = new LinkedHashSet<>();
        for (int i = 0; i < L; i++) {
            String stdId = br.readLine();

            set.remove(stdId);
            set.add(stdId);
        }

        StringBuilder sb = new StringBuilder();
        Iterator<String> iterator = set.iterator();
        for (int i = 0; i < K && iterator.hasNext(); i++) {
            sb.append(iterator.next()).append("\n");
        }

        System.out.println(sb);
    }
}