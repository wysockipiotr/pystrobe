from dataclasses import dataclass

from PyQt5.QtWidgets import QMenu


@dataclass()
class Menus:
    file: QMenu
    edit: QMenu
    insert: QMenu
    view: QMenu
    help: QMenu
