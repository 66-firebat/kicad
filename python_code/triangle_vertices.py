#!/usr/bin/env python3
from kipy import KiCad
from kipy.board_types import FootprintInstance, BoardRectangle, BoardPolygon
from kipy.geometry import Vector2, PolygonWithHoles, PolyLineNode
from kipy.board import BoardLayer

def create_polygon(vertices, layer, netname, board):
    boardpolygon = BoardPolygon()
    polygon = PolygonWithHoles()
    for v in vertices:
        polygon.outline.append(PolyLineNode.from_point(v))
    polygon.outline.closed = True
    boardpolygon.polygons.append(polygon)
    boardpolygon.attributes.fill.filled = True
    boardpolygon.layer = layer
    boardpolygon.net.name = netname
    board.create_items(boardpolygon)

def main():
    kicad = KiCad()
    print("✅ Connected to KiCad")

    board = kicad.get_board()
    print("✅ Board found")

    commit = board.begin_commit()

    try:
        # Board outline on Edge.Cuts
        outline = BoardRectangle()
        outline.layer = BoardLayer.BL_Edge_Cuts
        outline.start = Vector2.from_xy_mm(100, 100)
        outline.end   = Vector2.from_xy_mm(140, 130)
        board.create_items(outline)
        print("✅ Board outline drawn (40 x 30 mm)")

        # Filled copper polygon on F.Cu — a simple triangle
        triangle_vertices = [
            Vector2.from_xy_mm(110, 105),
            Vector2.from_xy_mm(130, 105),
            Vector2.from_xy_mm(120, 125),
        ]
        create_polygon(
            vertices=triangle_vertices,
            layer=BoardLayer.BL_F_Cu,
            netname="",   # empty string = unconnected
            board=board,
        )
        print("✅ Filled copper polygon drawn on F.Cu")

        # Place a resistor in the centre
        resistor = FootprintInstance()
        resistor.definition.id.library_nickname = "Device"
        resistor.definition.id.entry_name       = "R_0805_2012Metric"
        resistor.reference_field.text.value     = "R1"
        resistor.value_field.text.value         = "10k"
        resistor.position                       = Vector2.from_xy_mm(120, 115)
        resistor.layer                          = BoardLayer.BL_F_Cu
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
