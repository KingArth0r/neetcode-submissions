class Solution {
    public boolean isAnagram(String s, String t) {
        char[] word1 = s.toCharArray();
        char[] word2 = t.toCharArray();
        if (word1.length != word2.length) return false;
        int[] freq1 = new int[26];
        int[] freq2 = new int[26];

        for (int i = 0; i < word1.length; i++) {
            freq1[word1[i] - 'a']++;
            freq2[word2[i] - 'a']++;
        }

        for (int i = 0; i < 26; i++) {
            if (freq1[i] != freq2[i]) return false;
        }

        return true;
    }
}
