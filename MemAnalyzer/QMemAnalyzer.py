import sys
from PyQt5.QtWidgets import QWidget, QApplication, QFileDialog
from PyQt5.QtCore import QDir
from widget import Ui_Widget
import memorycheck


class QMemAnalyzer(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.__ui = Ui_Widget()
        self.__ui.setupUi(self)
        self.file_path = ""
        self.__ui.lineEdit_E1ID.setText("10")
        self.__ui.lineEdit_E1Size.setText("32")
        self.__ui.lineEdit_E2ID.setText("11")
        self.__ui.lineEdit_E2Size.setText("32")
        self.__ui.lineEdit_FID.setText("12")
        self.__ui.lineEdit_FSize.setText("8")

    def on_Button_FileSelect_released(self):
        cur_dir = QDir.currentPath()
        dlgTitle = "请选择文件："
        filt = "All(*.*)"
        file_list, filt_used = QFileDialog.getOpenFileName(self, dlgTitle, cur_dir, filt)
        if len(file_list) > 0:
            file_name = file_list.split("/")[-1]
            self.__ui.lineEdit.setText(file_name)
            self.file_path = file_list

    def on_pushButton0_released(self):
        id_eeprom1 = int(self.__ui.lineEdit_E1ID.text())
        size_eeprom1 = int(self.__ui.lineEdit_E1Size.text())
        draw0 = memorycheck.Drawfigure(1, self.__ui.lineEdit.text(), id_eeprom1, size_eeprom1)
        draw0.__main__()

    def on_pushButton1_released(self):
        id_eeprom2 = int(self.__ui.lineEdit_E2ID.text())
        size_eeprom2 = int(self.__ui.lineEdit_E2Size.text())
        draw1 = memorycheck.Drawfigure(1, self.__ui.lineEdit.text(), id_eeprom2, size_eeprom2)
        draw1.__main__()

    def on_pushButton2_released(self):
        id_flash = int(self.__ui.lineEdit_FID.text())
        size_flash = int(self.__ui.lineEdit_FSize.text())
        draw2 = memorycheck.Drawfigure(2, self.__ui.lineEdit.text(), id_flash, size_flash)
        draw2.__main__()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWdget = QMemAnalyzer()
    myWdget.show()
    sys.exit(app.exec_())
