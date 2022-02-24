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
from . Record import Record


pause_limit = 5 * 60
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
        self._status_b = TimerStatus.init
        self._left_seconds = self.init_seconds
        self.timer = QTimer()
        self.timer.timeout.connect(self._countdown_and_show)

        self.pause_timer = QTimer()
        self.pause_timer.timeout.connect(self.count_pause_time)
        self.pause_time = 0
        self.pt = False
        self.showTime()

        self.focus_status = FocusStatus.focus

        #Record Things
        self.pomo_record = Record()

        ('#98de5b', '#08e1ae')

        #animation test
        self.c_start_1 = '#98de5b'
        self.c_end_1= '#98de5b'
        self.c_start_2 = '#08e1ae'
        self.c_end_2 = '#08e1ae'
        self._animation_1 = QVariantAnimation(
            startValue=QColor(self.c_end_1),
            endValue=QColor(self.c_start_1),
            duration=400,
        )
        self._animation_2 = QVariantAnimation(
            startValue=QColor(self.c_end_2),
            endValue=QColor(self.c_start_2),
            duration=400,
        )
        self._animation_1.valueChanged.connect(self._set_temp_c)
        self._animation_2.valueChanged.connect(self.set_background)




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
        percentage = self._left_seconds / self.init_seconds * 100 - 100 if self.init_seconds != 0 else 0

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
        self._status_b = self._status
        self._status = TimerStatus.counting
        self._left_seconds -= 1
        self.showTime()
        self.timer.start(1000)

        # init 이면 time stamp start
        if self._status_b == TimerStatus.init:
            self.start_record()

        # paused 면 time stamp X
        elif self._status_b == TimerStatus.paused:
            self.pause_timer.stop()
            self.pause_time = 0




    #called when paus/stop button is pressed
    def _reset_event(self):
        self.timer.stop()
        if self._status == TimerStatus.counting:
            self._status_b = self._status
            self._status = TimerStatus.paused

            self.pause_time = 0
            self.pause_timer.start(1000)

        elif self._status == TimerStatus.paused:
            self.pause_timer.stop()
            self.pause_time = 0

            self._status_b = self._status
            self._status = TimerStatus.init
            #status를 focus->rest, rest->focus로 바꿈
            self.focus_status = FocusStatus.rest if self.focus_status == FocusStatus.focus else FocusStatus.focus

            #status가 init일 때 실행.
            if self.focus_status == FocusStatus.rest:
                self._rest_init()
            elif self.focus_status == FocusStatus.focus:
                self._focus_init()

            sb = pause_limit if self.pt else 0
            self.pomo_record.end_record(subtract_sec=sb)

    def _countdown_and_show(self):
        self._left_seconds -= 1
        self.showTime()
        if self._left_seconds < 0:
            if self._left_seconds == -1:
                self._bg_transition_setter('#fe5858', '#ee9617')
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

    def _focus_init(self):
        self.init_seconds = self.focus_seconds
        self._bg_transition_setter('#98de5b', '#08e1ae')
        self._left_seconds = self.init_seconds
        self.showTime()

    def _rest_init(self):
        self.init_seconds = self.rest_seconds
        self._left_seconds = self.init_seconds
        self._bg_transition_setter('#087ee1', '#05e8ba')
        self.showTime()


    def on_top_event(self):
        if not self.page.isActiveWindow():
            self.page.pomodoro_button.clicked.connect(lambda: self.page.ui.bg_app.setCurrentWidget(self.page.ui.pomodoro_appPage2))

            # self.page.maximize_minimize()
            self.page.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
            self.page.show()
            self.page.setWindowFlags(Qt.FramelessWindowHint)
            self.page.show()

            self.page.setWindowState(self.page.windowState() & ~Qt.WindowMinimized | Qt.WindowActive)
            # self.page.activateWindow()
            # self.page.setFocus()

    def start_record(self):
        self.pomo_record.start_record(self.focus_status)

    def count_pause_time(self):
        self.pause_time += 1
        print(self.pause_time)

        if self.pause_time == pause_limit:
            self.pause_timer.stop()
            self.pt=True

            self.pomo_record.end_record(self.pause_time)
            self._focus_init()
            self._status = TimerStatus.init
            self.page.hide_show()

            self.page.hide_show()
            self.pt = False

    def _bg_transition_setter(self, end1, end2):
        self._animation_1.setStartValue(QColor(self.c_start_1))
        self._animation_2.setStartValue(QColor(self.c_start_2))

        self._animation_1.setEndValue(QColor(end1))
        self._animation_2.setEndValue(QColor(end2))

        self._animation_1.start()
        self._animation_2.start()

        self.c_start_1 = end1
        self.c_start_2 = end2
    def _set_temp_c(self,color):
        self._temp_c = color.name()
    def set_background(self, color):
        self.page.ui.pomodoro_appPage2.setStyleSheet(u"background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
                                                     "stop:0 %s, stop: 1 %s)\n" % (self._temp_c, color.name())
                                                     )



class TimerStatus:
    init, counting, paused = 1, 2, 3

class FocusStatus:
    focus, rest = 1, 2

if __name__ == "__main__":
    progress = CircularProgress()
    progress.__init__()