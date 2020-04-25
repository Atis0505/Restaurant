from enum import Enum
from typing import Optional

from PyQt5.QtWidgets import QMessageBox


class MessageBoxType(Enum):
    REGULAR_INFO = 0
    ERROR = 1
    QUESTION = 2


class Messagebox(QMessageBox):

    def __init__(self, text: str, message_type: MessageBoxType):
        QMessageBox.__init__(self)
        self.title = "RM System"
        self.message_type = message_type
        self.setWindowTitle(self.title)
        self.setText(text)
        self.window_execution()

    def window_execution(self) -> Optional[bool]:
        if self.message_type == MessageBoxType.REGULAR_INFO:
            self.exec_()
        elif self.message_type == MessageBoxType.ERROR:
            self.setIcon(QMessageBox.Critical)
            self.exec_()
        elif self.message_type == MessageBoxType.QUESTION:
            self.setIcon(QMessageBox.Warning)
            self.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
            return self.exec_() == QMessageBox.Yes
