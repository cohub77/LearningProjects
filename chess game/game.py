def is_in_check(player_color, pieces):
    # Find the king of the player whose turn it is
    for piece in pieces:
        if piece.piece_type == "King" and piece.color == player_color:
            king = piece
            break

    # Check if any of the opponent's pieces can move to the king's square
    for piece in pieces:
        if piece.color != player_color:
            if piece.is_valid_move(king.row, king.col, pieces):
                return True

    return False

def on_click(event, selected_piece, current_player, pieces, board, draw_board, images):
    row = event.y // 50
    col = event.x // 50
    # Draw a rectangle around the selected square
    x0 = col * 50
    y0 = row * 50
    x1 = x0 + 50
    y1 = y0 + 50
    board.create_rectangle(x0, y0, x1, y1, outline="red", width=3, tags="selected_square")
    if selected_piece:
        # Check if the move is valid
        if selected_piece.is_valid_move(row, col, pieces):
            # Make a copy of the pieces list to simulate the move
            pieces_copy = [piece for piece in pieces]
            for piece in pieces_copy:
                if piece == selected_piece:
                    piece.row = row
                    piece.col = col
                if piece.row == row and piece.col == col and piece.color != selected_piece.color:
                    pieces_copy.remove(piece)
            
            # Check if the move gets the player out of check
            if not is_in_check(current_player, pieces_copy):
                # Move the selected piece to the clicked square
                selected_piece.row = row
                selected_piece.col = col
                # Check if a piece of the opposite color was captured
                for piece in pieces:
                    if piece.row == row and piece.col == col and piece.color != selected_piece.color:
                        pieces.remove(piece)
                        break
                draw_board(board, pieces, images)
                # Delete the rectangle around the selected square
                board.delete("selected_square")
                # Switch to the other player
                if current_player == "White":
                    next_player_color = "Black"
                else:
                    next_player_color = "White"
                
                # Check if the next player is in check
                if is_in_check(next_player_color, pieces):
                    print(f"{next_player_color} is in check!")
                
                current_player = next_player_color

        selected_piece = None      
        board.delete("selected_square")

    else:
        # Check if a piece of the current player's color was clicked
        for piece in pieces:
            if piece.row == row and piece.col == col and piece.color == current_player:
                selected_piece = piece
                break

    return selected_piece, current_player
            
def draw_board(board, pieces, images):
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
        image_name = f"chess game/pieces/{color}_{piece.piece_type.lower()}.png"
        image = images[image_name]
        board.create_image(piece.col * 50 + 25, piece.row * 50 + 25, image=image)