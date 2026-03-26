from kipy import KiCad
def main():
    kicad = KiCad()
    board = kicad.get_board()

    selection = board.get_selection()
    #do stuff
    board.create_items(items) or board.update_items(items)

if __name__ == "__main__":
    main()
