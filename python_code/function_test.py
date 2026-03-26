from kipy import KiCad, board_types

if __name__=='__main__':
    kicad = KiCad()
    board = kicad.get_board()
    layer = board.get_active_layer()
    rect = board_types.BoardRectangle()
    rect.top_left = board_types.Vector2.from_xy(50000000,50000000)
    rect.bottom_right = board_types.Vector2.from_xy(150000000, 150000000)
    rect.layer = layer
    rect.attributes.stroke.width = 500000
    
    board.create_items(rect)
