from enum import Enum
from typing import Optional

from PyQt5.QtWidgets import QMessageBox


class MessageBoxType(Enum):
    REGULAR_INFO = 0
    ERROR = 1
    NO_PERMISSION_RETRY = 2


class messagebox(QMessageBox):

    def __init__(self, text: str, message_type):
        QMessageBox.__init__(self)
        self.title = "RM System"
        self.setWindowTitle(self.title)
        self.setText(text)
        self.window_execution()

    def window_execution(self) -> Optional[bool]:
        if self.message_type == MessageBoxType.REGULAR_INFO:
            self.exec_()
        elif self.message_type == MessageBoxType.ERROR:
            self.setIcon(QMessageBox.Critical)
            self.exec_()
        elif self.message_type == MessageBoxType.NO_PERMISSION_RETRY:
            self.setIcon(QMessageBox.Warning)
            self.setStandardButtons(QMessageBox.Retry | QMessageBox.Cancel)
            return self.exec_() == QMessageBox.Retry
