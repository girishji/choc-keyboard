# Place footprints console script
#
# To run as script in python console,
#   place or symplink this script to ~/Documents/KiCad/6.0/scripting/plugins
#   Run from python console using 'import placesw'
#   To reapply:
#     import importlib
#     importlib.reload(placefp)
#  OR
#    exec(open("path-to-script-file").read())

import pcbnew

Width = 19
Height = 18


def place_switches():
    board = pcbnew.GetBoard()
    rows = [
        [
            board.FindFootprintByReference("S" + str(num))
            for num in range(i, 15 * 5 + i, 5)
        ]
        for i in range(1, 6)
    ]
    # row 1
    for i, fp in enumerate(rows[0]):
        fp.SetPosition(pcbnew.wxPointMM(i * Width, Height))
    # row 2
    for i, fp in enumerate(rows[1]):
        if i == 0:
            fp.SetPosition(pcbnew.wxPointMM(0.25 * Width, Height * 2))
        else:
            fp.SetPosition(pcbnew.wxPointMM(1.5 * Width + Width * (i - 1), Height * 2))
    # row 3
    for i, fp in enumerate(rows[2]):
        if i < 13:
            fp.SetPosition(pcbnew.wxPointMM(-0.25 * Width + i * Width, Height * 3))
        elif i == 13:
            fp.SetPosition(pcbnew.wxPointMM(i * Width, Height * 3))
        else:
            fp.SetPosition(pcbnew.wxPointMM(0.25 * Width + i * Width, Height * 3))
    # row 4
    for i, fp in enumerate(rows[3]):
        if i == 0:
            fp.SetPosition(pcbnew.wxPointMM(0, Height * 4))
        elif i < 12:
            fp.SetPosition(pcbnew.wxPointMM(0.25 * Width + i * Width, Height * 4))
        elif i == 12:
            fp.SetPosition(pcbnew.wxPointMM(0.5 * Width + i * Width, Height * 4))
        else:
            fp.SetPosition(pcbnew.wxPointMM(0.75 * Width + i * Width, Height * 4))
    # row 5
    for i, fp in enumerate(rows[4]):
        fp.SetOrientation(0)
        if i < 4:
            fp.SetPosition(pcbnew.wxPointMM(-0.5 * Width + i * Width, Height * 5))
        elif i == 4:
            fp.SetPosition(pcbnew.wxPointMM(-0.25 * Width + i * Width, Height * 5))
        elif i == 5:
            fp.SetPosition(pcbnew.wxPointMM(i * Width + 0.5, Height * 5.5))
            fp.Rotate(fp.GetPosition(), -(15 + 90) * 10)
        elif i == 6:
            fp.SetPosition(pcbnew.wxPointMM(0.25 * Width + i * Width, Height * 5))
        elif i == 7:
            fp.SetPosition(
                pcbnew.wxPointMM(0.5 * Width + i * Width - 0.5, Height * 5.5)
            )
            fp.Rotate(fp.GetPosition(), (15 + 90) * 10)
        elif i < 12:
            fp.SetPosition(pcbnew.wxPointMM(0.5 * Width + i * Width, Height * 5))
        else:
            fp.SetPosition(pcbnew.wxPointMM(0.75 * Width + i * Width, Height * 5))

    pcbnew.Refresh()


def place_mcus():
    board = pcbnew.GetBoard()
    ada = board.FindFootprintByReference("U1")
    if ada:
        ada.SetPosition(pcbnew.wxPointMM(6 * Width - 16, Height * 6 - 2))
        ada.SetOrientation(0)

    bp = board.FindFootprintByReference("U2")
    if bp:
        bp.SetOrientation(90 * 10)
        bp.SetPosition(pcbnew.wxPointMM(2, 2 * Height + 2))

    pcbnew.Refresh()


def place_screws():
    board = pcbnew.GetBoard()
    for i in range(1, 6):
        hole = board.FindFootprintByReference("H" + str(i))
        if not hole:
            return
        hole.SetPosition(
            pcbnew.wxPointMM(0.5 * Width + (i - 1) * 3 * Width, Height * 0.85)
        )

    hole = board.FindFootprintByReference("H6")
    hole.SetPosition(pcbnew.wxPointMM(0.5 * Width + 19 / 8 - 2, Height * (3 + 1.4)))
    hole = board.FindFootprintByReference("H7")
    hole.SetPosition(pcbnew.wxPointMM(2 * Width, Height * (4 + 0.85)))
    hole = board.FindFootprintByReference("H8")
    hole.SetPosition(pcbnew.wxPointMM(4 * Width + 19 / 4 + 2, Height * (5 + 0.05)))
    hole = board.FindFootprintByReference("H9")
    hole.SetPosition(pcbnew.wxPointMM(7.75 * Width, Height * (4 + 0.65)))
    hole = board.FindFootprintByReference("H10")
    hole.SetPosition(pcbnew.wxPointMM(12 * Width + 19 / 8, Height * (4 + 0.85)))
    hole = board.FindFootprintByReference("H11")
    hole.SetPosition(pcbnew.wxPointMM(14.25 * Width, Height * (4 + 0.85)))
    hole = board.FindFootprintByReference("H12")
    hole.SetPosition(pcbnew.wxPointMM(13.75 * Width - 19 / 8, Height * (2 + 0.85)))
    hole = board.FindFootprintByReference("H13")
    hole.SetPosition(pcbnew.wxPointMM(11.75 * Width + 19 / 8, Height * (3 + 0.65)))
    hole = board.FindFootprintByReference("H14")
    hole.SetPosition(pcbnew.wxPointMM(10.125 * Width + 19 / 8, Height * (2 + 0.85)))
    hole = board.FindFootprintByReference("H15")
    hole.SetPosition(pcbnew.wxPointMM(8.125 * Width + 19 / 8, Height * (2 + 0.85)))
    hole = board.FindFootprintByReference("H16")
    hole.SetPosition(pcbnew.wxPointMM(6.125 * Width + 19 / 8, Height * (2 + 0.85)))
    hole = board.FindFootprintByReference("H17")
    hole.SetPosition(pcbnew.wxPointMM(2.125 * Width + 19 / 8, Height * (2 + 0.85)))

    # small holes (18 to 25)
    hole = board.FindFootprintByReference("H18")
    hole.SetPosition(pcbnew.wxPointMM(1.5 * Width, Height * 0.85))
    hole = board.FindFootprintByReference("H19")
    hole.SetPosition(pcbnew.wxPointMM(5.5 * Width, Height * 0.85))
    hole = board.FindFootprintByReference("H20")
    hole.SetPosition(pcbnew.wxPointMM(11.5 * Width, Height * 0.85))
    hole = board.FindFootprintByReference("H21")
    hole.SetPosition(pcbnew.wxPointMM(12.5 * Width - 19 / 8, Height * (2 + 0.85)))
    hole = board.FindFootprintByReference("H22")
    hole.SetPosition(pcbnew.wxPointMM(12 * Width + 19 / 8, Height * (5 + 0.25)))
    hole = board.FindFootprintByReference("H23")
    hole.SetPosition(pcbnew.wxPointMM(7.4 * Width, Height * (4 + 0.65)))
    hole = board.FindFootprintByReference("H24")
    hole.SetPosition(pcbnew.wxPointMM(0 * Width, Height * (4 + 0.95)))
    hole = board.FindFootprintByReference("H25")
    hole.SetPosition(pcbnew.wxPointMM(3.125 * Width + 19 / 8, Height * 3))

    pcbnew.Refresh()


place_switches()
place_mcus()
place_screws()
