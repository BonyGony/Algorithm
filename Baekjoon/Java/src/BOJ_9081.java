import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class BOJ_9081 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int T = Integer.parseInt(br.readLine());
        StringBuilder answer = new StringBuilder();

        while (T-- > 0) {
            char[] word = br.readLine().toCharArray();

            answer.append(getNextPermutation(word)).append("\n");
        }

        System.out.println(answer);
    }

    private static String getNextPermutation(char[] word) {
        int front = word.length - 1;
        while (front > 0 && word[front - 1] >= word[front]) {
            front--;
        }

        if (front == 0) {
            return String.valueOf(word);
        }

        int back = word.length - 1;
        while (word[front - 1] >= word[back]) {
            back--;
        }

        swap(word, front - 1, back);

        Arrays.sort(word, front, word.length);

        return String.valueOf(word);
    }

    private static void swap(char[] word, int i, int j) {
        char temp = word[i];
        word[i] = word[j];
        word[j] = temp;
    }
}
