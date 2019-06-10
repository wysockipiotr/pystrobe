from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (
    QMainWindow,
    QWidget,
)

from ui.zoom_graphics_view import ZoomGraphicsView
from utils import ActionBuilder

from .actions import Actions
from .menus import Menus


class Defaults:
    WINDOW_TITLE = 'strobe'
    WINDOW_SIZE = (800, 500)
    WINDOW_POSITION = (300, 300)


class MainWindow(QMainWindow):
    """ Main window of the application """

    def __init__(self, parent: QWidget = None):
        super().__init__(parent)

        self.setWindowIcon(QIcon('assets/icon.ico'))

        self._menus: Menus = self._create_menus()
        self._actions: Actions = self._create_actions()

        self._graphics_view = ZoomGraphicsView(parent=self)
        self.setCentralWidget(self._graphics_view)

        self._populate_menus(self._actions)

        self.setWindowTitle(Defaults.WINDOW_TITLE)

        self._status_bar = self.statusBar()
        self.resize(*Defaults.WINDOW_SIZE)
        self.move(*Defaults.WINDOW_POSITION)

    def _create_menus(self) -> Menus:
        """ Create menus in menu bar """

        menu_bar = self.menuBar()
        return Menus(
            file=menu_bar.addMenu('&File'),
            edit=menu_bar.addMenu('&Edit'),
            insert=menu_bar.addMenu('&Insert'),
            view=menu_bar.addMenu('&View'),
            help=menu_bar.addMenu('&Help'),
        )

    def _create_actions(self) -> Actions:
        """ Create main app actions """

        with ActionBuilder(parent=self) as action:
            actions = Actions(
                file=Actions.File(
                    new=action.build(text='New file', shortcut='Ctrl+N'),
                    open=action.build(text='Open file', shortcut='Ctrl+O'),
                    save=action.build(text='Save', shortcut='Ctrl+S'),
                    save_as=action.build(text='Save as...', shortcut='Ctrl+Shift+S'),
                    exit=action.build(text='Quit', shortcut='Ctrl+Q')
                ),
                edit=Actions.Edit(
                    undo=action.build(text='Undo', shortcut='Ctrl+Z'),
                    redo=action.build(text='Redo', shortcut='Ctrl+Shift+Z'),
                    cut=action.build(text='Cut', shortcut='Ctrl+X'),
                    copy=action.build(text='Copy', shortcut='Ctrl+C'),
                    paste=action.build(text='Paste', shortcut='Ctrl+V'),
                    duplicate=action.build(text='Duplicate', shortcut='Ctrl+D'),
                )
            )
            return actions

    def _populate_menus(self, actions: Actions) -> None:
        """ Add actions to menus in the menu bar """

        # file
        file_menu = self._menus.file
        file_actions = actions.file
        file_menu.addActions((
            file_actions.new,
            file_actions.open,
            file_actions.save,
            file_actions.save_as,
        ))
        file_menu.addSeparator()
        file_menu.addAction(file_actions.exit)

        # edit
        edit_menu = self._menus.edit
        edit_actions = actions.edit
        edit_menu.addActions((
            edit_actions.undo,
            edit_actions.redo,
        ))
        edit_menu.addSeparator()
        edit_menu.addActions((
            edit_actions.cut,
            edit_actions.copy,
            edit_actions.paste,
            edit_actions.duplicate,
        ))


        # obj = QObject()
        # obj.installEventFilter()
# def from_event(qobject: QObject, type_: QEvent.Type) -> Observable[QEvent]:
#     if not qobject:
#         return never()
#
#     def subscribe(observer: Observer) -> Disposable:
#         qobject.installEventFilter()
#         return Disposable(lambda: observer.on_completed())
#
#     return Observable(subscribe)
