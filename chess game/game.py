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

def select_different_piece(row, col, current_player, pieces):
    for piece in pieces:
        if piece.row == row and piece.col == col and piece.color == current_player:
            return piece
    return None

def move_piece(selected_piece, row, col, pieces):
    selected_piece.row = row
    selected_piece.col = col
    for piece in pieces:
        if piece.row == row and piece.col == col and piece.color != selected_piece.color:
            pieces.remove(piece)
            break

def on_click(event, selected_piece, current_player, pieces, board, draw_board, images):
    row = event.y // 50
    col = event.x // 50
    king_in_check = is_in_check(current_player, pieces)

    if not selected_piece:
        # If no piece is selected, try to select one
        for piece in pieces:
            if piece.row == row and piece.col == col and piece.color == current_player:
                selected_piece = piece
                draw_board(board, pieces, images, selected_piece)
                break
    else:
        # If a piece is selected, handle move attempt
        if selected_piece.row == row and selected_piece.col == col:
            # Deselect the piece if the clicked square is the current position of the piece
            selected_piece = None
            draw_board(board, pieces, images, selected_piece)
        elif selected_piece.is_valid_move(row, col, pieces):
            # If the move is valid, simulate it with a copy of the pieces list
            pieces_copy = [piece.copy() if piece == selected_piece else piece for piece in pieces]
            move_piece(selected_piece, row, col, pieces_copy)

            # Check if the move gets the player out of check
            if not king_in_check or (king_in_check and not is_in_check(current_player, pieces_copy)):
                move_piece(selected_piece, row, col, pieces)

                # Capture the opponent's piece if there is one in the destination square
                for piece in pieces:
                    if piece.row == row and piece.col == col and piece.color != selected_piece.color:
                        pieces.remove(piece)
                        break

                draw_board(board, pieces, images, None)
                selected_piece = None

                # Switch to the other player
                if current_player == "White":
                    current_player = "Black"
                else:
                    current_player = "White"

                # Check if the next player is in check
                if is_in_check(current_player, pieces):
                    print(f"{current_player} is in check!")
            else:
                print(f"{current_player}'s king is in check. Invalid move.")
                selected_piece = None
                draw_board(board, pieces, images, selected_piece)
        else:
            # Deselect the piece after an invalid move
            selected_piece = None
            draw_board(board, pieces, images, selected_piece)

    return selected_piece, current_player
   
            
def draw_board(board, pieces, images, selected_piece):
    board.delete("all")
    for i in range(8):
        for j in range(8):
            if (i + j) % 2 == 0:
                color = "white"
            else:
                color = "gray"
            board.create_rectangle(i * 50, j * 50, (i + 1) * 50, (j + 1) * 50, fill=color)
            if selected_piece and selected_piece.row == j and selected_piece.col == i:
                board.create_rectangle(i * 50, j * 50, (i + 1) * 50, (j + 1) * 50, outline="red", width=4)
    for piece in pieces:
        if piece.color == "White":
            color = "white"
        else:
            color = "black"
        image_name = f"chess game/pieces/{color}_{piece.piece_type.lower()}.png"
        image = images[image_name]
        board.create_image(piece.col * 50 + 25, piece.row * 50 + 25, image=image)