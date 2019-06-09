from PyQt5.QtWidgets import (
    QAction,
)


class ActionBuilder:
    def __init__(self, parent=None) -> None:
        self._parent = parent

    def __enter__(self):
        return self

    def __exit__(self, *args):
        ...

    def build(self,
              text: str,
              shortcut: str = None,
              status_tip: str = None,
              icon: str = None) -> QAction:
        action = QAction(text=text, parent=self._parent)
        action.setText(text)
        if shortcut:
            action.setShortcut(shortcut)
        if icon:
            action.setIcon(icon)
        action.setStatusTip(status_tip if status_tip else text)
        return action
