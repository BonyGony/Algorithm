import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class BOJ_14584 {
    private static final int AlpCnt = 26, aIdx = 97, zIdx = 123;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String originalStr = br.readLine();

        int N = Integer.parseInt(br.readLine());
        String[] words = new String[N];
        for (int i = 0; i < N; i++) {
            words[i] = br.readLine();
        }

        char[] chars = new char[AlpCnt];
        for (int i = aIdx; i < zIdx; i++) {
            chars[i - aIdx] = (char) i;
        }

        for (int i = 0; i < AlpCnt; i++) {
            String decode = decoding(chars, originalStr);

            if (containWord(decode, words)) {
                System.out.println(decode);
                return;
            }

            rotate(chars);
        }
    }

    private static boolean containWord(String str, String[] words) {
        for (String word : words) {
            if (str.contains(word)) {
                return true;
            }
        }

        return false;
    }

    private static String decoding(char[] chars, String str) {
        StringBuilder sb = new StringBuilder();

        for (char c : str.toCharArray()) {
            sb.append(chars[c - aIdx]);
        }

        return sb.toString();
    }

    private static void rotate(char[] chars) {
        for (int i = 0; i < AlpCnt; i++) {
            chars[i] += 1;

            if (chars[i] >= zIdx) {
                chars[i] = aIdx;
            }
        }
    }
}
