from . whie_button import WhiteButton
from app.packages.pyside_or_pyqt import *

class PomoButton(WhiteButton):
    def __init__(self, parent, name, icon, width, height, active_im):
        WhiteButton.__init__(self, parent, name, icon, width, height)
        self.isactive = False
        self.active_im = active_im

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            # EMIT SIGNAL
            self.clicked.emit()
            # SET FOCUS
            self.setFocus()
            self.isactive = False if self.isactive else True
            self.repaint()


    def icon_paint(self, qp, image, rect):
        #if button active => active image
        image = self.active_im if self.isactive else image
        icon = QPixmap(image)
        painter = QPainter(icon)
        painter.setCompositionMode(QPainter.CompositionMode_SourceIn)
        painter.fillRect(icon.rect(), self._set_icon_color)
        qp.drawPixmap(
            (rect.width() - icon.width()) / 2,
            (rect.height() - icon.height()) / 2,
            icon
        )
        painter.end()

