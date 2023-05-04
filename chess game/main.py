import tkinter as tk
from piece import Piece, Pawn, Bishop, Queen, King, Rook, Knight
from game import on_click, draw_board

def handle_click(event):
    global selected_piece, current_player, turn_label_var
    selected_piece, current_player = on_click(event, selected_piece, current_player, pieces, board, draw_board, images)
    turn_label_var.set(f"Current player: {current_player}")


root = tk.Tk()
root.title("Chess Board")
turn_label_var = tk.StringVar()
turn_label_var.set("Current player: White")
board = tk.Canvas(root, width=400, height=400)
board.pack()
turn_label = tk.Label(root, textvariable=turn_label_var)
turn_label.pack()
# Create all the chess pieces
pieces = []
for i in range(8):
    pieces.append(Pawn("Pawn", "White", 1, i))
    pieces.append(Pawn("Pawn", "Black", 6, i))
piece_types = [Rook, Knight, Bishop, King, Queen, Bishop, Knight, Rook]
for i in range(8):
    piece_class = piece_types[i]
    pieces.append(piece_class(piece_class.__name__, "White", 0, i))
    pieces.append(piece_class(piece_class.__name__, "Black", 7, i))
# Load images for all the pieces
images = {}
for color in ["white", "black"]:
    for piece_type in ["pawn", "rook", "knight", "bishop", "queen", "king"]:
        image_name = f"chess game/pieces/{color}_{piece_type}.png"
        images[image_name] = tk.PhotoImage(file=image_name)

selected_piece = None
current_player = "White"

draw_board(board ,pieces ,images, selected_piece)
board.bind("<Button-1>", handle_click)

root.mainloop()

# Rest of your code here