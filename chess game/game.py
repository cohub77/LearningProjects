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
    king_in_check = is_in_check(current_player, pieces)
    if selected_piece:
        # Check if the move is valid
        if selected_piece.row == row and selected_piece.col == col:
            selected_piece = None
            draw_board(board, pieces, images, selected_piece)
        else:
            # Allow the player to select a different piece
            for piece in pieces:
                if piece.row == row and piece.col == col and piece.color == current_player:
                    selected_piece = piece
                    draw_board(board, pieces, images, selected_piece)
                    break
            else:
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
                    if not king_in_check or (king_in_check and not is_in_check(current_player, pieces_copy)):                        # Move the selected piece to the clicked square
                        selected_piece.row = row
                        selected_piece.col = col
                        # Check if a piece of the opposite color was captured
                        for piece in pieces:
                            if piece.row == row and piece.col == col and piece.color != selected_piece.color:
                                pieces.remove(piece)
                                break
                        # Delete the rectangle around the selected square
                        selected_piece = None  # Add this line to deselect the piece after it has been moved
                        # Switch to the other player
                        draw_board(board, pieces, images, selected_piece)
                        if current_player == "White":
                            next_player_color = "Black"
                        else:
                            next_player_color = "White"
                        
                        # Check if the next player is in check
                        if is_in_check(next_player_color, pieces):
                            print(f"{next_player_color} is in check!")
                        
                        current_player = next_player_color

                    else:
                        print(f"{current_player}'s king is in check. Invalid move.")
    

    else:
        selected_piece = None
        for piece in pieces:
            if piece.row == row and piece.col == col and piece.color == current_player:
                selected_piece = piece
                draw_board(board, pieces, images, selected_piece)
                break
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