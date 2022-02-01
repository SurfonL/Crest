import numpy
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

# DEFAULT PACKAGES
# ///////////////////////////////////////////////////////////////
import sys
import os

# IMPORT / GUI, SETTINGS AND WIDGETS
# ///////////////////////////////////////////////////////////////
# Packages
from app.packages.pyside_or_pyqt import * # Qt
from app.packages.widgets import * # Widgets
# GUIs
from app.uis.login.ui_login import Ui_Login # Login / Splash Screen
from app.uis.main_window.ui_main import Ui_MainWindow # MainWindow
from app.uis.chat.page_messages import Chat # Chat Widget
# Modules
import app.modules.ui_functions.functions as ui_functions
from app.modules.app_settings.settings import *

# MAIN WINDOW
# ///////////////////////////////////////////////////////////////
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        # GET WIDGETS FROM "ui_main.py"
        # Load widgets inside MainWindow
        # ///////////////////////////////////////////////////////////////
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # SET DEFAULT PAGE
        # ///////////////////////////////////////////////////////////////
        self.ui.app_pages.setCurrentWidget(self.ui.home)

        # LOAD DICT SETTINGS FROM "settings.json" FILE
        # ///////////////////////////////////////////////////////////////
        self.settings = Settings()
        
        ######################
        #variables init
        self.is_maximized = False
        
        
        # 로그인 페이지에서 엔터 누르면 넘어감
        self.ui.password.keyReleaseEvent = self.check_login

        #왼쪽 바: 아이콘, 세팅 버튼 등: TODO: 오른쪽으로 옮겨
        self.chat_button = LeftMenuButton(
            self,
            "custom_btn_top",
            "images/icons_svg/drum_sticks.svg",
            "Add new friend",
        )
        self.pomodoro_button = LeftMenuButton(
            self,
            "custom_btn_bottom_1",
            "images/icons_svg/pomodoro.png",
            "More options, test with many words",
        )
        self.custom_btn_bottom_2 = LeftMenuButton(
            self,
            "custom_btn_bottom_2",
            "images/icons_svg/icon_settings.svg",
            "Open settings",
        )
        self.ui.top_menus_layout.addWidget(self.chat_button)
        self.ui.top_menus_layout.addWidget(self.pomodoro_button)
        self.ui.bottom_menus_layout.addWidget(self.custom_btn_bottom_2)

        #left menu chat page
        self.chat_button.clicked.connect(lambda: self.ui.app_pages.setCurrentWidget(self.ui.chat))
        self.chat = Chat()
        self.ui.chat_layout.addWidget(self.chat)


        #left menu pomodoro page
        self.pomodoro_button.clicked.connect(lambda: self.ui.bg_app.setCurrentWidget(self.ui.pomodoro_appPage2))
        self.timer = CircularProgress(self)
        self.ui.clock_layout0.addWidget(self.timer)
        self.pomo_home_btn = WhiteButton(
            self,
            "pomo_home",
            "images/icons_svg/home.png",
            40,
            40
        )
        self.ui.pomo_home.addWidget(self.pomo_home_btn)
        self.pomo_home_btn.clicked.connect(lambda: self.ui.bg_app.setCurrentWidget(self.ui.bg_appPage1))
        self.pomo_play_btn = PomoButton(
            self,
            "play",
            "images/icons_svg/play.png",
            60,
            60,
        )
        self.pomo_pause_btn = PomoButton(
            self,
            "pause",
            "images/icons_svg/pause.png",
            60,
            60,
        )
        self.ui.pomo_buttons_layout.addWidget(self.pomo_play_btn, alignment=Qt.AlignCenter)
        self.ui.pomo_buttons_layout.addWidget(self.pomo_pause_btn, alignment=Qt.AlignCenter)
        self.pomo_pause_btn.hide()


        self.pomo_play_btn.clicked.connect(lambda: self.timer._start_event(int(self.ui.focus_edit.text())*60))
        self.pomo_play_btn.clicked.connect(self.hide_show)


        self.pomo_pause_btn.clicked.connect(self.timer._reset_event)
        self.pomo_pause_btn.clicked.connect(self.hide_show)


        self.ui.focus_edit.keyReleaseEvent = self.set_focus_time










        # DEBUG
        self.chat_button.clicked.connect(lambda: print(f"{self.settings['app_name']}: clicked"))
        self.chat_button.released.connect(lambda: print(f"{self.chat_button.objectName()}: released"))
        self.pomodoro_button.clicked.connect(lambda: print(f"{self.pomodoro_button.objectName()}: clicked"))
        self.pomodoro_button.released.connect(lambda: print(f"{self.pomodoro_button.objectName()}: released"))



        # SET UI DEFINITIONS
        # Run set_ui_definitions() in the ui_functions.py
        # ///////////////////////////////////////////////////////////////
        ui_functions.UiFunctions.set_ui_definitions(self)


        #Window settings
        # ///////////////////////////////////////////////////////////////

        self.maximize_minimize()
        self.setWindowFlags(Qt.FramelessWindowHint)

        # SHOW MAIN WINDOW
        # ///////////////////////////////////////////////////////////////
        self.show()

    def check_login(self, event):
        if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            password = self.ui.password.text()

            if  password == "hey":
                self.ui.password.setStyleSheet("#password:focus { border: 3px solid #bdff00; }")
                self.ui.bg_app.setCurrentIndex(1)

            else:
                # SET STYLESHEET
                self.ui.password.setStyleSheet("#password:focus { border: 3px solid rgb(255, 0, 0); }")

    # GET BTN RELEASED
    # ///////////////////////////////////////////////////////////////
    def btn_released(self):
        # GET BT CLICKED
        btn = self.sender()
        print(F"Button {btn.objectName()}, released!")


    # RESIZE EVENT
    # Whenever the window is resized, this event will be triggered
    # ///////////////////////////////////////////////////////////////
    def resizeEvent(self, event):
        ui_functions.UiFunctions.resize_grips(self)

    # MOUSE CLICK EVENTS
    # ///////////////////////////////////////////////////////////////
    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPos()

    # /////////////////////////////////////////////////////////////
    # 내가 추가한 함수들

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Shift and Qt.Key_Alt:
            self.maximize_minimize()

    # def closeEvent(self, event):
    #         event.ignore()

    def maximize_minimize(self):

        # CHANGE UI AND RESIZE GRIP
        def change_ui():
            if self.is_maximized:
                self.ui.margins_app.setContentsMargins(0, 0, 0, 0)
                self.ui.maximize_restore_app_btn.setToolTip("Restore")
                self.ui.maximize_restore_app_btn.setStyleSheet(
                    "background-image: url(:/icons_svg/images/icons_svg/icon_restore.svg);")
                self.ui.bg_app.setStyleSheet("#bg_app { border-radius: 0px; border: none; }")
                self.left_grip.hide()
                self.right_grip.hide()
                self.top_grip.hide()
                self.bottom_grip.hide()

        # CHECK EVENT
        if self.isMaximized():
            self.is_maximized = False
            self.showMinimized()
            change_ui()
        else:
            self.is_maximized = True
            self.showMaximized()
            change_ui()

    def set_focus_time(self,event):
        if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            value = int(self.ui.focus_edit.text())
            self.timer._edit_event(value)

    def hide_show(self):
        if self.timer._status == 2:
            self.pomo_play_btn.hide()
            self.pomo_pause_btn.original_icon()
            self.pomo_pause_btn.show()

        elif self.timer._status == 3 :
            self.pomo_play_btn.show()
            self.pomo_pause_btn.stop_icon()

        elif self.timer._status == 1:
            self.pomo_play_btn.show()
            self.pomo_pause_btn.hide()
            self.pomo_pause_btn.original_icon()








# SETTINGS WHEN TO START
# Set the initial class and also additional parameters of the "QApplication" class
# ///////////////////////////////////////////////////////////////
if __name__ == "__main__":
    # APPLICATION
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.ico"))
    window = MainWindow()
    sys.exit(app.exec_())