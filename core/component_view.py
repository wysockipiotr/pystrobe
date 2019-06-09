from typing import (
    Optional,
)
from PyQt5.QtWidgets import (
    QGraphicsItem,
    QStyleOptionGraphicsItem,
    QWidget,
)
from PyQt5.QtCore import (
    QRectF,
    Qt,
)
from PyQt5.QtGui import (
    QPainter,
    QBrush,
    QPen,
    QColor,
    QFont,
    QPainterPath,
)


class Defaults:
    OUTLINE_WIDTH = 2.0
    OUTLINE_COLOR = Qt.black
    BACKGROUND_COLOR = Qt.white
    HIGHLIGHT_COLOR = QColor(105, 186, 201)

    RECT_WIDTH = 100

    FONT_FACE = 'Roboto Mono'
    FONT_SIZE_LG = 24
    FONT_SIZE_MD = 14
    FONT_SIZE_SM = 8
    TOP_TEXT_BOUNDING_RECT = QRectF(0, -25, RECT_WIDTH, 25)

    LEVEL_OF_DETAIL_THRESHOLDS = (
        0.35,
        0.5,
    )

    RECT = QRectF(0, 0, RECT_WIDTH, RECT_WIDTH)

    BOUNDING_RECT = QRectF(
        -OUTLINE_WIDTH / 2,
        TOP_TEXT_BOUNDING_RECT.top(),
        RECT_WIDTH + OUTLINE_WIDTH,
        OUTLINE_WIDTH / 2 + RECT_WIDTH
    )
    COLLISION_SHAPE = QRectF(
        -OUTLINE_WIDTH / 2,
        -OUTLINE_WIDTH / 2,
        RECT_WIDTH + OUTLINE_WIDTH,
        RECT_WIDTH + OUTLINE_WIDTH
    )
    PEN = QPen(
        OUTLINE_COLOR,
        OUTLINE_WIDTH,
        style=Qt.SolidLine,
        cap=Qt.SquareCap,
        join=Qt.MiterJoin
    )
    PEN_SELECTED = QPen(
        HIGHLIGHT_COLOR,
        OUTLINE_WIDTH,
        style=Qt.SolidLine,
        cap=Qt.SquareCap,
        join=Qt.MiterJoin
    )
    BRUSH = QBrush(BACKGROUND_COLOR)

    @staticmethod
    def get_font(size: int) -> QFont:
        return QFont(Defaults.FONT_FACE, size)


class ComponentView(QGraphicsItem):
    """
    Graphics item associated with the displayed component
    """

    def __init__(self, parent: QGraphicsItem = None):
        super().__init__(parent)

        self.setFlag(QGraphicsItem.ItemIsMovable)
        self.setFlag(QGraphicsItem.ItemIsSelectable)

    def boundingRect(self) -> QRectF:
        """
        Rectangular bounding area that needs updates (repaints)

        Returns:
            Bounding rectangle
        """
        return Defaults.BOUNDING_RECT

    def shape(self) -> QPainterPath:
        """
        Component's shape, used for collision detection (e.g. selecting, moving)

        Returns:
            Collision rectangle
        """
        path = QPainterPath()
        path.addRect(Defaults.COLLISION_SHAPE)
        return path

    def paint(self,
              painter: QPainter,
              option: QStyleOptionGraphicsItem,
              widget: Optional[QWidget] = ...) -> None:
        """
        Paint component

        Returns:
            None
        """
        level_of_detail = option.levelOfDetailFromTransform(
            painter.worldTransform()
        )

        self._paint_rect(painter)
        self._paint_text(level_of_detail, painter)

        self.scene().update()

    def _paint_text(self, level_of_detail: float, painter: QPainter) -> None:
        """
        Paint component's text labels

        Args:
            level_of_detail: Level of detail from painter's world transform
            painter: QPainter

        Returns:
            None
        """
        painter.setPen(self._highlightable_pen)
        painter.setFont(Defaults.get_font(
            Defaults.FONT_SIZE_MD
            if level_of_detail > Defaults.LEVEL_OF_DETAIL_THRESHOLDS[0]
            else Defaults.FONT_SIZE_LG
        ))
        painter.drawText(
            Defaults.RECT,
            Qt.AlignCenter,
            'XNOR'
        )

        if level_of_detail > Defaults.LEVEL_OF_DETAIL_THRESHOLDS[1]:
            painter.setFont(Defaults.get_font(
                Defaults.FONT_SIZE_SM
            ))
            painter.drawText(
                Defaults.TOP_TEXT_BOUNDING_RECT,
                Qt.AlignCenter, 'GATE #1'
            )

    def _paint_rect(self, painter: QPainter):
        """
        Paint component's box rectangle

        Args:
            painter: QPainter

        Returns:
            None
        """
        painter.setBrush(Defaults.BRUSH)
        painter.setPen(self._highlightable_pen)
        painter.drawRect(Defaults.RECT)

    @property
    def _highlightable_pen(self) -> QPen:
        """
        Pen for the current state of component selection

        Returns:
            Active pen
        """
        return (
            Defaults.PEN_SELECTED
            if self.isSelected()
            else Defaults.PEN
        )