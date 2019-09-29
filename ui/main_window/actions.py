from utils.action_factory import make_action_factory


def make_actions(parent):
    action = make_action_factory(parent)
    return {
        "file": {
            "new": action(text="New file", shortcut="Ctrl+N"),
            "open": action(text="Open file", shortcut="Ctrl+O"),
            "save": action(text="Save", shortcut="Ctrl+S"),
            "save_as": action(text="Save as...", shortcut="Ctrl+Shift+S"),
            "quit": action(text="Quit", shortcut="Ctrl+Q"),
        },
        "edit": {
            "undo": action(text="Undo", shortcut="Ctrl+Z"),
            "redo": action(text="Redo", shortcut="Ctrl+Shift+Z"),
            "cut": action(text="Cut", shortcut="Ctrl+X"),
            "copy": action(text="Copy", shortcut="Ctrl+C"),
            "paste": action(text="Paste", shortcut="Ctrl+V"),
            "duplicate": action(text="Duplicate", shortcut="Ctrl+D"),
        },
        "help": {"about": action(text="About strobe"), "about_qt": action(text="Qt")},
    }
