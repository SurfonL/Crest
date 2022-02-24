import sys
from PySide6.QtGui import QIcon, QAction
from PySide6.QtWidgets import QMainWindow, QMenu, QApplication, QSystemTrayIcon, QFrame
from PySide6.QtCore import SIGNAL

class MyApp(QMainWindow):
    def __init__(self, parent, title):
        super().__init__(parent)
        self.exitOnClose = False
        exit = QAction(QIcon(), "Exit", self)
        self.connect(exit, SIGNAL("triggered()"), self.exitEvent)
        self.trayIcon = QSystemTrayIcon(QIcon("icon.ico"), self)
        menu = QMenu(self)
        menu.addAction(exit)
        self.trayIcon.setContextMenu(menu)
        self.connect(self.trayIcon, \
            SIGNAL("activated(QSystemTrayIcon::ActivationReason)"), \
            self.trayIconActivated)
        self.trayIcon.show()
        self.trayIcon.showMessage("MyApp is running!", "Click to open window\nRight click for menu" )

    def trayIconActivated(self, reason):
        if reason == QSystemTrayIcon.Context:
            self.trayIcon.contextMenu().show()
        elif reason == QSystemTrayIcon.Trigger:
            self.show()
            self.raise_()

    def closeEvent(self, event):
        if self.exitOnClose:
            self.trayIcon.hide()
            del self.trayIcon
            event.accept()
        else:
            self.hide()
            event.setAccepted(True)
            event.ignore()

    def exitEvent(self):
        self.exitOnClose = True
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myapp = MyApp(None, "My System Tray App")
    app.exec_()