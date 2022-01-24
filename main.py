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

# GLOBALS
# ///////////////////////////////////////////////////////////////
counter = 0

# LOGIN
# ///////////////////////////////////////////////////////////////

    # CHECK LOGIN
    # ///////////////////////////////////////////////////////////////


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

        # 로그인 페이지에서 엔터 누르면 넘어감
        self.ui.password.keyReleaseEvent = self.check_login

        #왼쪽 바: 아이콘, 세팅 버튼 등: TODO: 오른쪽으로 옮겨
        self.custom_btn_top = LeftMenuButton(
            self,
            "custom_btn_top",
            "images/icons_svg/icon_add_user.svg",
            "Add new friend"
        )
        self.custom_btn_bottom_1 = LeftMenuButton(
            self,
            "custom_btn_bottom_1",
            "images/icons_svg/icon_more_options.svg",
            "More options, test with many words"
        )
        self.custom_btn_bottom_2 = LeftMenuButton(
            self,
            "custom_btn_bottom_2",
            "images/icons_svg/icon_settings.svg",
            "Open settings"
        )
        self.ui.top_menus_layout.addWidget(self.custom_btn_top)
        self.ui.bottom_menus_layout.addWidget(self.custom_btn_bottom_1)
        self.ui.bottom_menus_layout.addWidget(self.custom_btn_bottom_2)



        #left menu 버튼에 기능을 추가하자!
        #TODO: chat 페이지를 하나 만드는게 더 나을 듯
        self.custom_btn_top.clicked.connect(self.sec_button_clicked)







        # DEBUG
        self.custom_btn_top.clicked.connect(lambda: print(f"{self.settings['app_name']}: clicked"))
        self.custom_btn_top.released.connect(lambda: print(f"{self.custom_btn_top.objectName()}: released"))
        self.custom_btn_bottom_1.clicked.connect(lambda: print(f"{self.custom_btn_bottom_1.objectName()}: clicked"))
        self.custom_btn_bottom_1.released.connect(lambda: print(f"{self.custom_btn_bottom_1.objectName()}: released"))

        
        # TOP USER BOX
        # Add widget to App
        # ///////////////////////////////////////////////////////////////
        self.top_user = TopUserInfo(self.ui.left_messages, 8, 64, "wanderson", "Writing python codes")
        self.top_user.setParent(self.ui.top_user_frame)
        self.top_user.status.connect(self.status_change)

        # SET UI DEFINITIONS
        # Run set_ui_definitions() in the ui_functions.py
        # ///////////////////////////////////////////////////////////////
        ui_functions.UiFunctions.set_ui_definitions(self)

        # ADD MESSAGE BTNS / FRIEND MENUS
        # Add btns to page
        # ///////////////////////////////////////////////////////////////
        add_user = [
            {
                "user_image" : "images/users/cat.png",
                "user_name" : "Tom",
                "user_description" : "Did you see a mouse?",
                "user_status" : "online",
                "unread_messages" : 2,
                "is_active" : False
            },
            {
                "user_image" : "images/users/mouse.png",
                "user_name" : "Jerry",
                "user_description" : "I think I saw a cat...",
                "user_status" : "busy",
                "unread_messages" : 1,
                "is_active" : False
            },
            {
                "user_image" : "images/users/me.png",
                "user_name" : "Me From The Future",
                "user_description" : "Lottery result...",
                "user_status" : "invisible",
                "unread_messages" : 0,
                "is_active" : False
            }
        ]
        self.menu = FriendMessageButton
        def add_menus(self, parameters):
            id = 0
            for parameter in parameters:
                
                user_image = parameter['user_image']
                user_name = parameter['user_name']
                user_description = parameter['user_description']
                user_status = parameter['user_status']
                unread_messages = parameter['unread_messages']
                is_active = parameter['is_active']
                
                self.menu = FriendMessageButton(
                    id, user_image, user_name, user_description, user_status, unread_messages, is_active
                )
                self.menu.clicked.connect(self.btn_clicked)
                self.menu.released.connect(self.btn_released)
                self.ui.messages_layout.addWidget(self.menu)
                id += 1

        add_menus(self, add_user)

        self.maximize_minimize()
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)

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


    # SET USERNAME TO MAIN WINDOW
    # ///////////////////////////////////////////////////////////////
    def set_user_and_description(self, username):
        self.top_user.user_name = username
        print(f"User: {username} are logged!")

    # PRINT STATUS
    # ///////////////////////////////////////////////////////////////
    def status_change(self, status):
        print(f"send signal: {status}")
        
    # GET BTN CLICKED
    # ///////////////////////////////////////////////////////////////
    def btn_clicked(self):
        # GET BT CLICKED
        btn = self.sender()

        # UNSELECT CHATS
        ui_functions.UiFunctions.deselect_chat_message(self, btn.objectName())

        # SELECT CLICKED
        if btn.objectName():
            btn.reset_unread_message()
            ui_functions.UiFunctions.select_chat_message(self, btn.objectName())

        # LOAD CHAT PAGE
        if btn.objectName():
            # REMOVE CHAT
            for chat in reversed(range(self.ui.chat_layout.count())):
                self.ui.chat_layout.itemAt(chat).widget().deleteLater()
            self.chat = None

            # SET CHAT WIDGET
            self.chat = Chat(btn.user_image, btn.user_name, btn.user_description, btn.objectName(), self.top_user.user_name)

            # ADD WIDGET TO LAYOUT
            self.ui.chat_layout.addWidget(self.chat)

            # JUMP TO CHAT PAGE
            self.ui.app_pages.setCurrentWidget(self.ui.chat)

        # DEBUG
        print(f"Button {btn.objectName()}, clicked!")

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


    def sec_button_clicked(self):
        # GET BT CLICKED
        btn = self.sender()

        # UNSELECT CHATS
        ui_functions.UiFunctions.deselect_chat_message(self, btn.objectName())

        # SELECT CLICKED
        if btn.objectName():
            btn.reset_unread_message()
            ui_functions.UiFunctions.select_chat_message(self, btn.objectName())

        # LOAD CHAT PAGE
        if btn.objectName():
            # REMOVE CHAT
            for chat in reversed(range(self.ui.chat_layout.count())):
                self.ui.chat_layout.itemAt(chat).widget().deleteLater()
            self.chat = None

            # SET CHAT WIDGET
            self.chat = Chat(btn.user_image, btn.user_name, btn.user_description, btn.objectName(),
                             self.top_user.user_name)

            # ADD WIDGET TO LAYOUT
            self.ui.chat_layout.addWidget(self.chat)

            # JUMP TO CHAT PAGE
            self.ui.app_pages.setCurrentWidget(self.ui.chat)

        # DEBUG
        print(f"Button {btn.objectName()}, clicked!")



    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Shift and Qt.Key_Alt:
            self.maximize_minimize()

    # def closeEvent(self, event):
    #         event.ignore()

    def maximize_minimize(self):
        global _is_maximized

        # CHANGE UI AND RESIZE GRIP
        def change_ui():
            if _is_maximized:
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
            _is_maximized = False
            self.showMinimized()
            change_ui()
        else:
            _is_maximized = True
            self.showMaximized()
            change_ui()


# SETTINGS WHEN TO START
# Set the initial class and also additional parameters of the "QApplication" class
# ///////////////////////////////////////////////////////////////
if __name__ == "__main__":
    # APPLICATION
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.ico"))
    window = MainWindow()
    sys.exit(app.exec_())