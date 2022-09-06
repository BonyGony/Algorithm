import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class BOJ_7682 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder answer = new StringBuilder();

        while (true) {
            String ticTacToe = br.readLine();
            if (ticTacToe.equals("end")) break;

            answer.append(isValid(ticTacToe) ? "valid" : "invalid").append("\n");
        }

        System.out.println(answer);
    }

    private static boolean isValid(String ticTacToe) {
        int cntO = 0, cntX = 0, ansO = 0, ansX = 0;

        for (char ox : ticTacToe.toCharArray()) {
            if (ox == 'O') cntO++;
            else if (ox == 'X') cntX++;
        }

        if (cntX - cntO != 1 && cntX - cntO != 0) return false;

        for (int i = 0; i < 9; i += 3) {
            if (!isBlank(ticTacToe.charAt(i)) && checkRow(ticTacToe, i)) {
                if (ticTacToe.charAt(i) == 'O') ansO++;
                else ansX++;
            }
        }

        for (int j = 0; j < 3; j++) {
            if (!isBlank(ticTacToe.charAt(j)) && checkCol(ticTacToe, j)) {
                if (ticTacToe.charAt(j) == 'O') ansO++;
                else ansX++;
            }
        }

        if (ticTacToe.charAt(4) != '.' && checkCross(ticTacToe)) {
            if (ticTacToe.charAt(4) == 'O') ansO++;
            else ansX++;
        }

        if (ansX > 0) {
            if (ansO > 0) return false;
            return cntX - cntO == 1;
        }

        if (ansO > 0) {
            return cntX - cntO == 0;
        }

        return cntX + cntO == 9;
    }

    private static boolean checkCross(String ticTacToe) {
        return (ticTacToe.charAt(4) == ticTacToe.charAt(0) && ticTacToe.charAt(4) == ticTacToe.charAt(8))
                || (ticTacToe.charAt(4) == ticTacToe.charAt(2) && ticTacToe.charAt(4) == ticTacToe.charAt(6));
    }

    private static boolean checkCol(String ticTacToe, int j) {
        return ticTacToe.charAt(j) == ticTacToe.charAt(j + 3)
                && ticTacToe.charAt(j + 3) == ticTacToe.charAt(j + 6);
    }

    private static boolean checkRow(String ticTacToe, int i) {
        return ticTacToe.charAt(i) == ticTacToe.charAt(i + 1)
                && ticTacToe.charAt(i + 1) == ticTacToe.charAt(i + 2);
    }

    private static boolean isBlank(char block) {
        return block != 'O' && block != 'X';
    }
}
