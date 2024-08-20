from game.ClassChess import Chess

def main():
    chess = Chess()
    while True:
        play(chess)

def play(chess):
    try:
        # print(chess.show_board())
        print("turn: ", chess.turn)
        from_row = int(input("From row: "))
        from_col = int(input("From col: "))
        to_row = int(input("To Row: "))
        to_col = int(input("To Col: "))
        # :)
        chess.move(
            from_row,
            from_col,
            to_row,
            to_col,
        )
        print("Move successful!")
    except Exception as e:
        print("error", e)

def show_instructions():
    print("Welcome to Chess!")
    print("Instructions:")
    print("1. Enter the row and column of the piece you want to move.")
    print("2. Enter the row and column of the destination.")
    print("3. Follow the prompts to make your move.")
    print("4. Type 'exit' to quit the game.")

if __name__ == '__main__':
    show_instructions()
    main()