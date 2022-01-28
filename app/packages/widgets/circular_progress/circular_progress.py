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
# ///////////////////////////////////////////////////////////////

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import enum

class CircularProgress(QWidget):
    def __init__(self, focus_time):
        QWidget.__init__(self)

        # CUSTOM PROPERTIES

        self.width = 500
        self.height = 500
        self.progress_width = 30
        self.progress_rounded_cap = True
        self.max_value = 100
        self.progress_color = 0xffffff
        # Text
        self.enable_text = True
        self.font_family = "Segoe UI"
        self.font_size = 30
        self.suffix = "%"
        self.text_color = 0xffffff
        # BG
        self.enable_bg = False
        self.bg_color = 0x44475a

        # SET DEFAULT SIZE WITHOUT LAYOUT
        self.resize(self.width, self.height)



        #Timer things...
        self.focus_time = focus_time
        minutes = self.focus_time // 60
        seconds = self.focus_time - (minutes * 60)
        self.time_string = "{:02}:{:02}".format(int(minutes), int(seconds))
        self._status = TimerStatus.init
        self._left_seconds = self.focus_time
        self.timer = QTimer()
        self.timer.timeout.connect(self._countdown_and_show)
        self.showTime()


    # ADD DROPSHADOW
    def add_shadow(self, enable):
        if enable:
            self.shadow = QGraphicsDropShadowEffect(self)
            self.shadow.setBlurRadius(15)
            self.shadow.setXOffset(0)
            self.shadow.setYOffset(0)
            self.shadow.setColor(QColor(0, 0, 0, 80))
            self.setGraphicsEffect(self.shadow)

    # SET VALUE
    def set_value(self, value):
        self.value = value
        self.repaint() # Render progress bar after change value


    # PAINT EVENT (DESIGN YOUR CIRCULAR PROGRESS HERE)
    def paintEvent(self, e):
        # SET PROGRESS PARAMETERS
        width = self.width - self.progress_width
        height = self.height - self.progress_width
        margin = self.progress_width / 2
        percentage = self._left_seconds / self.focus_time * 100

        print(self._left_seconds,self.focus_time,percentage)


        value =  percentage* 360 / self.max_value

        # PAINTER
        paint = QPainter()
        paint.begin(self)
        paint.setRenderHint(QPainter.Antialiasing) # remove pixelated edges
        paint.setFont(QFont(self.font_family, self.font_size))

        # CREATE RECTANGLE
        rect = QRect(0, 0, self.width, self.height)
        paint.setPen(Qt.NoPen)
        paint.drawRect(rect)

        # PEN
        pen = QPen()             
        pen.setWidth(self.progress_width)
        # Set Round Cap
        if self.progress_rounded_cap:
            pen.setCapStyle(Qt.RoundCap)

        # ENABLE BG
        if self.enable_bg:
            pen.setColor(QColor(self.bg_color))
            paint.setPen(pen)  
            paint.drawArc(margin, margin, width, height, 0, 360 * 16) 

        # CREATE ARC / CIRCULAR PROGRESS
        pen.setColor(QColor(self.progress_color))
        paint.setPen(pen)      
        paint.drawArc(margin, margin, width, height, -90 * 16, value * 16,)

        # CREATE TEXT
        if self.enable_text:
            pen.setColor(QColor(self.text_color))
            paint.setPen(pen)
            paint.drawText(rect, Qt.AlignCenter, self.time_string)

        # END
        paint.end()

    class TimerStatus(enum.Enum):
        init, counting, paused = 1, 2, 3

    class ButtonText:
        start, pause, reset = "Start", "Pause", "Reset"




    def _start_event(self, value):
        if (self._status == TimerStatus.init or self._status == TimerStatus.paused) and self._left_seconds > 0:
            self._left_seconds -= 1
            self._status = TimerStatus.counting
            self.showTime()
            self.timer.start(1000)
        elif self._status == TimerStatus.counting:
            self.timer.stop()
            self._status = TimerStatus.paused
        self.focus_time = value

    def _reset_event(self):
        self._status = TimerStatus.init
        self._left_seconds = self.focus_time * 60
        self.timer.stop()
        self.showTime()

    def _countdown_and_show(self):
        if self._left_seconds > 0:
            self._left_seconds -= 1
            self.showTime()
        else:
            self.timer.stop()
            self.showTime()
            self._status = TimerStatus.init
            self._left_seconds = self.minutesSpinBox.value() * 60

    def showTime(self):
        total_seconds = min(self._left_seconds, 359940)  # Max time: 99:59:00
        hours = total_seconds // 3600
        total_seconds = total_seconds - (hours * 3600)
        minutes = total_seconds // 60
        seconds = total_seconds - (minutes * 60)
        self.time_string = "{:02}:{:02}".format(int(minutes), int(seconds))
        self.set_value(self.time_string)

    def _edit_event(self, value):
        if self._status == TimerStatus.init:
            self._left_seconds = value * 60
            self.showTime()



class TimerStatus(enum.Enum):
    init, counting, paused = 1, 2, 3

class Timerwidget:
    def _countdown_and_show(self):
        if self._left_seconds > 0:
            self._left_seconds -= 1
            self.showTime()
        else:
            self.timer.stop()
            self.showTime()
            self._status = TimerStatus.init
            self._left_seconds = self.minutesSpinBox.value() * 60

    def _start_event(self):
        if (self._status == TimerStatus.init or self._status == TimerStatus.paused) and self._left_seconds > 0:
            self._left_seconds -= 1
            self._status = TimerStatus.counting
            self.showTime()
            self.timer.start(1000)
        elif self._status == TimerStatus.counting:
            self.timer.stop()
            self._status = TimerStatus.paused

    def _reset_event(self):
        self._status = TimerStatus.init
        self._left_seconds = self.minutesSpinBox.value() * 60
        self.timer.stop()
        self.showTime()

    def _edit_event(self):
        if self._status == TimerStatus.init:
            self._left_seconds = self.minutesSpinBox.value() * 60
            self.showTime()

    def showTime(self):
        total_seconds = min(self._left_seconds, 359940)  # Max time: 99:59:00
        hours = total_seconds // 3600
        total_seconds = total_seconds - (hours * 3600)
        minutes = total_seconds // 60
        seconds = total_seconds - (minutes * 60)
        self.displayArea.setText("{:02}:{:02}:{:02}".format(int(hours), int(minutes), int(seconds)))
        self.displayArea.setAlignment(Qt.AlignHCenter)

    def setWidgets(self):
        hbox = QHBoxLayout()
        hbox.addWidget(self.minutesLabel)
        hbox.addWidget(self.minutesSpinBox)
        hbox.addWidget(self.startButton)
        hbox.addWidget(self.resetButton)
        hbox.setAlignment(Qt.AlignLeft)
        vbox = QVBoxLayout()
        vbox.addLayout(hbox)
        vbox.addWidget(self.displayArea)
        self.setLayout(vbox)

if __name__ == "__main__":
    progress = CircularProgress()
    progress.__init__()