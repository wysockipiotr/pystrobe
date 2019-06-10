from PyQt5.QtGui import (
    QPen,
    QBrush,
    QColor,
    QWheelEvent,
    QPainter,
)
from PyQt5.QtWidgets import (
    QGraphicsView,
    QWidget,
)
from PyQt5.QtCore import Qt

from PyQt5.QtCore import (
    pyqtBoundSignal,
    pyqtSlot as slot,
)
from PyQt5.QtCore import QTimeLine

from core import (
    Scene,
    ComponentView,
)


class Qwerty(QGraphicsView):
    ...


class ZoomGraphicsView(QGraphicsView):
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)

        self.setDragMode(QGraphicsView.RubberBandDrag)
        self.setRenderHints(QPainter.Antialiasing | QPainter.TextAntialiasing)
        self.setTransformationAnchor(QGraphicsView.AnchorUnderMouse)
        # self.setCacheMode(QGraphicsView.CacheBackground)
        self.setViewportUpdateMode(QGraphicsView.FullViewportUpdate)

        self.setScene(Scene())

        for _ in range(4):
            self.scene().addItem(ComponentView())

        self.num_scheduled_steps = 0

    def wheelEvent(self, event: QWheelEvent) -> None:
        if event.modifiers() & Qt.ControlModifier:
            num_degrees = event.angleDelta().y() / 8.0
            num_steps = num_degrees / 15.0

            self.num_scheduled_steps += num_steps

            if self.num_scheduled_steps * num_steps < 0:
                self.num_scheduled_steps = num_steps

            animation = QTimeLine(duration=350, parent=self)
            animation.setUpdateInterval(20)

            value_changed_sig: pyqtBoundSignal = animation.valueChanged
            value_changed_sig.connect(self.scaling_step)

            finished_sig: pyqtBoundSignal = animation.finished
            finished_sig.connect(self.animation_finished)

            animation.start()
        else:
            super().wheelEvent(event)

    @slot(float, name='scaling_step')
    def scaling_step(self):
        factor = 1.0 + self.num_scheduled_steps / 300.0
        self.scale(factor, factor)

    @slot(name='animation_finished')
    def animation_finished(self):
        if self.num_scheduled_steps > 0:
            self.num_scheduled_steps -= 1
        else:
            self.num_scheduled_steps += 1
