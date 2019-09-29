import typing

from PyQt5.QtWidgets import QMenuBar, QWidget, QAction, QMenu


class MainMenuBar(QMenuBar):
    def __init__(
        self,
        actions: typing.Dict[str, typing.Dict[str, QAction]],
        parent: typing.Optional[QWidget] = None,
    ):
        super().__init__(parent)
        self.menus = self._create_menus(actions)

    def _create_menus(self, actions) -> typing.Dict[str, QMenu]:
        """ Create menus in menu bar """

        menus = {
            "file": self.addMenu("&File"),
            "edit": self.addMenu("&Edit"),
            "insert": self.addMenu("&Insert"),
            "view": self.addMenu("&View"),
            "help": self.addMenu("&Help"),
        }

        return self._populate_menus(menus, actions)

    @staticmethod
    def _populate_menus(
        menus: typing.Dict[str, QMenu], actions
    ) -> typing.Dict[str, QMenu]:
        """ Add actions to menus in the menu bar """

        file_menu, file_actions = menus["file"], actions["file"]
        file_menu.addActions(
            (file_actions[action] for action in ("new", "open", "save", "save_as"))
        )
        file_menu.addSeparator()
        file_menu.addAction(file_actions["quit"])

        edit_menu, edit_actions = menus["edit"], actions["edit"]
        edit_menu.addActions((edit_actions[action] for action in ("undo", "redo")))
        edit_menu.addSeparator()
        edit_menu.addActions(
            (edit_actions[action] for action in ("cut", "copy", "paste", "duplicate"))
        )

        help_menu, help_actions = menus["help"], actions["help"]
        help_menu.addActions((help_actions[action] for action in ("about", "about_qt")))

        return menus
