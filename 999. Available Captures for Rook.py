class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        idx = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'R':
                    idx = [i, j]
                    break
        x, y = idx[0], idx[1]
        count = 0
        for i in range(x-1, -1, -1):
            if board[i][y] == 'p':
                count += 1
                break
            elif board[i][y] == 'B':
                break
            
        for i in range(x+1, 8):
            if board[i][y] == 'p':
                count += 1
                break
            elif board[i][y] == 'B':
                break

        for i in range(y-1, -1, -1):
            if board[x][i] == 'p':
                count += 1
                break
            elif board[x][i] == 'B':
                break
        
        for i in range(y+1, 8):
            if board[x][i] == 'p':
                count += 1
                break
            elif board[x][i] == 'B':
                break
        return count