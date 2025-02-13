from PySide6 import QtCore, QtGui, QtWidgets


class PushButton(QtWidgets.QPushButton):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._animation = QtCore.QVariantAnimation(
            startValue=QtGui.QColor("#4CAF50"),
            endValue=QtGui.QColor("white"),
            duration=400,
        )
        self._update_stylesheet(QtGui.QColor("white"), QtGui.QColor("black"))

        self._animation.valueChanged.connect(self._on_value_changed)

    def _on_value_changed(self, color):
        foreground = (
            QtGui.QColor("black")
            if self._animation.direction() == QtCore.QAbstractAnimation.Forward
            else QtGui.QColor("white")
        )
        print(color)
        self._update_stylesheet(color, foreground)

    def _update_stylesheet(self, background, foreground):

        self.setStyleSheet(
            """
        QPushButton{
            background-color: %s;
            border: none;
            color: %s;
            padding: 16px 32px;
            text-align: center;
            text-decoration: none;
            font-size: 16px;
            margin: 4px 2px;
            border: 2px solid #4CAF50;
        }
        """
            % (background.name(), foreground.name())
        )

    def enterEvent(self, event):
        self._animation.setDirection(QtCore.QAbstractAnimation.Backward)
        self._animation.start()
        super().enterEvent(event)

    def leaveEvent(self, event):
        self._animation.setDirection(QtCore.QAbstractAnimation.Forward)
        self._animation.start()
        super().leaveEvent(event)


class Dialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle(self.tr("Dialog"))

        self.pushButton = PushButton()
        self.pushButton.setText(self.tr("Click Here"))
        self.pushButton.setSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum
        )

        lay = QtWidgets.QVBoxLayout(self)
        lay.addWidget(self.pushButton)

        self.resize(400, 300)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    w = Dialog()
    w.show()
    sys.exit(app.exec_())