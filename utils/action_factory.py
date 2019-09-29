import typing

from PyQt5.QtCore import QObject
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QAction


def make_action_factory(parent: typing.Optional[QObject]):
    def make_action(
        text: str,
        shortcut: typing.Optional[str] = None,
        status_tip: typing.Optional[str] = None,
        icon: typing.Optional[QIcon] = None,
    ) -> QAction:
        action = QAction(text, parent)
        if shortcut:
            action.setShortcut(shortcut)
        if icon:
            action.setIcon(icon)
        action.setStatusTip(status_tip or text)
        return action

    return make_action
