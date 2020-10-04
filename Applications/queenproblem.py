class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        prev_queens = []
        board = ["." * n] * n
        self.dfs(board, res, [], prev_queens, 0)
        
        return res
    
    def dfs(self, board, res, subset, prev_queens, row):
        if len(subset) == len(board):
            res.append(subset)
        else:
            for col in range(len(board)):
                board[row] = board[row][:col]+"Q"+board[row][col+1:]  # Place Queen

                if(self.isValid(board, row, col, prev_queens)):
                    prev_queens.append((row,col))  # Valid Queen, keep track of its position
                    self.dfs(board, res, subset+[board[row]], prev_queens, row+1)
                    prev_queens.pop()  # Remove its position and get ready for next placement (backtracking)
                board[row] = "." * len(board)   # Restore the row and get ready for next placemen  (backtracking)
                    
    
    
    def isValid(self, board, row, col, prev_queens):
        queen = 1
        for i in range(0, row):
            if queen > 1:
                valid = False
            if board[i][col] == "Q":
                queen += 1
        if queen > 1:
            return False
        
        for queen_pos in prev_queens:
            if abs(queen_pos[0]-row) == abs(queen_pos[1]-col):
                return False
        
        return True
