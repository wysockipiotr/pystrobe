from dataclasses import dataclass

from PyQt5.QtWidgets import QAction


@dataclass()
class Actions:
    @dataclass()
    class File:
        new_file: QAction
        exit_app: QAction

    @dataclass()
    class Edit:
        undo: QAction
        redo: QAction

    @dataclass()
    class Insert:
        ...

    @dataclass()
    class View:
        ...

    @dataclass()
    class Help:
        ...

    file: File
    # edit: Edit
    # insert: Insert
    # view: View
    # help: Help
