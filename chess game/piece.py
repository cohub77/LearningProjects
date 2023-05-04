class Piece:
    def __init__(self, piece_type, color, row, col):
        self.piece_type = piece_type
        self.color = color
        self.row = row
        self.col = col

    def __str__(self):
        return f"{self.color} {self.piece_type} at ({self.row}, {self.col})"

    def is_valid_move(self, dest_row, dest_col, pieces):
        pass



class Pawn(Piece):
    def is_valid_move(self, dest_row, dest_col, pieces):
        flag = True
        for piece in pieces:
                    if piece.row == dest_row and piece.col == dest_col and piece.color != self.color:
                        flag = False
        # Pawns can move forward one or two squares from their starting row
        if self.color == "White":
            if dest_row == self.row + 1 and dest_col == self.col:
                return flag
            elif dest_row == self.row + 2 and dest_col == self.col and self.row == 1:
                return flag
            # Pawns can capture diagonally
            elif dest_row == self.row + 1 and abs(dest_col - self.col) == 1:
                # Check if there is a piece of the opposite color at the destination square
                for piece in pieces:
                    if piece.row == dest_row and piece.col == dest_col and piece.color != self.color:
                        return True
        else:
            if dest_row == self.row - 1 and dest_col == self.col:
                return flag
            elif dest_row == self.row - 2 and dest_col == self.col and self.row == 6:
                return flag
            # Pawns can capture diagonally
            elif dest_row == self.row - 1 and abs(dest_col - self.col) == 1:
                # Check if there is a piece of the opposite color at the destination square
                for piece in pieces:
                    if piece.row == dest_row and piece.col == dest_col and piece.color != self.color:
                        return True
class Bishop(Piece):
    def is_valid_move(self, dest_row, dest_col, pieces):
        if abs(dest_row - self.row) == abs(dest_col - self.col):
                # Check if the path is clear
                row_step = (dest_row - self.row) // abs(dest_row - self.row)
                col_step = (dest_col - self.col) // abs(dest_col - self.col)
                current_row = self.row + row_step
                current_col = self.col + col_step
                while current_row != dest_row or current_col != dest_col:
                    # Check if there is a piece at this position
                    for piece in pieces:
                        if piece.row == current_row and piece.col == current_col:
                            return False
                    current_row += row_step
                    current_col += col_step
                # Check if there is a piece of the same color at the destination square
                for piece in pieces:
                    if piece.row == dest_row and piece.col == dest_col and piece.color == self.color:
                        return False
                return True

class Queen(Piece):
    def is_valid_move(self, dest_row, dest_col, pieces):
         if abs(dest_row - self.row) == abs(dest_col - self.col) or dest_row == self.row or dest_col == self.col:
                # Check if the path is clear
                if dest_row == self.row:
                    col_step = (dest_col - self.col) // abs(dest_col - self.col)
                    current_col = self.col + col_step
                    while current_col != dest_col:
                        # Check if there is a piece at this position
                        for piece in pieces:
                            if piece.row == dest_row and piece.col == current_col:
                                return False
                        current_col += col_step
                elif dest_col == self.col:
                    row_step = (dest_row - self.row) // abs(dest_row - self.row)
                    current_row = self.row + row_step
                    while current_row != dest_row:
                        # Check if there is a piece at this position
                        for piece in pieces:
                            if piece.row == current_row and piece.col == dest_col:
                                return False
                        current_row += row_step
                else:
                    row_step = (dest_row - self.row) // abs(dest_row - self.row)
                    col_step = (dest_col - self.col) // abs(dest_col - self.col)
                    current_row = self.row + row_step
                    current_col = self.col + col_step
                    while current_row != dest_row or current_col != dest_col:
                        # Check if there is a piece at this position
                        for piece in pieces:
                            if piece.row == current_row and piece.col == current_col:
                                return False
                        current_row += row_step
                        current_col += col_step
                # Check if there is a piece of the same color at the destination square
                for piece in pieces:
                    if piece.row == dest_row and piece.col == dest_col and piece.color == self.color:
                        return False
                return True
            
class Knight(Piece):
    
    def is_valid_move(self, dest_row, dest_col, pieces):
        # Knights can move to any of the squares immediately adjacent to it horizontally or vertically and then one square diagonally
            if abs(dest_row - self.row) == 2 and abs(dest_col - self.col) == 1 or abs(dest_row - self.row) == 1 and abs(dest_col - self.col) == 2:
                # Check if there is a piece of the same color at the destination square
                for piece in pieces:
                    if piece.row == dest_row and piece.col == dest_col and piece.color == self.color:
                        return False
                return True
            
class Rook(Piece):
    def is_valid_move(self, dest_row, dest_col, pieces):
        # Rooks can move any number of squares along a rank or file
            if dest_row == self.row or dest_col == self.col:
                # Check if the path is clear
                if dest_row == self.row:
                    col_step = (dest_col - self.col) // abs(dest_col - self.col)
                    current_col = self.col + col_step
                    while current_col != dest_col:
                        # Check if there is a piece at this position
                        for piece in pieces:
                            if piece.row == dest_row and piece.col == current_col:
                                return False
                        current_col += col_step
                else:
                    row_step = (dest_row - self.row) // abs(dest_row - self.row)
                    current_row = self.row + row_step
                    while current_row != dest_row:
                        # Check if there is a piece at this position
                        for piece in pieces:
                            if piece.row == current_row and piece.col == dest_col:
                                return False
                        current_row += row_step
                # Check if there is a piece of the same color at the destination square
                for piece in pieces:
                    if piece.row == dest_row and piece.col == dest_col and piece.color == self.color:
                        return False
                return True
            
class King(Piece):
        def is_valid_move(self, dest_row, dest_col, pieces):
            # Kings can move one square in any direction
                if abs(dest_row - self.row) <= 1 and abs(dest_col - self.col) <= 1:
                    # Check if there is a piece of the same color at the destination square
                    for piece in pieces:
                        if piece.row == dest_row and piece.col == dest_col and piece.color == self.color:
                            return False
                    return True