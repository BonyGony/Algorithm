public class LC_392 {
    public static void main(String[] args) {
        isSubsequence("abc", "ahbgdc");
        isSubsequence("axc", "ahbgdc");
    }
    public static boolean isSubsequence(String s, String t) {
        if (s.length() == 0) {
            return true;
        }

        int idx = 0;

        for (char c : t.toCharArray()) {
            if (c == s.charAt(idx)) {
                idx++;

                if (idx == s.length()) {
                    return true;
                }
            }
        }

        return false;
    }
}
