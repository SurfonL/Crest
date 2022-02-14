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
import os
from directory import BASE_DIR
import pandas as pd
import datetime
from anytree import Node, RenderTree

# IMPORT / GUI, SETTINGS AND WIDGETS
# ///////////////////////////////////////////////////////////////
# Packages
from app.packages.pyside_or_pyqt import *  # Qt
from app.packages.widgets import *  # Widgets
# GUI
from app.uis.chat.ui_page_messages import Ui_chat_page  # MainWindow
from app.uis.chat.message import Message  # MainWindow


# MAIN WINDOW
# ///////////////////////////////////////////////////////////////
class Chat(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        user_image = "images/users/Fletcher.jpg"
        user_name = "Terence Fletcher"
        user_description = ' "not quite my tempo" '
        my_name = "my_name"

        self.page = Ui_chat_page()
        self.page.setupUi(self)

        # # UPDATE INFO
        self.page.user_image.setStyleSheet(
            "#user_image { background-image: url(\"" + os.path.normpath(user_image).replace("\\", "/") + "\") }")
        self.page.user_name.setText(user_name)
        self.page.user_description.setText(user_description)

        # CHANGE PLACEHOLDER TEXT
        format_user_name = user_name.replace(" ", "_").replace("-", "_")
        format_user_name = format_user_name.lower()
        self.page.line_edit_message.setPlaceholderText(f"Message #{str(format_user_name).lower()}")

        # ENTER / RETURN PRESSED
        self.page.line_edit_message.keyReleaseEvent = self.enter_return_release

        # ENTER / RETURN PRESSED
        self.page.btn_send_message.clicked.connect(self.send_message)

        # MESSAGES
        self.messages = [
            f"Hi {my_name.capitalize()}, how are you?",
            f"Hello {my_name.capitalize()}, how are you today?",
            f"{my_name.capitalize()}, do you know if it is going to rain today?",
            f"{my_name.capitalize()}, how is your day?",
            f"{my_name.capitalize()}, do you remember that you owe me $100? Humm..."
        ]


        # self.c= ConvHelper()



        # SEND USER MESSAGE
        self.send_by_bot('t')

    # ENTER / RETURN SEND MESSAGE
    def enter_return_release(self, event):
        if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            self.send_message()

    # SEND MESSAGE
    def send_message(self):
        if self.page.line_edit_message.text() != "":
            self.my_msg = Message(self.page.line_edit_message.text(), True)
            self.page.chat_messages_layout.addWidget(self.my_msg, Qt.AlignCenter, Qt.AlignBottom)
            self.page.line_edit_message.setText("")

            # SCROLL TO END            
            QTimer.singleShot(10, lambda: self.page.messages_frame.setFixedHeight(
                self.page.chat_messages_layout.sizeHint().height()))
            QTimer.singleShot(15, lambda: self.scroll_to_end())

            # SEND USER MESSAGE
            QTimer.singleShot(300, lambda: self.send_by_bot(self.my_msg.get_message()))

    # SEND MESSAGE BY FRIEND
    def send_by_bot(self, msg):

        # out_msg = self.c.n_pomo.a
        out_msg = 'tmp'
        self.message = Message(out_msg, False)
        self.page.chat_messages_layout.addWidget(self.message, Qt.AlignCenter, Qt.AlignBottom)
        self.page.line_edit_message.setText("")

        # SCROLL TO END            
        QTimer.singleShot(10, lambda: self.page.messages_frame.setFixedHeight(
            self.page.chat_messages_layout.sizeHint().height()))
        QTimer.singleShot(15, lambda: self.scroll_to_end())

    def scroll_to_end(self):
        # SCROLL TO END
        self.scroll_bar = self.page.chat_messages.verticalScrollBar()
        self.scroll_bar.setValue(self.scroll_bar.maximum())


# r_dir = os.path.join(BASE_DIR, 'data', 'record.xlsx')
#
#
# class Conversation:
#
#     def __init__(self):
#         self.msg = 'what'
#         self.respond_list = ['n pomo', 't time']
#         self.reply = 'what'
#
#     def input_msg(self, msg):
#         if msg in self.answer_list:
#             i = self.answer_list.index(msg)
#             r = self.respond_list[i]
#
#             if r == 'n pomo':
#                 self.reply = 'a'
#
#     def print_msg(self):
#         return self.msg + self.answer_list
#
#     def n_pomo_reply(self):
#         print('w')
#
#     def n_pomo(self):
#         thresh = datetime.timedelta(minutes=20)
#         focus_t_idx = df[today_idx]['Duration'] > thresh
#         df_today_f = df[today_idx & focus_idx]
#
#
# class ConvHelper:
#     def __init__(self):
#
#         self.df = pd.read_excel(r_dir)
#         self.thresh = datetime.timedelta(minutes=20)
#
#         self.df['Duration'] = pd.to_timedelta(self.df.Duration)
#
#         self.today_idx = self.df['Date'] == pd.to_datetime('today').replace(hour=0, minute=0, second=0, microsecond=0)
#         self.yesterday_idx = self.df['Date'] == pd.to_datetime('today').replace(hour=0, minute=0, second=0, microsecond=0) - datetime.timedelta(days=1)
#
#         self.focus_idx = self.df['Pomo'] == 'focus'
#         self.rest_idx = self.df['Pomo'] == 'rest'
#         self.pause_idx = self.df['Pomo'] == 'pause'
#
#
#         self.t_idx = self.df[self.today_idx]['Duration'] > self.thresh
#         self.y_t_idx = self.df[self.yesterday_idx]['Duration'] > self.thresh
#
#         self.df_today_f = self.df[self.today_idx & self.focus_idx]
#
#         self.init = Node('init', q='what?', l_inputs=['pomos', 't pomo'], a=None)
#         self.n_pomo = Node('n_pomo', parent=self.init, a=self.h_n_pomo())
#
#
#     def h_n_pomo(self):
#         number = 'total pomos: '+ str(self.df[self.today_idx & self.t_idx & self.focus_idx]['Duration'].count()) + '\n'
#         t_time = 'total pomo_time: '+str(self.df[self.today_idx & self.focus_idx]['Duration'].sum())[7:]+ '\n'
#         t_r_time = 'total rest_time: '+str(self.df[self.today_idx & self.rest_idx]['Duration'].sum())[7:]+ '\n'
#         t_p_time = 'total pause_time: '+str(self.df[self.today_idx & self.pause_idx]['Duration'].sum())[7:]+ '\n'
#         o = number + t_time + t_r_time + t_p_time
#
#
#         self.y_t_idx = self.df[self.yesterday_idx]['Duration'] > self.thresh
#         number_y = 'total pomos yesterday: ' + str(self.df[self.yesterday_idx & self.y_t_idx & self.focus_idx]['Duration'].count()) + '\n'
#         t_time_y = 'total pomo_time yesterday: ' + str(self.df[self.yesterday_idx & self.focus_idx]['Duration'].sum())[7:] + '\n'
#         t_r_time_y = 'total rest_time yesterday: ' + str(self.df[self.yesterday_idx & self.rest_idx]['Duration'].sum())[7:] + '\n'
#         t_p_time_y = 'total pause_time yesterday: ' + str(self.df[self.yesterday_idx & self.pause_idx]['Duration'].sum())[7:] + '\n'
#         o_y = number_y + t_time_y + t_r_time_y + t_p_time_y
#
#         return o + '\n' + o_y


# if __name__ == '__main__':
#     c = ConvHelper()
#     print(c.n_pomo.a)

