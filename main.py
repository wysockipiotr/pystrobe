import sys
import os

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt

from ui import MainWindow


if __name__ == "__main__":
    # windows task bar icon fix
    if os.name == "nt":
        import ctypes

        app_id = "wysockipiotr.strobe"
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(app_id)

    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps, True)

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
