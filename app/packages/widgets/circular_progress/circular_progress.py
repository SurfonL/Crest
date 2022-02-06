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
    def __init__(self, page):
        QWidget.__init__(self)

        self.page = page

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
        self.font_size = 40
        self.suffix = "%"
        self.text_color = 0xffffff
        # BG
        self.enable_bg = False
        self.bg_color = 0x44475a

        # SET DEFAULT SIZE WITHOUT LAYOUT
        self.resize(self.width, self.height)



        #Timer things...
        self.init_seconds = int(self.page.ui.focus_edit.text()) * 60
        self.focus_seconds = int(self.page.ui.focus_edit.text()) * 60
        self.rest_seconds = int(self.page.ui.rest_edit.text()) * 60
        minutes = self.init_seconds // 60
        seconds = self.init_seconds - (minutes * 60)
        self.time_string = "{:02}:{:02}".format(int(minutes), int(seconds))
        self._status = TimerStatus.init
        self._left_seconds = self.init_seconds
        self.timer = QTimer()
        self.timer.timeout.connect(self._countdown_and_show)
        self.showTime()

        self.focus_status = FocusStatus.focus


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
        percentage = self._left_seconds / self.init_seconds * 100 - 100

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
        paint.drawArc(margin, margin, width, height, 90*16, value * 16,)
        #

        # CREATE TEXT
        if self.enable_text:
            pen.setColor(QColor(self.text_color))
            paint.setPen(pen)
            paint.drawText(rect, Qt.AlignCenter, self.time_string)

        # END
        paint.end()

    def _start_event(self):
        if (self._status == TimerStatus.init or self._status == TimerStatus.paused):
            self._left_seconds -= 1
            self._status = TimerStatus.counting
            self.showTime()
            self.timer.start(1000)


    #called when paus/stop button is pressed
    def _reset_event(self):
        if self._status == TimerStatus.counting:
            self._status = TimerStatus.paused

        #Timer is "Stopped"
        elif self._status == TimerStatus.paused and self.focus_status == FocusStatus.focus:
            self.rest_init()
            self._left_seconds = self.init_seconds
            self._status = TimerStatus.init
            self.showTime()

        elif self._status == TimerStatus.paused and self.focus_status == FocusStatus.rest:
            self.focus_init()
            self._left_seconds = self.init_seconds
            self._status = TimerStatus.init
            self.showTime()

        self.timer.stop()


    def _countdown_and_show(self):
        self._left_seconds -= 1
        self.showTime()
        if self._left_seconds < 0:
            self.page.ui.pomodoro_appPage2.setStyleSheet(u"background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
                                                 "stop:0 rgba(254,88,88,1), stop: 1 rgba(238,150,23,1))\n"
                                                 "")
            self.on_top_event()


    def showTime(self):
        if self._left_seconds >= 0:
            minutes = self._left_seconds // 60
            seconds = self._left_seconds - (minutes * 60)
            self.time_string = "{:02}:{:02}".format(int(minutes), int(seconds))
        else:
            minutes = abs(self._left_seconds) // 60
            seconds = abs(self._left_seconds) - (minutes * 60)
            self.time_string = "-{:02}:{:02}".format(int(minutes), int(seconds))

        self.set_value(self.time_string)


    def focus_edit_event(self, value):
        self.focus_seconds = value * 60
        if self.focus_status == FocusStatus.focus:
            if self._status == TimerStatus.counting:
                self.init_seconds = self.focus_seconds
            else:
                self.init_seconds = self.focus_seconds
                self._left_seconds = self.focus_seconds
                self.showTime()



    def rest_edit_event(self,value):
        self.rest_seconds = value * 60
        if self.focus_status == FocusStatus.rest:
            if self._status == TimerStatus.counting:
                self.init_seconds = self.rest_seconds
            else:
                self.init_seconds = self.rest_seconds
                self._left_seconds = self.rest_seconds
                self.showTime()


    def rest_init(self):
        self.focus_status = FocusStatus.rest
        self.init_seconds = self.rest_seconds
        self.page.ui.pomodoro_appPage2.setStyleSheet(u"background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
                                                  "stop:0 rgba(8, 126, 225,1), stop: 1 rgba(5, 232, 186,1))\n"
                                                  "")

    def focus_init(self):
        self.focus_status = FocusStatus.focus
        self.init_seconds = self.focus_seconds
        self.page.ui.pomodoro_appPage2.setStyleSheet(u"background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
                                             "stop:0 rgba(152, 222, 91,1), stop: 1 rgba(8, 225, 174,1))\n"
                                             "")


    def on_top_event(self):
        if not self.page.isActiveWindow():
            self.page.pomodoro_button.clicked.connect(lambda: self.page.ui.bg_app.setCurrentWidget(self.page.ui.pomodoro_appPage2))
            self.page.maximize_minimize()
            self.page.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
            self.page.show()
            self.page.setWindowFlags(Qt.FramelessWindowHint)
            self.page.show()

            self.page.setWindowState(self.page.windowState() & ~Qt.WindowMinimized | Qt.WindowActive)
            # self.page.activateWindow()
            # self.page.setFocus()








class TimerStatus:
    init, counting, paused = 1, 2, 3

class FocusStatus:
    focus, rest = 1, 2

if __name__ == "__main__":
    progress = CircularProgress()
    progress.__init__()