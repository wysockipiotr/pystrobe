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
        new_file: QAction
        exit_app: QAction

    @dataclass()
    class Edit(GetAllActionsMixin):
        undo: QAction
        redo: QAction

    @dataclass()
    class Insert(GetAllActionsMixin):
        ...

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
