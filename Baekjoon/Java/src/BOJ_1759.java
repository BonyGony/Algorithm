import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Set;
import java.util.StringTokenizer;

public class BOJ_1759 {
    private static final Set<Character> consonants = Set.of('a', 'e', 'i', 'o', 'u');

    private static int L, C;
    private static char[] characters, combination;
    private static final StringBuilder answer = new StringBuilder();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        L = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());

        characters = br.readLine().replaceAll("\\s", "").toCharArray();
        combination = new char[L];

        Arrays.sort(characters);

        getCombination(0, 0);

        System.out.println(answer);
    }

    private static void getCombination(int depth, int strIdx) {
        if (depth == L) {
            if (isValid()) {
                answer.append(String.valueOf(combination)).append("\n");
            }

            return;
        }

        for (int i = strIdx; i < C; i++) {
            combination[depth] = characters[i];
            getCombination(depth + 1, i + 1);
        }
    }

    private static boolean isValid() {
        int consonantCnt = 0, collectionCnt = 0;

        for (char c : combination) {
            if (consonants.contains(c)) {
                consonantCnt++;
            } else {
                collectionCnt++;
            }
        }

        return consonantCnt >= 1 && collectionCnt >= 2;
    }
}
