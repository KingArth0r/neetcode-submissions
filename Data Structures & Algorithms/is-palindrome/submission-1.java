class Solution {
    public boolean isPalindrome(String s) {
        s = s.toLowerCase().trim();
        StringBuilder t = new StringBuilder();
        for (int i = 0; i < s.length(); i++) {
            if (('a' <= s.charAt(i) && 'z' >= s.charAt(i)) || ('0' <= s.charAt(i) && '9' >= s.charAt(i))) {
                t.append(s.charAt(i));
            }
        }
        for (int i = 0; i < t.length()/2; i++) {
            if (t.charAt(i) != t.charAt(t.length() - 1 - i)) return false;
        }
        return true;
    }
}
