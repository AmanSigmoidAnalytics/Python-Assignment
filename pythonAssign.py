class Solution:
    def dfs(self, i: int, j: int, board: list[list[str]], n: int, m: int) -> None:
        # if index go out of bounds or we reach X or Z( Z indicates we have already visited this index)
        if (i < 0 or i >= n or j < 0 or j >= m or board[i][j] == 'X' or board[i][j] == 'Z'):
            return
        board[i][j] = 'Z' # mark current 'O' as 'Z'
        #recursive dfs in all 4 directions
        self.dfs(i + 1, j, board, n, m)
        self.dfs(i - 1, j, board, n, m)
        self.dfs(i, j + 1, board, n, m)
        self.dfs(i, j - 1, board, n, m)

    def solve(self, board: list[list[str]]) -> None:
        
        # solution : Instead of transforming all 'O's which are 4 directionally surrounded
        #            find recursively all 'O's that can be reached by edges (boundary) of matrix
        #            Transform all such 'O's to any character let say 'Z'
        #            Now all 'O's that are left are surrounded by 'X' in all 4 direction
        #            revert back all 'Z' to 'O' as they will not change ( since they are reachable from boundaries) 
        
        n, m = len(board), len(board[0]) # finding shape of matrix 

        # iterate all the boundary of matrix ie FIRST ROW,LAST ROW,FIRST COLUMN,LAST COLUMN
        # while iterating if we reach a index where board[i][j] =='O' 
        # apply a dfs 
        

        
        for i in range(0, n):
            if board[i][0] == 'O':
                self.dfs(i, 0, board, n, m)
            if board[i][m - 1] == 'O':
                self.dfs(i, m - 1, board, n, m)

        for i in range(0, m):
            if board[0][i] == 'O':
                self.dfs(0, i, board, n, m)
            if board[n - 1][i] == 'O':
                self.dfs(n - 1, i, board, n, m)
        
        print("\n Intermediate Board")
        for row in board:
            print(row)

        for i in range(0, n):
            for j in range(0, m):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'Z':
                    board[i][j] = 'O'

# driver code 
if __name__ == "__main__":
    sol = Solution()
    
    # input
    board=[]
    r=int(input("Enter number of rows"))
    c=int(input("Enter number of columns"))

    for i in range(r):
        row=[]
        for j in range(c):
            row.append(input())
        board.append(row)    

    print("Original Board:")
    for row in board:
        print(row)

    sol.solve(board)

    print("\nModified Board:")
    for row in board:
        print(row)                    