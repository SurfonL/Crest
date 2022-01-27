# ///////////////////////////////////////////////////////////////
#
# BY: WANDERSON M.PIMENTA
# PROJECT MADE WITH: Qt Designer and PySide6
# V: 1.0.0
#
# This project can be used freely for all uses, as long as they maintain the
# respective credits only in the Python scripts, any information in the visual
# interface (GUI) can be modified without any implication.
#
# There are limitations on Qt licenses if you want to use your products
# commercially, I recommend reading them on the official website:
# https://doc.qt.io/qtforpython/licenses.html
#
# ///////////////////////////////////////////////////////////////

# IMPORT
# ///////////////////////////////////////////////////////////////
# Packages
from app.packages.pyside_or_pyqt import *
# Modules
import app.modules.ui_functions.functions as ui_functions
from app.modules.app_settings.settings import *
import os

# TOOLTIP / LABEL StyleSheet
style_tooltip = """ 
QLabel {		
	background-color: #0b0b0c;	
	color: rgb(230, 230, 230);
	padding-left: 10px;
	padding-right: 10px;
	border-radius: 17px;
    border: 1px solid #2f3032;
    border-left: 3px solid #bdff00;
    font: 800 9pt "Segoe UI";
}
"""

# CUSTOM LEFT MENU
class WhiteButton(QWidget):
    # SIGNALS
    clicked = Signal()
    released = Signal()

    def __init__(self, parent, name, icon, width, height):
        QWidget.__init__(self)
        # APP PATH
        app_path = os.path.abspath(os.getcwd())
        icon_path = os.path.join(app_path, icon)

        # GET SETTINGS
        settings = Settings()
        self.settings = settings.items

        # DEFAULT PARAMETERS
        self.width = width
        self.height = height
        self.pos_x = 0
        self.pos_y = 0
        self.border_radius = 10
        self.parent = parent
        self.setGeometry(0, 0, self.width, self.height)
        self.setMinimumSize(self.width, self.height)
        self.setCursor(Qt.PointingHandCursor)
        self.setObjectName(name)

        # BG COLORS
        self.color_default = QColor(self.settings["left_menu"]["color"])
        self.color_hover = QColor(self.settings["left_menu"]["color_hover"])
        self.color_pressed = QColor(self.settings["left_menu"]["color_pressed"])
        self._set_color = self.color_default

        # ICON
        self.icon_color = QColor(0xE6E6E6)
        self.icon_color_pressed = QColor(0x151617)
        self._set_icon_path = icon_path        
        self._set_icon_color = self.icon_color

        # Custom
        self.isactive = False


    # PAINT EVENT
    # Responsible for painting the button, as well as the icon
    def paintEvent(self, event):
        # PAINTER
        paint = QPainter()
        paint.begin(self)
        paint.setRenderHint(QPainter.RenderHint.Antialiasing)

        # CREATE RECTANGLE
        rect = QRect(0, 0, self.width, self.height)

        # DRAW ICONS
        self.icon_paint(paint, self._set_icon_path, rect)

        # END PAINTER
        paint.end()

    # DRAW ICON WITH COLORS
    def icon_paint(self, qp, image, rect):
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

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            # EMIT SIGNAL
            self.clicked.emit()
            # SET FOCUS
            self.setFocus()





