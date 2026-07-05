class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        // make map where key is the common characters 
        // and values is list of strings with the same number of characters

        Map<String, List<String>> ans = new HashMap<>();
        
        for (String s : strs) {
            // create char freq array for each string
            int[] count = new int[26];
            for (char c : s.toCharArray()) {
                count[c - 'a']++;
            }

            // turn array into string
            String key = Arrays.toString(count);
            // add new list if new group 
            if (!ans.containsKey(key)) {
                ans.put(key, new LinkedList<>());
            }
            // add string at the key
            ans.get(key).add(s);
        }

        // return the list of the values of the map
        return new LinkedList<>(ans.values());
    }
}
