import typing

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QWidget, QAction, QMessageBox, QApplication
from PyQt5.QtCore import pyqtSlot as slot

from ui.main_window.actions import make_actions
from ui.main_window.menu_bar import MainMenuBar
from ui.zoom_graphics_view import ZoomGraphicsView


class Defaults:
    WINDOW_TITLE = "strobe"
    WINDOW_SIZE = (800, 500)
    WINDOW_POSITION = (300, 300)


class MainWindow(QMainWindow):
    """ Main window of the application """

    def __init__(self, parent: QWidget = None):
        super().__init__(parent)

        self._actions: typing.Dict[str, typing.Dict[str, QAction]] = make_actions(
            parent=self
        )
        self.setMenuBar(MainMenuBar(self._actions, self))

        self._graphics_view = ZoomGraphicsView(parent=self)
        self.setCentralWidget(self._graphics_view)
        self.setWindowIcon(QIcon("assets/icon.ico"))
        self.setWindowTitle(Defaults.WINDOW_TITLE)
        self._status_bar = self.statusBar()
        self.resize(*Defaults.WINDOW_SIZE)
        self.move(*Defaults.WINDOW_POSITION)

        self._connect_signals()

    def _connect_signals(self) -> None:
        self._actions["help"]["about"].triggered.connect(self._about)
        self._actions["help"]["about_qt"].triggered.connect(self._about_qt)
        self._actions["file"]["quit"].triggered.connect(self._quit)

    @slot()
    def _about(self):
        QMessageBox.about(
            self,
            " About strobe",
            """
            <b>strobe</b><br />
            <em>Digital circuits simulator</em><br /><br />
            <a href="https://github.com/wysockipiotr/pystrobe">GitHub repo</a><br />
            Piotr Wysocki (<a href="https://github.com/wysockipiotr">wysockipiotr</a>)
            """,
        )

    @slot()
    def _about_qt(self):
        QMessageBox.aboutQt(self)

    @slot()
    def _quit(self):
        QApplication.quit()
