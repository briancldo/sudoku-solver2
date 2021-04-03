class Square:
    def __init__(self, number: int = 0, candidates = []):
        self.number = number
        self.candidates = candidates
        
    def __str__(self):
        return str(self.number)

horizontal_divider = '-------+-------+-------'
vertical_divider = '|'

class Grid:
    def __init__(self, grid):
        self.grid = grid
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                self.grid[row][col] = Square(grid[row][col])
    
    # TODO: replace with GUI
    def show_grid(self):
        for row in range(len(self.grid)):
            if row > 0 and row % 3 == 0:
                print(horizontal_divider)
                
            for col in range(len(self.grid[row])):
                if col > 0 and col % 3 == 0:
                    print(f' {vertical_divider}', end='')
                print(f' {str(self.grid[row][col])}', end='')
                if col == len(self.grid[row]) - 1:
                    print(' ')
