from PyQt5.QtCore import QObject, QPointF
from PyQt5.QtGui import QPen
from PyQt5.QtWidgets import QGraphicsScene, QStyleOptionGraphicsItem
from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5.QtCore import Qt

LEVEL_OF_DETAIL_THRESHOLD = 0.35
GRID_SIZE = 25


class Scene(QGraphicsScene):
    def __init__(self, parent: QObject = None):
        super().__init__(parent)

    def drawBackground(self, painter: QtGui.QPainter, rect: QtCore.QRectF) -> None:
        """ Draw dotted grid in the background """

        level_of_detail = QStyleOptionGraphicsItem.levelOfDetailFromTransform(
            painter.worldTransform()
        )

        if level_of_detail > LEVEL_OF_DETAIL_THRESHOLD:
            pen = QPen(Qt.black, 3.0)
            pen.setCosmetic(True)
            painter.setPen(pen)

            left = int(rect.left()) - int(rect.left()) % GRID_SIZE
            top = int(rect.top()) - int(rect.top()) % GRID_SIZE

            x = left
            y = top

            while x < rect.right():
                while y < rect.bottom():
                    painter.drawPoint(QPointF(x, y))
                    y += GRID_SIZE
                y = top
                x += GRID_SIZE
