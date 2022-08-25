import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class BOJ_2851 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int answer = 0;

        for (int i = 0; i < 10; i++) {
            int n = Integer.parseInt(br.readLine());

            if (Math.abs(100 - (answer + n)) <= Math.abs(100 - answer)) {
                answer += n;
            } else {
                break;
            }
        }

        System.out.println(answer);
    }
}
