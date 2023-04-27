import tkinter as tk

class Piece:
    def __init__(self, piece_type, color, row, col):
        self.piece_type = piece_type
        self.color = color
        self.row = row
        self.col = col

    def __str__(self):
        return f"{self.color} {self.piece_type} at ({self.row}, {self.col})"

    def is_valid_move(self, dest_row, dest_col):
        if self.piece_type == "Pawn":
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
        elif self.piece_type == "Bishop":
            # Bishops can move any number of squares diagonally
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
    # Other pieces not implemented yet
        elif self.piece_type == "Queen":
    # Queens can move any number of squares along a rank, file, or diagonal
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
        elif self.piece_type == "Rook":
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
        elif self.piece_type == "Knight":
            # Knights can move to any of the squares immediately adjacent to it horizontally or vertically and then one square diagonally
            if abs(dest_row - self.row) == 2 and abs(dest_col - self.col) == 1 or abs(dest_row - self.row) == 1 and abs(dest_col - self.col) == 2:
                # Check if there is a piece of the same color at the destination square
                for piece in pieces:
                    if piece.row == dest_row and piece.col == dest_col and piece.color == self.color:
                        return False
                return True
        elif self.piece_type == "King":
            # Kings can move one square in any direction
            if abs(dest_row - self.row) <= 1 and abs(dest_col - self.col) <= 1:
                # Check if there is a piece of the same color at the destination square
                for piece in pieces:
                    if piece.row == dest_row and piece.col == dest_col and piece.color == self.color:
                        return False
                return True
def on_click(event):
    global selected_piece, current_player
    row = event.y // 50
    col = event.x // 50
    # Dra        w a rectangle around the selected square
    x0 = col * 50
    y0 = row * 50
    x1 = x0 + 50
    y1 = y0 + 50
    board.create_rectangle(x0, y0, x1, y1, outline="red", width=3, tags="selected_square")
    if selected_piece:
        # Check if the move is valid
        if selected_piece.is_valid_move(row, col):
            # Move the selected piece to the clicked square
            selected_piece.row = row
            selected_piece.col = col
            # Check if a piece of the opposite color was captured
            for piece in pieces:
                if piece.row == row and piece.col == col and piece.color != selected_piece.color:
                    pieces.remove(piece)
                    break
            draw_board()
            # Delete the rectangle around the selected square
            board.delete("selected_square")
            # Switch to the other player
            if current_player == "White":
                current_player = "Black"
            else:
                current_player = "White"
        selected_piece = None      
        board.delete("selected_square")

    else:
        # Check if a piece of the current player's color was clicked
        for piece in pieces:
            if piece.row == row and piece.col == col and piece.color == current_player:
                selected_piece = piece
                break
            
        
def draw_board():
    board.delete("all")
    for i in range(8):
        for j in range(8):
            if (i + j) % 2 == 0:
                color = "white"
            else:
                color = "gray"
            board.create_rectangle(i * 50, j * 50, (i + 1) * 50, (j + 1) * 50, fill=color)
    for piece in pieces:
        if piece.color == "White":
            color = "white"
        else:
            color = "black"
        image_name = f"pieces/{color}_{piece.piece_type.lower()}.png"
        image = images[image_name]
        board.create_image(piece.col * 50 + 25, piece.row * 50 + 25, image=image)

root = tk.Tk()
root.title("Chess Board")

board = tk.Canvas(root, width=400, height=400)
board.pack()
board.bind("<Button-1>", on_click)

# Create all the chess pieces
pieces = []
for i in range(8):
    pieces.append(Piece("Pawn", "White", 1, i))
    pieces.append(Piece("Pawn", "Black", 6, i))
piece_types = ["Rook", "Knight", "Bishop", "King", "Queen", "Bishop", "Knight", "Rook"]
for i in range(8):
    pieces.append(Piece(piece_types[i], "White", 0, i))
    pieces.append(Piece(piece_types[i], "Black", 7, i))
# Load images for all the pieces
images = {}
for color in ["white", "black"]:
    for piece_type in ["pawn", "rook", "knight", "bishop", "queen", "king"]:
        image_name = f"pieces/{color}_{piece_type}.png"
        images[image_name] = tk.PhotoImage(file=image_name)

selected_piece = None
current_player = "White"

draw_board()

root.mainloop()