import pcbnew
import wx

import wx

class RectangleDialog(wx.Dialog):
    def __init__(self, parent):
        super().__init__(parent, title="Create Rectangle")

        main_sizer = wx.BoxSizer(wx.VERTICAL)

        grid = wx.FlexGridSizer(3, 2, 5, 5)
        grid.AddGrowableCol(1, 1)

        # Width
        grid.Add(wx.StaticText(self, label="Width (mm):"),
                 0, wx.ALIGN_CENTER_VERTICAL)
        self.width_input = wx.TextCtrl(self)
        grid.Add(self.width_input, 1, wx.EXPAND)

        # Height
        grid.Add(wx.StaticText(self, label="Height (mm):"),
                 0, wx.ALIGN_CENTER_VERTICAL)
        self.height_input = wx.TextCtrl(self)
        grid.Add(self.height_input, 1, wx.EXPAND)

        # Layer
        grid.Add(wx.StaticText(self, label="Layer:"),
                 0, wx.ALIGN_CENTER_VERTICAL)
        self.layer_choice = wx.Choice(self, choices=[
            "F.SilkS", "B.SilkS", "F.Cu", "B.Cu"
        ])
        self.layer_choice.SetSelection(0)
        grid.Add(self.layer_choice, 1, wx.EXPAND)

        main_sizer.Add(grid, 1, wx.EXPAND | wx.ALL, 10)

        # Buttons
        btns = self.CreateButtonSizer(wx.OK | wx.CANCEL)
        main_sizer.Add(btns, 0, wx.EXPAND | wx.ALL, 10)

        self.SetSizer(main_sizer)
        self.SetMinSize((300, 200))
        self.Fit()
        self.Layout()
        self.Centre()
        
    def get_values(self):
        try:
            width = float(self.width_input.GetValue())
            height = float(self.height_input.GetValue())
        except ValueError:
            return None, None, None

        layer_map = {
            "F.SilkS": pcbnew.F_SilkS,
            "B.SilkS": pcbnew.B_SilkS,
            "F.Cu": pcbnew.F_Cu,
            "B.Cu": pcbnew.B_Cu,
        }

        layer = layer_map[self.layer_choice.GetStringSelection()]

        return width, height, layer


class RectanglePlugin(pcbnew.ActionPlugin):
    def defaults(self):
        self.name = "Draw Rectangle (by size)"
        self.category = "Modify PCB"
        self.description = "Draw a rectangle using entered width and height"
        self.show_toolbar_button = True

def Run(self):
    import wx
    import pcbnew

    board = pcbnew.GetBoard()

    # 🔑 Get KiCad main window (fixes rendering issues)
    parent = wx.GetTopLevelWindows()[0]

    dialog = RectangleDialog(parent)

    if dialog.ShowModal() != wx.ID_OK:
        return

    try:
        width = float(dialog.width_input.GetValue())
        height = float(dialog.height_input.GetValue())
    except ValueError:
        wx.MessageBox("Invalid input!", "Error", wx.OK | wx.ICON_ERROR)
        return

    layer_map = {
        "F.SilkS": pcbnew.F_SilkS,
        "B.SilkS": pcbnew.B_SilkS,
        "F.Cu": pcbnew.F_Cu,
        "B.Cu": pcbnew.B_Cu,
    }

    layer = layer_map[dialog.layer_choice.GetStringSelection()]

    w = pcbnew.FromMM(width)
    h = pcbnew.FromMM(height)

    cursor = pcbnew.GetCursorPosition()

    rect = pcbnew.PCB_SHAPE(board)
    rect.SetShape(pcbnew.SHAPE_T_RECT)
    rect.SetLayer(layer)

    rect.SetStart(cursor)
    rect.SetEnd(pcbnew.VECTOR2I(cursor.x + w, cursor.y + h))

    board.Add(rect)
    pcbnew.Refresh()

Run()