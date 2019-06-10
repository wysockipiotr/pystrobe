from dataclasses import dataclass

from PyQt5.QtWidgets import QAction


class GetAllActionsMixin:
    def all(self):
        return [
            getattr(self, action_name)
            for action_name in self.__dir__()
            if isinstance(getattr(self, action_name), QAction)
        ]


@dataclass()
class Actions:
    @dataclass()
    class File(GetAllActionsMixin):
        new: QAction
        open: QAction
        save: QAction
        save_as: QAction
        exit: QAction

    @dataclass()
    class Edit(GetAllActionsMixin):
        undo: QAction
        redo: QAction
        cut: QAction
        copy: QAction
        duplicate: QAction
        paste: QAction

    @dataclass()
    class Insert(GetAllActionsMixin):
        wire: QAction
        input: QAction
        output: QAction
        clock: QAction

    @dataclass()
    class View(GetAllActionsMixin):
        ...

    @dataclass()
    class Help(GetAllActionsMixin):
        ...

    file: File
    edit: Edit
    # insert: Insert
    # view: View
    # help: Help
