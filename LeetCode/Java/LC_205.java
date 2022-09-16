import java.util.HashMap;
import java.util.Map;

public class LC_205 {
    public static void main(String[] args) {
        isIsomorphic("egg", "add");
        isIsomorphic("foo", "bar");
        isIsomorphic("paper", "title");
    }

    public static boolean isIsomorphic(String s, String t) {
        Map<Character, Character> sMap = new HashMap<>();
        Map<Character, Character> tMap = new HashMap<>();

        for (int i = 0; i < s.length(); i++) {
            if ((sMap.containsKey(s.charAt(i)) && sMap.get(s.charAt(i)) != t.charAt(i))
                    || (tMap.containsKey(t.charAt(i)) && tMap.get(t.charAt(i)) != s.charAt(i))) {
                return false;
            }

            sMap.put(s.charAt(i), t.charAt(i));
            tMap.put(t.charAt(i), s.charAt(i));
        }

        return true;
    }
}
