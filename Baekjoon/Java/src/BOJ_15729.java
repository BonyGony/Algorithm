import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

public class BOJ_15729 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        List<Boolean> buttons = Arrays.stream(br.readLine().split(" "))
                .map(s -> s.equals("1")).collect(Collectors.toList());

        int answer = 0;
        for (int idx = 0; idx < N; idx++) {
            if (isOn(buttons.get(idx))) {
                changeButton(buttons, idx);
                answer++;
            }
        }

        System.out.println(answer);
    }

    private static void changeButton(List<Boolean> buttons, int idx) {
        buttons.set(idx, !buttons.get(idx));

        if (idx + 1 < buttons.size()) {
            buttons.set(idx + 1, !buttons.get(idx + 1));
        }

        if (idx + 2 < buttons.size()) {
            buttons.set(idx + 2, !buttons.get(idx + 2));
        }
    }

    private static boolean isOn(boolean button) {
        return button;
    }
}
