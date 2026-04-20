# KiCad Plugin Template

This is a template for creating KiCad PCB editor plugins with Python scripting.

## Quick Start Template

Copy this structure for new plugins:

### 1. Create Plugin Folder Structure
```
your_plugin_name/
├── __init__.py          # Empty or minimal package marker
├── your_plugin_name.py  # Main plugin script
└── README.md           # Documentation
```

### 2. Plugin Script Template (your_plugin_name.py)

```python
import wx

# Conditional import for KiCad environment
try:
    import pcbnew
    PCBNEW_AVAILABLE = True
except ImportError:
    PCBNEW_AVAILABLE = False
    # Mock classes for standalone debugging
    class ActionPlugin:
        pass
    class BOARD:
        pass
    class PCB_SHAPE:
        def __init__(self, board): pass
        def SetShape(self, shape): pass
        def SetLayer(self, layer): pass
        def SetStart(self, point): pass
        def SetEnd(self, point): pass
    class VECTOR2I:
        def __init__(self, x, y): 
            self.x, self.y = x, y
    pcbnew = type('MockPcbnew', (), {
        'ActionPlugin': ActionPlugin,
        'GetBoard': lambda: BOARD(),
        'FromMM': lambda mm: int(mm * 1000000),  # Mock conversion
        'PCB_SHAPE': PCB_SHAPE,
        'VECTOR2I': VECTOR2I,
        'Refresh': lambda: None,
        'F_SilkS': 0, 'B_SilkS': 1, 'F_Cu': 2, 'B_Cu': 3,
        'User_1': 4, 'User_2': 5,
        'SHAPE_T_RECT': 0
    })()

# Your dialog class
class YourPluginDialog(wx.Dialog):
    def __init__(self, parent):
        super().__init__(parent, title="Your Plugin Title")
        
        # Create your dialog UI here
        main_sizer = wx.BoxSizer(wx.VERTICAL)
        
        # Add controls...
        
        # OK/Cancel buttons
        btns = self.CreateButtonSizer(wx.OK | wx.CANCEL)
        main_sizer.Add(btns, 0, wx.EXPAND | wx.ALL, 10)
        
        self.SetSizer(main_sizer)
        self.Fit()
        self.Centre()
    
    def get_values(self):
        # Return dialog values
        return {}

# Plugin class
class YourPlugin(ActionPlugin if not PCBNEW_AVAILABLE else pcbnew.ActionPlugin):
    def defaults(self):
        self.name = "Your Plugin Name"
        self.category = "Modify PCB"
        self.description = "Description of what your plugin does"
        self.show_toolbar_button = True
    
    def Run(self):
        if not PCBNEW_AVAILABLE:
            print("pcbnew not available - run from within KiCad")
            return
        
        # Get PCB editor window to avoid switching
        parent = None
        for win in wx.GetTopLevelWindows():
            title = win.GetTitle()
            if "PCB" in title and "Editor" in title:
                parent = win
                break
        
        # Show dialog
        dialog = YourPluginDialog(parent)
        if dialog.ShowModal() != wx.ID_OK:
            return
        
        # Get values from dialog
        values = dialog.get_values()
        
        # Get board
        board = pcbnew.GetBoard()
        
        # Perform PCB operations here
        # Example: Add a shape
        # shape = pcbnew.PCB_SHAPE(board)
        # ... configure shape ...
        # board.Add(shape)
        # pcbnew.Refresh()
        
        dialog.Destroy()

# Standalone debugging
if __name__ == "__main__":
    app = wx.App(False)
    frame = wx.Frame(None, title="Debug Frame")
    
    dialog = YourPluginDialog(frame)
    result = dialog.ShowModal()
    
    if result == wx.ID_OK:
        values = dialog.get_values()
        print(f"Values: {values}")
    else:
        print("Dialog cancelled")
    
    dialog.Destroy()
    frame.Destroy()
    app.MainLoop()
```

### 3. __init__.py Template
```python
from .your_plugin_name import YourPluginClass

YourPluginClass().register()
```

**Required Considerations:**
- The `__init__.py` file serves as the package initializer for the plugin.
- It must import the main plugin class from the plugin script (e.g., `your_plugin_name.py`).
- Call the `register()` method on an instance of the plugin class to register it with KiCad.
- Replace `your_plugin_name` with your actual plugin filename and `YourPluginClass` with your plugin class name.
- This ensures the plugin is automatically loaded when KiCad starts and the plugin directory is present.
YourPluginClass().register()
```

**Required Considerations:**
- The `__init__.py` file serves as the package initializer for the plugin.
- It must import the main plugin class from the plugin script (e.g., `your_plugin_name.py`).
- Call the `register()` method on an instance of the plugin class to register it with KiCad.
- Replace `your_plugin_name` with your actual plugin filename and `YourPluginClass` with your plugin class name.
- This ensures the plugin is automatically loaded when KiCad starts and the plugin directory is present.
YourPluginClass().register()
```

**Required Considerations:**
- The `__init__.py` file serves as the package initializer for the plugin.
- It must import the main plugin class from the plugin script (e.g., `your_plugin_name.py`).
- Call the `register()` method on an instance of the plugin class to register it with KiCad.
- Replace `your_plugin_name` with your actual plugin filename and `YourPluginClass` with your plugin class name.
- This ensures the plugin is automatically loaded when KiCad starts and the plugin directory is present.
YourPluginClass().register()
```

**Required Considerations:**
- The `__init__.py` file serves as the package initializer for the plugin.
- It must import the main plugin class from the plugin script (e.g., `your_plugin_name.py`).
- Call the `register()` method on an instance of the plugin class to register it with KiCad.
- Replace `your_plugin_name` with your actual plugin filename and `YourPluginClass` with your plugin class name.
- This ensures the plugin is automatically loaded when KiCad starts and the plugin directory is present.

### 4. README.md Template
```markdown
# Your Plugin Name

Brief description of what the plugin does.

## Features

- Feature 1
- Feature 2

## Installation

1. Place this folder in: `~/.local/share/kicad/9.0/scripting/plugins/your_plugin_name/`
2. Restart KiCad
3. Open a PCB and find the plugin in the toolbar/menu

## Usage

1. Run the plugin from KiCad
2. Configure options in the dialog
3. Click OK to apply changes

## Debugging

For VS Code debugging:

1. Use Miniconda Python environment
2. Install wxPython: `conda install -c conda-forge wxpython`
3. Set VS Code interpreter to Miniconda Python
4. Run script directly for dialog testing

## Requirements

- KiCad 9.0+
- Python 3.8+
- wxPython (for debugging)

## Troubleshooting

- Plugin not showing: Check folder location and restart KiCad
- Import errors: Ensure KiCad Python environment is set up
- Dialog issues: Test standalone first
```

## Setup Checklist for New Plugins

When starting a new KiCad plugin project:

### 1. Environment Setup
- [ ] KiCad 9.0 installed with Python scripting
- [ ] Miniconda installed for debugging
- [ ] wxPython installed in debug environment
- [ ] VS Code with Python extension

### 2. Project Structure
- [ ] Create plugin folder in KiCad plugins directory
- [ ] Add `__init__.py` (empty)
- [ ] Create main plugin `.py` file
- [ ] Create `README.md`

### 3. Code Template
- [ ] Conditional pcbnew import with mocks
- [ ] Plugin class inheriting from ActionPlugin
- [ ] Dialog class for user input
- [ ] PCB editor window detection
- [ ] Standalone debug mode
- [ ] Proper error handling

### 4. Testing
- [ ] Test dialog standalone
- [ ] Test in KiCad environment
- [ ] Verify no window switching
- [ ] Check all layer options work

### 5. Documentation
- [ ] Installation instructions
- [ ] Usage guide
- [ ] Troubleshooting tips
- [ ] Requirements list

## Best Practices

1. **Always test standalone first** - Use the debug mode to verify dialog logic
2. **Handle imports conditionally** - Support both KiCad and debug environments
3. **Find PCB editor window** - Prevent unwanted window switching
4. **Use board operations safely** - Avoid unsupported APIs like GetCursorPosition
5. **Document everything** - Include setup, usage, and troubleshooting in README
6. **Keep it modular** - Separate dialog, plugin logic, and PCB operations

## Common KiCad API Patterns

```python
# Get board
board = pcbnew.GetBoard()

# Convert mm to internal units
size = pcbnew.FromMM(value_in_mm)

# Create shapes
shape = pcbnew.PCB_SHAPE(board)
shape.SetShape(pcbnew.SHAPE_T_RECT)
shape.SetLayer(layer_constant)
shape.SetStart(pcbnew.VECTOR2I(x1, y1))
shape.SetEnd(pcbnew.VECTOR2I(x2, y2))
board.Add(shape)

# Refresh view
pcbnew.Refresh()
```

## Layer Constants Reference

- F_SilkS, B_SilkS (silk screen)
- F_Cu, B_Cu (copper layers)
- User_1, User_2, ... (user layers)
- Edge_Cuts (board outline)

Use `dir(pcbnew)` to see all available constants in your KiCad version.
```

This template provides a complete starting point for new KiCad plugins. Copy the structure, customize the dialog and PCB operations, and you'll have a working plugin with debugging support.