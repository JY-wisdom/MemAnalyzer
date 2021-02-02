import os
import sys

from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QApplication, QFileDialog, QVBoxLayout, QTableView, QHeaderView
from PyQt5.QtCore import QDir, QObject, pyqtSignal, pyqtSlot
from widget import Ui_Widget

class QMemAnalyzer(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.__ui = Ui_Widget()
        self.__ui.setupUi(self)
        self.file_path = ""
        self.__ui.lineEdit_E1ID.setText("11")
        self.__ui.lineEdit_E1Size.setText("32")
        self.__ui.lineEdit_E2ID.setText("12")
        self.__ui.lineEdit_E2Size.setText("32")
        self.__ui.lineEdit_FID.setText("13")
        self.__ui.lineEdit_FSize.setText("8")

    def on_Button_FileSelect_released(self):
        cur_dir = QDir.currentPath()
        dlgTitle = "请选择文件："
        filt = "All(*.*)"
        file_list,filt_used = QFileDialog.getOpenFileName(self, dlgTitle, cur_dir, filt)
        if len(file_list) > 0:
            file_name = file_list.split("/")[-1]
            self.__ui.lineEdit.setText(file_name)
            self.file_path = file_list
    def on_pushButton_released(self):
        id_eeprom1 = int(self.__ui.lineEdit_E1ID.text())
        id_eeprom2 = int(self.__ui.lineEdit_E2ID.text())
        id_flash = int(self.__ui.lineEdit_FID.text())
        size_eeprom1 = int(self.__ui.lineEdit_E1Size.text())
        size_eeprom2 = int(self.__ui.lineEdit_E2Size.text())
        size_flash = int(self.__ui.lineEdit_FSize.text())
        print("plot")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWdget = QMemAnalyzer()
    myWdget.show()
    sys.exit(app.exec_())
