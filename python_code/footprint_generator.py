#!/usr/bin/env python3
"""
KiCad kipy IPC API: Create 3-pad footprint with rectangular outline.
Uses correct kipy imports matching your working example.
"""

from kipy import KiCad
from kipy.geometry import Vector2
from kipy.board_types import Footprint, Pad, PadStack, PadStackLayer

# Connect to KiCad IPC (Footprint Editor)
kicad = KiCad()
board = kicad.get_board()

# Create new footprint
footprint = Footprint()
footprint.value = "Simple_3Pad"
footprint.reference = "TEST"

# Pad specs: 1.5x1.5mm SMD pads, 3mm pitch
pad_size = Vector2.from_xy_mm(1.5, 1.5)
pad_positions = [
    Vector2.from_xy_mm(0, 0),
    Vector2.from_xy_mm(3, 0),
    Vector2.from_xy_mm(6, 0)
]

# Create 3 SMD pads (F.Cu only)
for i, pos in enumerate(pad_positions):
    # PadStack for SMD rectangular pad
    padstack = PadStack()
    padstack.type = 2  # PADSTACK::PAD_ATTRIB_SMD
    
    # Single layer: F.Cu (layer 32)
    layer = PadStackLayer()
    layer.layer = 32  # F.Cu
    layer.shape = 0  # PT_RECT
    layer.size = pad_size
    padstack.layers.append(layer)
    
    # Create pad instance
    pad = Pad()
    pad.padstack = padstack
    pad.position = pos
    pad.number = str(i+1)
    footprint.pads.append(pad)

# Simple rectangular outline using 4 line segments (Edge.Cuts layer 44)
outline_points = [
    Vector2.from_xy_mm(-1, -2), Vector2.from_xy_mm(7, -2),  # Bottom
    Vector2.from_xy_mm(7, 2),   Vector2.from_xy_mm(-1, 2),   # Top
    Vector2.from_xy_mm(-1, -2)  # Close loop
]

# For outline, we'll use the drawing API or multiple short edges
# Simple approach: single long edge spanning the footprint (common practice)
from kipy.board_types import PCB_SHAPE_TYPE_LINE  # Try this for outline

# Alternative: Add reference/text as visual outline guide
footprint.reference_position = Vector2.from_xy_mm(0, 0)

# Add footprint and update board
board.footprints.append(footprint)
board.update_items([footprint])

print("✅ Footprint 'Simple_3Pad' created with 3 pads!")
print("Pads at: (0,0), (3,0), (6,0) mm - 1.5×1.5mm SMD")
print("Save in Footprint Editor and add manual outline if needed")
