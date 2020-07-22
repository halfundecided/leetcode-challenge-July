"""
July 21, 2020
Word Search
"""
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(0, len(board)):
            for j in range(0, len(board[i])):
                if board[i][j] == word[0]:
                    if self.dfs(board, i, j, word, 0) == True:
                        return True
        
        return False
    
    def dfs(self, board, i, j, word, index):
        
        if index == len(word):
            return True
        
        if i < 0 or i > len(board)-1 or j < 0 or j > len(board[i])-1 or board[i][j] != word[index]:
            return False
        
        temp = board[i][j]
        board[i][j] = '.'
        index += 1
        result = self.dfs(board, i-1, j, word, index) or self.dfs(board, i+1, j, word, index) or self.dfs(board, i, j+1, word, index) or self.dfs(board, i, j-1, word, index)        
        board[i][j] = temp
        return result
            

