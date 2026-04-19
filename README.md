# Rectangle Plugin for KiCad

This plugin adds a dialog to draw a rectangle on a PCB using user-entered width, height, and layer.

## What was fixed

- Corrected Python syntax so `Run` is properly defined as a method of `RectanglePlugin`.
- Removed duplicate `import wx` and made `pcbnew` import conditional for standalone testing.
- Added a standalone debug mode so the dialog can be executed directly from VS Code.
- Replaced the unsupported `pcbnew.GetCursorPosition()` call with board center placement using `board.GetBoardEdgesBoundingBox()`.
- Added `User.1` and `User.2` layer options in the dialog and mapped them to `pcbnew.User_1` and `pcbnew.User_2`.
- Updated dialog parenting logic to prefer the KiCad PCB editor window so the script does not switch to the project view.

## Files

- `rectangle_plugin.py` — main plugin script
- `__init__.py` — plugin package marker

## Required environment

- KiCad 9.0 with Python scripting enabled
- `wxPython` installed for standalone dialog debugging
- A Python interpreter that is compatible with your system and KiCad installation

## Installation

1. Place the plugin folder in your KiCad scripting plugins directory:
   - `~/.local/share/kicad/9.0/scripting/plugins/rectangle_plugin`
2. Make sure the folder contains both `__init__.py` and `rectangle_plugin.py`.
3. Restart KiCad.
4. Open a PCB in KiCad and run the plugin from the plugin menu or the toolbar.

## Debugging in VS Code

1. Install the Python extension in VS Code.
2. Use a supported Python interpreter, such as Miniconda Python, if your system Python has compatibility issues.
3. Install `wxPython` in the selected interpreter.
4. Open `rectangle_plugin.py` in VS Code.
5. Set breakpoints in the script.
6. Run the script in debug mode.

### Recommended standalone debug setup

```bash
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda.sh
bash ~/miniconda.sh -b -p ~/miniconda
~/miniconda/bin/conda tos accept --override-channels --channel https://repo.anaconda.com/pkgs/main
~/miniconda/bin/conda tos accept --override-channels --channel https://repo.anaconda.com/pkgs/r
~/miniconda/bin/conda install -c conda-forge wxpython -y
```

Then select `~/miniconda/bin/python` as the VS Code Python interpreter.

## Usage notes

- `rectangle_plugin.py` can run in two modes:
  - Standalone debug mode via `python rectangle_plugin.py` (dialog only)
  - KiCad plugin mode when loaded inside KiCad (creates a PCB rectangle)
- The plugin now avoids unsupported KiCad APIs and uses board center placement instead of cursor position.
- If KiCad switches windows unexpectedly, the dialog will try to attach to the PCB editor window.

## Layer options supported

- `F.SilkS`
- `B.SilkS`
- `F.Cu`
- `B.Cu`
- `User.1`
- `User.2`

## Troubleshooting

- If you see errors about `pcbnew` when running standalone, run the script from within KiCad or use the standalone debug environment.
- If you see a glibc or symbol lookup error, use a separate Python environment such as Miniconda.
- If the plugin does not appear in KiCad, verify the folder location and restart KiCad.

## Notes

- The plugin uses `pcbnew` only when running inside KiCad.
- Standalone execution is intended for debugging the dialog and input handling only.
