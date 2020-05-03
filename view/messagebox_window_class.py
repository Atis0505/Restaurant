from enum import Enum
from typing import Optional

from PyQt5.QtWidgets import QMessageBox


class MessageBoxType(Enum):
    REGULAR_INFO = 0
    ERROR = 1
    QUESTION = 2


class Messagebox(QMessageBox):

    def __init__(self):
        super().__init__()
        self.title = "RM System"
        self.setWindowTitle(self.title)

    def window_execution(self, text: str, message_type: MessageBoxType) -> Optional[bool]:
        if message_type == MessageBoxType.REGULAR_INFO:
            self.setText(text)
            self.exec_()
        elif message_type == MessageBoxType.ERROR:
            self.setIcon(QMessageBox.Critical)
            self.setText(text)
            self.exec_()
        # elif message_type == MessageBoxType.QUESTION:
        #     self.setText(text)
        #     self.setIcon(QMessageBox.Warning)
        #     self.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
        #     self.activateWindow()
        #     self.show()
        #     result = self.exec_()
        #     if result == QMessageBox.Yes:
        #         ans = True
        #     else:
        #         ans = False
        #     return ans
