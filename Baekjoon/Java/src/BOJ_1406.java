import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.List;
import java.util.ListIterator;

public class BOJ_1406 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        List<String> list = new LinkedList<>(List.of(br.readLine().split("")));

        int M = Integer.parseInt(br.readLine());
        ListIterator<String> iterator = list.listIterator(list.size());

        while (M-- > 0) {
            String[] inputs = br.readLine().split(" ");

            switch (inputs[0]) {
                case "L":
                    if (iterator.hasPrevious()) {
                        iterator.previous();
                    }
                    break;
                case "D":
                    if (iterator.hasNext()) {
                        iterator.next();
                    }
                    break;
                case "B":
                    if (iterator.hasPrevious()) {
                        iterator.previous();
                        iterator.remove();
                    }
                    break;
                default:
                    iterator.add(inputs[1]);
                    break;
            }
        }

        StringBuilder answer = new StringBuilder();
        for (String s : list) {
            answer.append(s);
        }
        System.out.println(answer);
    }
}
