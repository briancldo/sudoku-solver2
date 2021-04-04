from utils import flatten

default_candidates = [1, 2, 3, 4, 5, 6, 7, 8, 9]

class Square:
    def __init__(self, number: int, row, column):
        self.number = number
        self.candidates = list(default_candidates)
        self.row = row
        self.column = column
        
    def remove_candidates(self, candidates: list = []):
        for candidate in candidates:
            if candidate in self.candidates:
                self.candidates.remove(candidate)
        
    def __str__(self):
        return str(self.number)

horizontal_divider = '-------+-------+-------'
vertical_divider = '|'

class Grid:
    def __init__(self, grid):
        self.solved = False
        self.num_empty = 0
        self.grid = grid
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                square = self.grid[row][col]
                if int(square) == 0:
                    self.num_empty += 1
                self.grid[row][col] = Square(square, row, col)
    
    @staticmethod
    def convert_squares_to_numbers(squares):
        return [square.number for square in squares]
    
    def get_row(self, row_index):
        return self.convert_squares_to_numbers(self.grid[row_index])
    
    def get_column(self, column_index):
        column = []
        for row in range(len(self.grid)):
            column.append(self.grid[row][column_index])
        return self.convert_squares_to_numbers(column)
            
    def get_block(self, row_index, column_index):
        top_left_corner_row = row_index - row_index % 3
        top_left_corner_col = column_index - column_index % 3
        bottom_right_corner_row = top_left_corner_row + 2
        bottom_right_corner_col = top_left_corner_col + 2
        
        relevant_rows = self.grid[top_left_corner_row:bottom_right_corner_row + 1]
        block = [row[top_left_corner_col:bottom_right_corner_col + 1] for row in relevant_rows]
        return self.convert_squares_to_numbers(flatten(block))
    
    def get_context(self, row_index, column_index):
        row = self.get_row(row_index)
        column = self.get_column(column_index)
        block = self.get_block(row_index, column_index)
        return (row, column, block)
    
    def evaluate_square(self, square: Square, show_progress):
        if square.number == 0:
            context = self.get_context(square.row, square.column)
            context = list(set(flatten(context)))
            square.remove_candidates(context)
            if len(square.candidates) == 1:
                square.number = square.candidates[0]
                self.num_empty -= 1
                if show_progress:
                    print('---------------------------')
                    self.show_grid()
                    print('---------------------------')
            elif len(square.candidates) < 1:
                raise Exception(f'Row {square.row}, Column {square.column}, 0 candidates.')
    
    def solve(self, show_progress = False):
        while self.num_empty > 0:
            for row in range(len(self.grid)):
                for col in range(len(self.grid)):
                    self.evaluate_square(self.grid[row][col], show_progress)
        self.solved = True
    
    def is_valid_row(self, row_index):
        row = self.get_row(row_index)
        row.sort()
        return row == default_candidates
    
    def is_valid_column(self, column_index):
        column = self.get_column(column_index)
        column.sort()
        return column == default_candidates
    
    def is_valid_block(self, block_index):
        block = self.get_block(block_index - block_index % 3, (block_index % 3) * 3)
        block.sort()
        return block == default_candidates
    
    def get_validity_report(self):
        if self.solved == False:
            raise Exception('Puzzle not solved yet. Call <Grid>.solve() first.')
        
        invalid_parts = []
        valid = True
        for i in range(9):
            valid_row = self.is_valid_row(i)
            valid_column = self.is_valid_column(i)
            valid_block = self.is_valid_block(i)
            
            if not valid_row:
                invalid_parts.append(f'Row {i + 1}')
            if not valid_column:
                invalid_parts.append(f'Column {i + 1}')
            if not valid_block:
                invalid_parts.append((f'Block {i + 1}'))
            
            valid = valid and \
                    valid_row and \
                    valid_column and \
                    valid_block
        return {
            'valid': valid,
            'invalid_parts': invalid_parts
        }
        
    
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
