class Solution {
    public boolean isValidSudoku(char[][] board) {
        // check rows
        for (int i = 0; i < board.length; i++) {
            Set<Character> row = new HashSet<>();
            for (int j = 0; j < board.length; j++) {
                if (row.contains(board[i][j])) return false;
                if (board[i][j] != '.') row.add(board[i][j]);
            }
        }

        // check cols
        for (int i = 0; i < board.length; i++) {
            Set<Character> col = new HashSet<>();
            for (int j = 0; j < board.length; j++) {
                if (col.contains(board[j][i])) return false;
                if (board[j][i] != '.') col.add(board[j][i]);
            }
        }

        // check subboxes
        for (int i = 0; i < board.length; i += 3) {
            for (int j = 0; j < board.length; j += 3) {
                Set<Character> box = new HashSet<>();
                for (int k = 0; k < 3; k++) {
                    for (int l = 0; l < 3; l++) {
                        if (box.contains(board[i + k][j + l])) return false;
                        if (board[i + k][j + l] != '.') box.add(board[i + k][j + l]);
                    }
                }
            }
        }

        return true;

    }
}
