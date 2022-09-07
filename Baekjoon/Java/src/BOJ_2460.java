import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class BOJ_2460 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int answer = 0, cur = 0;
        for (int i = 0; i < 10; i++) {
            String[] inputs = br.readLine().split(" ");
            int out = Integer.parseInt(inputs[0]);
            int in = Integer.parseInt(inputs[1]);

            cur = cur - out + in;
            answer = Math.max(answer, cur);
        }

        System.out.println(answer);
    }
}
