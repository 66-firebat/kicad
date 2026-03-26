#!/usr/bin/env python3
from kipy import KiCad
from kipy.board_types import FootprintInstance, BoardRectangle
from kipy.geometry import Vector2
from kipy.board import BoardLayer

def main():
    kicad = KiCad()
    print("✅ Connected to KiCad")

    board = kicad.get_board()
    print("✅ Board found")

    commit = board.begin_commit()

    try:
        # Draw a 40x30mm board outline on Edge.Cuts
        outline = BoardRectangle()
        outline.layer = BoardLayer.BL_Edge_Cuts
        outline.start = Vector2.from_xy_mm(100, 100)
        outline.end   = Vector2.from_xy_mm(140, 130)
        board.create_items(outline)
        print("✅ Board outline drawn (40 x 30 mm)")

        # Place a single R_0805 resistor in the centre
        resistor = FootprintInstance()
        resistor.definition.id.library_nickname  = "Device"
        resistor.definition.id.entry_name        = "R_0805_2012Metric"
        resistor.reference_field.text.value      = "R1"   # <-- fixed
        resistor.value_field.text.value          = "10k"  # <-- fixed
        resistor.position                        = Vector2.from_xy_mm(120, 115)
        resistor.layer                           = BoardLayer.BL_F_Cu
        board.create_items(resistor)
        print("✅ Resistor R1 placed at centre of board")

        board.push_commit(commit)
        print("\n🎉 Done! Check the PCB editor in KiCad.")

    except Exception as e:
        board.drop_commit(commit)
        print(f"❌ Something went wrong, changes rolled back: {e}")
        raise

if __name__ == "__main__":
    main()
