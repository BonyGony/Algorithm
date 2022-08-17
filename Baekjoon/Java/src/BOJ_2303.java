import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class BOJ_2303 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());

        int answer = 1, max = 0;
        for (int n = 1; n <= N; n++) {
            int[] inputs = Arrays.stream(br.readLine().split(" "))
                    .mapToInt(Integer::parseInt).toArray();

            for (int i = 0; i < 3; i++) {
                for (int j = i + 1; j < 4; j++) {
                    for (int k = j + 1; k < 5; k++) {
                        System.out.println(inputs[i] + inputs[j] + inputs[k]);
                        int sum = (inputs[i] + inputs[j] + inputs[k]) % 10;

                        if (max <= sum) {
                            max = sum;
                            answer = n;
                        }
                    }
                }
            }
        }

        System.out.println(answer);
    }
}
