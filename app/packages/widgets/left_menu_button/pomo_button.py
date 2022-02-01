from . whie_button import WhiteButton
from app.packages.pyside_or_pyqt import *

class PomoButton(WhiteButton):
    def __init__(self, parent, name, icon, width, height):
        WhiteButton.__init__(self, parent, name, icon, width, height)


        self.is_original = True
        self.icon_original = icon
        self.icon_stop = "images/icons_svg/stop.png"


    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            # EMIT SIGNAL
            self.clicked.emit()
            # SET FOCUS
            self.setFocus()
            self.repaint()


    def icon_paint(self, qp, image, rect):
        #if button active => active image
        image = self.icon_original if self.is_original else self.icon_stop
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

    def stop_icon(self):
        self.is_original = False

    def original_icon(self):
        self.is_original = True
        self.repaint()





