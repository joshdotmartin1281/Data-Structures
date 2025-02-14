class NQueens:
    def __init__(self):
        self.solutions = 0 

    def is_valid(self, board, row, col, n):
        for i in range(row):
            if board[i] == col or \
               abs(board[i] - col) == abs(i - row):
                return False
        return True

    def recursive(self, board, row, n):
        if row == n:
            self.solutions += 1 
            return
        
        for col in range(n):
            if self.is_valid(board, row, col, n):
                board[row] = col 
                self.recursive(board, row + 1, n)
                board[row] = -1

    def solve(self, n: int):
        board = [-1] * n 
        self.solutions = 0
        self.recursive(board, 0, n)
        return self.solutions
    
def main():
    n = int(input("Enter the value of n (number of queens): ").strip())
    nqueens = NQueens()
    solutions = nqueens.solve(n)
    print(f"Number of valid solutions for {n}-Queens: {solutions}")

if __name__ == "__main__":
    main()