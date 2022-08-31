import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class BOJ_17609 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder answer = new StringBuilder();

        int T = Integer.parseInt(br.readLine());

        while (T-- > 0) {
            String str = br.readLine();
            TwoPointer twoPointer = new TwoPointer(0, str.length() - 1);

            if (isPalindrome(str, twoPointer)) {
                answer.append(0);
            } else if (isPseudoPalindrome(str, twoPointer)) {
                answer.append(1);
            } else {
                answer.append(2);
            }

            answer.append("\n");
        }

        System.out.println(answer);
    }

    private static boolean isPseudoPalindrome(String str, TwoPointer twoPointer) {
        return isPalindrome(str, new TwoPointer(twoPointer.getLeft() + 1, twoPointer.getRight()))
                || isPalindrome(str, new TwoPointer(twoPointer.getLeft(), twoPointer.getRight() - 1));
    }

    private static boolean isPalindrome(String str, TwoPointer twoPointer) {
        while (twoPointer.getLeft() <= twoPointer.getRight()) {
            if (str.charAt(twoPointer.getLeft()) != str.charAt(twoPointer.getRight())) {
                return false;
            }

            twoPointer.movePointer();
        }

        return true;
    }

    private static class TwoPointer {
        int left, right;

        public TwoPointer(int left, int right) {
            this.left = left;
            this.right = right;
        }

        public int getLeft() {
            return left;
        }

        public int getRight() {
            return right;
        }

        public void movePointer() {
            this.left++;
            this.right--;
        }
    }
}
