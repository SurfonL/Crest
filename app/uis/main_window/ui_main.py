# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainMcMyCG.ui'
##
## Created by: Qt User Interface Compiler version 6.0.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from . resources_rc import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1134, 816)
        self.stylesheet = QWidget(MainWindow)
        self.stylesheet.setObjectName(u"stylesheet")
        self.stylesheet.setStyleSheet(u"/* DEFAULT */\n"
"QWidget {\n"
"	font: 9pt \"Segoe UI\";\n"
"	color: rgb(230, 230, 230);\n"
"	selection-background-color: rgb(86, 115, 0);\n"
"}\n"
"/* Bg App */\n"
"#bg_app {	\n"
"	background-color: rgb(0, 0, 0);\n"
"	border: 2px solid rgb(30, 32, 33);\n"
"}\n"
"\n"
"/* Left Menu */\n"
"#left_menu {\n"
"	border-top-left-radius: 10px;\n"
"	border-bottom-left-radius: 10px;\n"
"}\n"
"\n"
"/* Logo Top */\n"
"#logo_top {\n"
"	background-image: url(:/images_svg/images/images_svg/logo_symbol_top.svg);\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"}\n"
"\n"
"/* Buttons */\n"
"#left_menu QPushButton {\n"
"	border: none;	\n"
"	background-color: transparent;\n"
"	border-radius: 10px;\n"
"	background-repeat: none;\n"
"	background-position: center;\n"
"}\n"
"#left_menu QPushButton:hover {\n"
"	background-color: rgb(21, 22, 23);\n"
"}\n"
"#left_menu QPushButton:pressed {\n"
"	background-color: rgb(172, 229, 0);\n"
"}\n"
"#add_user_btn {	\n"
"	background-image: url(:/icons_svg/images/icons_svg/ico"
                        "n_add_user.svg);\n"
"}\n"
"#settings_btn {	\n"
"	background-image: url(:/icons_svg/images/icons_svg/icon_settings.svg);\n"
"}\n"
"\n"
"/* Left Messages */\n"
"#left_messages {\n"
"	background-color: rgb(21, 22, 23);\n"
"	border: none;\n"
"	border-left: 3px solid rgb(30, 32, 33);\n"
"}\n"
"\n"
"/* Top */\n"
"#top_messages {\n"
"	border: none;\n"
"	border-bottom: 1px solid rgb(47, 48, 50);\n"
"}\n"
"\n"
"/* Search Message */\n"
"#search_sms_frame .QLineEdit {\n"
"	border: 2px solid rgb(47, 48, 50);\n"
"	border-radius: 15px;\n"
"	background-color: rgb(47, 48, 50);\n"
"	color: rgb(121, 121, 121);\n"
"	padding-left: 30px;\n"
"	padding-right: 10px;\n"
"	background-image: url(:/icons_svg/images/icons_svg/icon_search.svg);\n"
"	background-repeat: none;\n"
"	background-position: left center;\n"
"}\n"
"#search_sms_frame .QLineEdit:hover {\n"
"	color: rgb(230, 230, 230);\n"
"	border: 2px solid rgb(62, 63, 66);\n"
"}\n"
"#search_sms_frame .QLineEdit:focus {\n"
"	color: rgb(230, 230, 230);\n"
"	border: 2px solid rgb(53, 54"
                        ", 56);\n"
"	background-color: rgb(14, 14, 15);\n"
"}\n"
"\n"
"/* Menus Scroll Area */\n"
"#left_messages_scroll, #messages_scroll {\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"/* Bottom / Signal */\n"
"#bottom_messages {	\n"
"	background-color: rgb(30, 32, 33);\n"
"}\n"
"#signal_icon { \n"
"	background-image: url(:/icons_svg/images/icons_svg/icon_signal.svg);\n"
"	background-repeat: none;\n"
"	background-position: left center;\n"
"}\n"
"#label_top{	\n"
"	font: 800 10pt \"Segoe UI\";\n"
"	color: rgb(189, 255, 0);\n"
"}\n"
"#label_bottom {	\n"
"	color: rgb(166, 166, 166);\n"
"}\n"
"\n"
"/* Right Content */\n"
"#right_content {\n"
"	border-top-right-radius: 10px;\n"
"	border-bottom-right-radius: 10px;\n"
"}\n"
"\n"
"/* Top Bar */\n"
"#top_bar {\n"
"	border-top-right-radius: 10px;\n"
"}\n"
"\n"
"/* Title Bar */\n"
"#title_bar {\n"
"	background-image: url(:/images_svg/images/images_svg/text_logo.svg);\n"
"	background-repeat: no-repeat;\n"
"	background-position: left center;\n"
"	border-left: 15px solid trans"
                        "parent;\n"
"}\n"
"\n"
"/* Top BTNs */\n"
"#top_btns {  }\n"
"#top_btns .QPushButton {	\n"
"	background-position: center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	outline: none;\n"
"	border-radius: 8px;\n"
"	text-align: left;\n"
"}\n"
"#top_btns .QPushButton:hover { background-color: rgb(21, 22, 23); }\n"
"#top_btns .QPushButton:pressed { background-color: rgb(172, 229, 0); }\n"
"#top_btns #close_app_btn:hover { background-color: rgb(255, 0, 127); }\n"
"#top_btns #close_app_btn:pressed { background-color: rgb(172, 229, 0); }\n"
"\n"
"/* Content / Pages */\n"
"#app_pages {\n"
"	background-color: transparent;\n"
"}\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ScrollBars */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 8px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(47, 48, 50);\n"
"    min-widt"
                        "h: 25px;\n"
"	border-radius: 4px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 8px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgb(47, 48"
                        ", 50);\n"
"    min-height: 25px;\n"
"	border-radius: 4px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: transparent;\n"
"     height: 10px;\n"
"    border-radius: 4px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: transparent;\n"
"    height: 10px;\n"
"    border-radius: 4px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"")
        self.margins_app = QVBoxLayout(self.stylesheet)
        self.margins_app.setSpacing(0)
        self.margins_app.setObjectName(u"margins_app")
        self.margins_app.setContentsMargins(10, 10, 10, 10)
        self.bg_app = QStackedWidget(self.stylesheet)
        self.bg_app.setObjectName(u"bg_app")
        self.bg_app.setStyleSheet(u"#bg_app { border-radius: 10px; }")
        self.bg_app.setFrameShape(QFrame.NoFrame)
        self.bg_app.setFrameShadow(QFrame.Raised)
        self.bg_app.setLineWidth(0)
        self.pomodoro_appPage2 = QWidget()
        self.pomodoro_appPage2.setObjectName(u"pomodoro_appPage2")
        self.pomodoro_appPage2.setStyleSheet(u"background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"stop:0 rgba(152, 222, 91,1), stop: 1 rgba(8, 225, 174,1))\n"
"")
        self.gridLayout = QGridLayout(self.pomodoro_appPage2)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.pomodoro_appPage2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(500, 500))
        self.frame_3.setMaximumSize(QSize(500, 500))
        self.frame_3.setStyleSheet(u"background: None")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.clock_layout0 = QVBoxLayout(self.frame_3)
        self.clock_layout0.setSpacing(0)
        self.clock_layout0.setObjectName(u"clock_layout0")
        self.clock_layout0.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.clock_layout0.setContentsMargins(0, 0, 0, 0)

        self.gridLayout.addWidget(self.frame_3, 2, 1, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)

        self.verticalSpacer_4 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)

        self.gridLayout.addItem(self.verticalSpacer_4, 1, 1, 1, 1)

        self.frame_4 = QFrame(self.pomodoro_appPage2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 60))
        self.frame_4.setStyleSheet(u"background: None")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.buttons_layout = QHBoxLayout(self.frame_4)
        self.buttons_layout.setSpacing(0)
        self.buttons_layout.setObjectName(u"buttons_layout")
        self.buttons_layout.setContentsMargins(0, 0, 0, 0)
        self.pomo_buttons_layout = QHBoxLayout()
        self.pomo_buttons_layout.setObjectName(u"pomo_buttons_layout")

        self.buttons_layout.addLayout(self.pomo_buttons_layout)


        self.gridLayout.addWidget(self.frame_4, 4, 1, 1, 1)

        self.pomo_title_bar = QFrame(self.pomodoro_appPage2)
        self.pomo_title_bar.setObjectName(u"pomo_title_bar")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pomo_title_bar.sizePolicy().hasHeightForWidth())
        self.pomo_title_bar.setSizePolicy(sizePolicy)
        self.pomo_title_bar.setMinimumSize(QSize(0, 45))
        self.pomo_title_bar.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.pomo_title_bar.setFrameShape(QFrame.StyledPanel)
        self.pomo_title_bar.setFrameShadow(QFrame.Raised)
        self.pomo_title_bar.setLineWidth(0)
        self.horizontalLayout_5 = QHBoxLayout(self.pomo_title_bar)
        self.horizontalLayout_5.setSpacing(4)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_5.setContentsMargins(0, 0, -1, 0)
        self.horizontalSpacer_5 = QSpacerItem(3000, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_5)

        self.top_btns_2 = QFrame(self.pomo_title_bar)
        self.top_btns_2.setObjectName(u"top_btns_2")
        self.top_btns_2.setEnabled(True)
        sizePolicy.setHeightForWidth(self.top_btns_2.sizePolicy().hasHeightForWidth())
        self.top_btns_2.setSizePolicy(sizePolicy)
        self.top_btns_2.setMaximumSize(QSize(100, 16777215))
        self.top_btns_2.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.top_btns_2.setFrameShape(QFrame.NoFrame)
        self.top_btns_2.setFrameShadow(QFrame.Raised)
        self.top_btns_2.setLineWidth(0)
        self.top_btn_layout_2 = QHBoxLayout(self.top_btns_2)
        self.top_btn_layout_2.setSpacing(4)
        self.top_btn_layout_2.setObjectName(u"top_btn_layout_2")
        self.top_btn_layout_2.setContentsMargins(0, 0, 0, 0)
        self.minimize_app_btn_2 = QPushButton(self.top_btns_2)
        self.minimize_app_btn_2.setObjectName(u"minimize_app_btn_2")
        self.minimize_app_btn_2.setMinimumSize(QSize(28, 28))
        self.minimize_app_btn_2.setMaximumSize(QSize(28, 28))
        palette = QPalette()
        brush = QBrush(QColor(230, 230, 230, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(255, 255, 255, 0))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush2 = QBrush(QColor(86, 115, 0, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Highlight, brush2)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Highlight, brush2)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Highlight, brush2)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
#endif
        self.minimize_app_btn_2.setPalette(palette)
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setStyleStrategy(QFont.NoAntialias)
        self.minimize_app_btn_2.setFont(font)
        self.minimize_app_btn_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.minimize_app_btn_2.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/icons_svg/images/icons_svg/icon_minimize.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.minimize_app_btn_2.setIcon(icon)
        self.minimize_app_btn_2.setIconSize(QSize(10, 10))

        self.top_btn_layout_2.addWidget(self.minimize_app_btn_2)

        self.maximize_restore_app_btn_2 = QPushButton(self.top_btns_2)
        self.maximize_restore_app_btn_2.setObjectName(u"maximize_restore_app_btn_2")
        self.maximize_restore_app_btn_2.setMinimumSize(QSize(28, 28))
        self.maximize_restore_app_btn_2.setMaximumSize(QSize(28, 28))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(9)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setStyleStrategy(QFont.PreferDefault)
        self.maximize_restore_app_btn_2.setFont(font1)
        self.maximize_restore_app_btn_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.maximize_restore_app_btn_2.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/icons_svg/images/icons_svg/icon_maximize.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon1.addFile(u":/icons_svg/images/icons_svg/icon_restore.svg", QSize(), QIcon.Normal, QIcon.On)
        self.maximize_restore_app_btn_2.setIcon(icon1)
        self.maximize_restore_app_btn_2.setIconSize(QSize(10, 10))
        self.maximize_restore_app_btn_2.setCheckable(False)
        self.maximize_restore_app_btn_2.setChecked(False)

        self.top_btn_layout_2.addWidget(self.maximize_restore_app_btn_2)

        self.close_app_btn_2 = QPushButton(self.top_btns_2)
        self.close_app_btn_2.setObjectName(u"close_app_btn_2")
        self.close_app_btn_2.setMinimumSize(QSize(28, 28))
        self.close_app_btn_2.setMaximumSize(QSize(28, 28))
        self.close_app_btn_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.close_app_btn_2.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u":/icons_svg/images/icons_svg/icon_close.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.close_app_btn_2.setIcon(icon2)
        self.close_app_btn_2.setIconSize(QSize(10, 10))

        self.top_btn_layout_2.addWidget(self.close_app_btn_2)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.top_btn_layout_2.addItem(self.horizontalSpacer_3)


        self.horizontalLayout_5.addWidget(self.top_btns_2)


        self.gridLayout.addWidget(self.pomo_title_bar, 0, 0, 1, 3, Qt.AlignRight)

        self.verticalSpacer_6 = QSpacerItem(20, 50, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_6, 3, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 2, 0, 1, 1)

        self.frame = QFrame(self.pomodoro_appPage2)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background: None")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setVerticalSpacing(0)
        self.gridLayout_2.setContentsMargins(0, 0, 9, -1)
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_4, 0, 0, 1, 1)

        self.frame_9 = QFrame(self.frame)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMinimumSize(QSize(45, 20))
        self.frame_9.setMaximumSize(QSize(45, 20))
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.rest_edit = QLineEdit(self.frame_9)
        self.rest_edit.setObjectName(u"rest_edit")
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(9)
        font2.setBold(False)
        font2.setItalic(False)
        self.rest_edit.setFont(font2)
        self.rest_edit.setCursor(QCursor(Qt.ArrowCursor))
        self.rest_edit.setMouseTracking(False)
        self.rest_edit.setStyleSheet(u"background: rgba(255,255,255,0);")
        self.rest_edit.setMaxLength(2)
        self.rest_edit.setFrame(False)
        self.rest_edit.setAlignment(Qt.AlignCenter)
        self.rest_edit.setCursorMoveStyle(Qt.LogicalMoveStyle)
        self.rest_edit.setClearButtonEnabled(False)

        self.horizontalLayout_3.addWidget(self.rest_edit)


        self.gridLayout_2.addWidget(self.frame_9, 2, 1, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_5, 3, 1, 1, 1)

        self.frame_8 = QFrame(self.frame)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMinimumSize(QSize(45, 20))
        self.frame_8.setMaximumSize(QSize(45, 20))
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.focus_edit = QLineEdit(self.frame_8)
        self.focus_edit.setObjectName(u"focus_edit")
        self.focus_edit.setCursor(QCursor(Qt.ArrowCursor))
        self.focus_edit.setMouseTracking(False)
        self.focus_edit.setStyleSheet(u"background: rgba(255,255,255,0)")
        self.focus_edit.setMaxLength(2)
        self.focus_edit.setFrame(False)
        self.focus_edit.setAlignment(Qt.AlignCenter)
        self.focus_edit.setClearButtonEnabled(False)

        self.horizontalLayout_2.addWidget(self.focus_edit)


        self.gridLayout_2.addWidget(self.frame_8, 1, 1, 1, 1)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(45, 45))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.pomo_home = QVBoxLayout(self.frame_2)
        self.pomo_home.setSpacing(0)
        self.pomo_home.setObjectName(u"pomo_home")
        self.pomo_home.setContentsMargins(0, 0, 0, 0)

        self.gridLayout_2.addWidget(self.frame_2, 0, 1, 1, 1)


        self.gridLayout.addWidget(self.frame, 1, 2, 2, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 200, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_3, 5, 1, 2, 1)

        self.frame_5 = QFrame(self.pomodoro_appPage2)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy1)
        self.frame_5.setStyleSheet(u"background: None")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, -1, -1)
        self.taskEdit = QLineEdit(self.frame_5)
        self.taskEdit.setObjectName(u"taskEdit")
        self.taskEdit.setMouseTracking(False)
        self.taskEdit.setStyleSheet(u"background: rgba(255,255,255,0);")
        self.taskEdit.setText(u"")
        self.taskEdit.setFrame(False)
        self.taskEdit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.taskEdit.setDragEnabled(True)
        self.taskEdit.setClearButtonEnabled(False)

        self.horizontalLayout_4.addWidget(self.taskEdit)


        self.gridLayout.addWidget(self.frame_5, 6, 2, 1, 1)

        self.bg_app.addWidget(self.pomodoro_appPage2)
        self.psd_appPage0 = QWidget()
        self.psd_appPage0.setObjectName(u"psd_appPage0")
        self.psd_appPage0.setEnabled(True)
        self.psd_appPage0.setStyleSheet(u"#bg {\n"
"	background-color: rgb(0, 0, 0);\n"
"	border-radius: 10px;\n"
"}\n"
"QLabel {\n"
"	color:  rgb(121, 121, 121);\n"
"	padding-left: 10px;\n"
"	padding-top: 20px;\n"
"}\n"
".QLineEdit {\n"
"	border: 3px solid rgb(47, 48, 50);\n"
"	border-radius: 15px;\n"
"	background-color: rgb(47, 48, 50);\n"
"	color: rgb(121, 121, 121);\n"
"	padding-left: 10px;\n"
"	padding-right: 10px;\n"
"	background-repeat: none;\n"
"	background-position: left center;\n"
"}\n"
".QLineEdit:hover {\n"
"	color: rgb(230, 230, 230);\n"
"	border: 3px solid rgb(62, 63, 66);\n"
"}\n"
".QLineEdit:focus {\n"
"	color: rgb(230, 230, 230);\n"
"	border: 3px solid rgb(189, 255, 0);\n"
"	background-color: rgb(14, 14, 15);\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(self.psd_appPage0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.password = QLineEdit(self.psd_appPage0)
        self.password.setObjectName(u"password")
        self.password.setMinimumSize(QSize(200, 0))
        self.password.setMaximumSize(QSize(400, 16777215))
        self.password.setLayoutDirection(Qt.LeftToRight)
        self.password.setEchoMode(QLineEdit.Password)
        self.password.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.password, 0, Qt.AlignHCenter)

        self.verticalSpacer = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.bg_app.addWidget(self.psd_appPage0)
        self.bg_appPage1 = QWidget()
        self.bg_appPage1.setObjectName(u"bg_appPage1")
        self.base_Layout = QVBoxLayout(self.bg_appPage1)
        self.base_Layout.setSpacing(0)
        self.base_Layout.setObjectName(u"base_Layout")
        self.base_Layout.setContentsMargins(0, 0, 0, 0)
        self.horizontal_Layout = QHBoxLayout()
        self.horizontal_Layout.setSpacing(0)
        self.horizontal_Layout.setObjectName(u"horizontal_Layout")
        self.left_menu = QFrame(self.bg_appPage1)
        self.left_menu.setObjectName(u"left_menu")
        self.left_menu.setMinimumSize(QSize(50, 0))
        self.left_menu.setMaximumSize(QSize(50, 16777215))
        self.left_menu.setFrameShape(QFrame.NoFrame)
        self.left_menu.setFrameShadow(QFrame.Raised)
        self.left_menu.setLineWidth(0)
        self.vertical_left_menu_layout = QVBoxLayout(self.left_menu)
        self.vertical_left_menu_layout.setSpacing(0)
        self.vertical_left_menu_layout.setObjectName(u"vertical_left_menu_layout")
        self.vertical_left_menu_layout.setContentsMargins(0, 0, 0, 0)
        self.logo_top = QLabel(self.left_menu)
        self.logo_top.setObjectName(u"logo_top")
        self.logo_top.setMinimumSize(QSize(50, 50))
        self.logo_top.setMaximumSize(QSize(50, 50))

        self.vertical_left_menu_layout.addWidget(self.logo_top)

        self.top_menus = QFrame(self.left_menu)
        self.top_menus.setObjectName(u"top_menus")
        self.top_menus.setMinimumSize(QSize(0, 50))
        self.top_menus.setFrameShape(QFrame.NoFrame)
        self.top_menus.setFrameShadow(QFrame.Raised)
        self.top_menus_layout = QVBoxLayout(self.top_menus)
        self.top_menus_layout.setSpacing(5)
        self.top_menus_layout.setObjectName(u"top_menus_layout")
        self.top_menus_layout.setContentsMargins(5, 5, 5, 5)

        self.vertical_left_menu_layout.addWidget(self.top_menus)

        self.spacer_vertical_menu = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.vertical_left_menu_layout.addItem(self.spacer_vertical_menu)

        self.bottom_menus = QFrame(self.left_menu)
        self.bottom_menus.setObjectName(u"bottom_menus")
        self.bottom_menus.setMinimumSize(QSize(0, 50))
        self.bottom_menus.setFrameShape(QFrame.NoFrame)
        self.bottom_menus.setFrameShadow(QFrame.Raised)
        self.bottom_menus_layout = QVBoxLayout(self.bottom_menus)
        self.bottom_menus_layout.setSpacing(5)
        self.bottom_menus_layout.setObjectName(u"bottom_menus_layout")
        self.bottom_menus_layout.setSizeConstraint(QLayout.SetMinAndMaxSize)
        self.bottom_menus_layout.setContentsMargins(5, 5, 5, 5)

        self.vertical_left_menu_layout.addWidget(self.bottom_menus)


        self.horizontal_Layout.addWidget(self.left_menu)

        self.right_content = QFrame(self.bg_appPage1)
        self.right_content.setObjectName(u"right_content")
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(9)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setStyleStrategy(QFont.PreferAntialias)
        self.right_content.setFont(font3)
        self.right_content.setFrameShape(QFrame.NoFrame)
        self.right_content.setFrameShadow(QFrame.Raised)
        self.right_content.setLineWidth(0)
        self.verticalLayout = QVBoxLayout(self.right_content)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.top_bar = QFrame(self.right_content)
        self.top_bar.setObjectName(u"top_bar")
        self.top_bar.setMinimumSize(QSize(0, 45))
        self.top_bar.setMaximumSize(QSize(16777215, 45))
        self.top_bar.setFrameShape(QFrame.NoFrame)
        self.top_bar.setFrameShadow(QFrame.Raised)
        self.top_bar.setLineWidth(0)
        self.horizontalLayout = QHBoxLayout(self.top_bar)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.title_bar = QLabel(self.top_bar)
        self.title_bar.setObjectName(u"title_bar")
        self.title_bar.setStyleSheet(u"ba")
        self.title_bar.setLineWidth(0)

        self.horizontalLayout.addWidget(self.title_bar)

        self.top_btns = QFrame(self.top_bar)
        self.top_btns.setObjectName(u"top_btns")
        self.top_btns.setMaximumSize(QSize(100, 16777215))
        self.top_btns.setFrameShape(QFrame.NoFrame)
        self.top_btns.setFrameShadow(QFrame.Raised)
        self.top_btns.setLineWidth(0)
        self.top_btn_layout = QHBoxLayout(self.top_btns)
        self.top_btn_layout.setSpacing(4)
        self.top_btn_layout.setObjectName(u"top_btn_layout")
        self.top_btn_layout.setContentsMargins(0, 0, 0, 0)
        self.minimize_app_btn = QPushButton(self.top_btns)
        self.minimize_app_btn.setObjectName(u"minimize_app_btn")
        self.minimize_app_btn.setMinimumSize(QSize(28, 28))
        self.minimize_app_btn.setMaximumSize(QSize(28, 28))
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Active, QPalette.Highlight, brush2)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
#endif
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Highlight, brush2)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
#endif
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Highlight, brush2)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
#endif
        self.minimize_app_btn.setPalette(palette1)
        self.minimize_app_btn.setFont(font)
        self.minimize_app_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.minimize_app_btn.setStyleSheet(u"background-image: url(:/icons_svg/images/icons_svg/icon_minimize.svg);")
        self.minimize_app_btn.setIconSize(QSize(20, 20))

        self.top_btn_layout.addWidget(self.minimize_app_btn)

        self.maximize_restore_app_btn = QPushButton(self.top_btns)
        self.maximize_restore_app_btn.setObjectName(u"maximize_restore_app_btn")
        self.maximize_restore_app_btn.setMinimumSize(QSize(28, 28))
        self.maximize_restore_app_btn.setMaximumSize(QSize(28, 28))
        self.maximize_restore_app_btn.setFont(font1)
        self.maximize_restore_app_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.maximize_restore_app_btn.setStyleSheet(u"background-image: url(:/icons_svg/images/icons_svg/icon_maximize.svg);")
        self.maximize_restore_app_btn.setIconSize(QSize(20, 20))

        self.top_btn_layout.addWidget(self.maximize_restore_app_btn)

        self.close_app_btn = QPushButton(self.top_btns)
        self.close_app_btn.setObjectName(u"close_app_btn")
        self.close_app_btn.setMinimumSize(QSize(28, 28))
        self.close_app_btn.setMaximumSize(QSize(28, 28))
        self.close_app_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.close_app_btn.setStyleSheet(u"background-image: url(:/icons_svg/images/icons_svg/icon_close.svg);")
        self.close_app_btn.setIconSize(QSize(20, 20))

        self.top_btn_layout.addWidget(self.close_app_btn)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.top_btn_layout.addItem(self.horizontalSpacer)


        self.horizontalLayout.addWidget(self.top_btns)


        self.verticalLayout.addWidget(self.top_bar)

        self.content = QFrame(self.right_content)
        self.content.setObjectName(u"content")
        self.content.setFrameShape(QFrame.NoFrame)
        self.content.setFrameShadow(QFrame.Raised)
        self.content.setLineWidth(0)
        self.verticalLayout_4 = QVBoxLayout(self.content)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.app_pages = QStackedWidget(self.content)
        self.app_pages.setObjectName(u"app_pages")
        self.app_pages.setStyleSheet(u"background-color: transparent;")
        self.home = QWidget()
        self.home.setObjectName(u"home")
        self.home.setStyleSheet(u"#home {\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"	background-image: url(:/images_svg/images/images_svg/logo_home.svg);\n"
"}")
        self.app_pages.addWidget(self.home)
        self.chat = QWidget()
        self.chat.setObjectName(u"chat")
        self.chat_layout = QVBoxLayout(self.chat)
        self.chat_layout.setSpacing(0)
        self.chat_layout.setObjectName(u"chat_layout")
        self.chat_layout.setContentsMargins(0, 0, 0, 0)
        self.app_pages.addWidget(self.chat)

        self.verticalLayout_4.addWidget(self.app_pages)


        self.verticalLayout.addWidget(self.content)


        self.horizontal_Layout.addWidget(self.right_content)


        self.base_Layout.addLayout(self.horizontal_Layout)

        self.bg_app.addWidget(self.bg_appPage1)

        self.margins_app.addWidget(self.bg_app)

        MainWindow.setCentralWidget(self.stylesheet)

        self.retranslateUi(MainWindow)

        self.app_pages.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(tooltip)
        self.minimize_app_btn_2.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.minimize_app_btn_2.setText("")
#if QT_CONFIG(tooltip)
        self.maximize_restore_app_btn_2.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.maximize_restore_app_btn_2.setText("")
#if QT_CONFIG(tooltip)
        self.close_app_btn_2.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.close_app_btn_2.setText("")
        self.rest_edit.setInputMask("")
        self.rest_edit.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.focus_edit.setInputMask("")
        self.focus_edit.setText(QCoreApplication.translate("MainWindow", u"25", None))
        self.password.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Who are you?", None))
        self.title_bar.setText("")
#if QT_CONFIG(tooltip)
        self.minimize_app_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.minimize_app_btn.setText("")
#if QT_CONFIG(tooltip)
        self.maximize_restore_app_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.maximize_restore_app_btn.setText("")
#if QT_CONFIG(tooltip)
        self.close_app_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.close_app_btn.setText("")
    # retranslateUi

