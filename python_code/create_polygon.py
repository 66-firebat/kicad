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
