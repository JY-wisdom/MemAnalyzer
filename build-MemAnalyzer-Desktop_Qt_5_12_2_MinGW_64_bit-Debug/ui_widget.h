/********************************************************************************
** Form generated from reading UI file 'widget.ui'
**
** Created by: Qt User Interface Compiler version 5.12.2
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_WIDGET_H
#define UI_WIDGET_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QGroupBox>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_Widget
{
public:
    QPushButton *Button_FileSelect;
    QLineEdit *lineEdit;
    QGroupBox *groupBox;
    QLabel *label;
    QLabel *label_2;
    QLabel *label_3;
    QLabel *label_4;
    QLabel *label_5;
    QLineEdit *lineEdit_E1ID;
    QLineEdit *lineEdit_E2ID;
    QLineEdit *lineEdit_FID;
    QLineEdit *lineEdit_E1Size;
    QLineEdit *lineEdit_E2Size;
    QLineEdit *lineEdit_FSize;
    QLabel *label_6;
    QLabel *label_7;
    QLabel *label_8;
    QPushButton *pushButton;

    void setupUi(QWidget *Widget)
    {
        if (Widget->objectName().isEmpty())
            Widget->setObjectName(QString::fromUtf8("Widget"));
        Widget->resize(400, 300);
        Button_FileSelect = new QPushButton(Widget);
        Button_FileSelect->setObjectName(QString::fromUtf8("Button_FileSelect"));
        Button_FileSelect->setGeometry(QRect(10, 10, 75, 23));
        lineEdit = new QLineEdit(Widget);
        lineEdit->setObjectName(QString::fromUtf8("lineEdit"));
        lineEdit->setGeometry(QRect(100, 10, 281, 20));
        groupBox = new QGroupBox(Widget);
        groupBox->setObjectName(QString::fromUtf8("groupBox"));
        groupBox->setGeometry(QRect(10, 40, 281, 231));
        label = new QLabel(groupBox);
        label->setObjectName(QString::fromUtf8("label"));
        label->setGeometry(QRect(10, 60, 54, 12));
        label_2 = new QLabel(groupBox);
        label_2->setObjectName(QString::fromUtf8("label_2"));
        label_2->setGeometry(QRect(10, 100, 54, 12));
        label_3 = new QLabel(groupBox);
        label_3->setObjectName(QString::fromUtf8("label_3"));
        label_3->setGeometry(QRect(10, 140, 54, 12));
        label_4 = new QLabel(groupBox);
        label_4->setObjectName(QString::fromUtf8("label_4"));
        label_4->setGeometry(QRect(80, 30, 54, 12));
        label_5 = new QLabel(groupBox);
        label_5->setObjectName(QString::fromUtf8("label_5"));
        label_5->setGeometry(QRect(160, 30, 54, 12));
        lineEdit_E1ID = new QLineEdit(groupBox);
        lineEdit_E1ID->setObjectName(QString::fromUtf8("lineEdit_E1ID"));
        lineEdit_E1ID->setGeometry(QRect(80, 60, 41, 20));
        lineEdit_E2ID = new QLineEdit(groupBox);
        lineEdit_E2ID->setObjectName(QString::fromUtf8("lineEdit_E2ID"));
        lineEdit_E2ID->setGeometry(QRect(80, 100, 41, 20));
        lineEdit_FID = new QLineEdit(groupBox);
        lineEdit_FID->setObjectName(QString::fromUtf8("lineEdit_FID"));
        lineEdit_FID->setGeometry(QRect(80, 140, 41, 20));
        lineEdit_E1Size = new QLineEdit(groupBox);
        lineEdit_E1Size->setObjectName(QString::fromUtf8("lineEdit_E1Size"));
        lineEdit_E1Size->setGeometry(QRect(160, 60, 41, 20));
        lineEdit_E2Size = new QLineEdit(groupBox);
        lineEdit_E2Size->setObjectName(QString::fromUtf8("lineEdit_E2Size"));
        lineEdit_E2Size->setGeometry(QRect(160, 100, 41, 20));
        lineEdit_FSize = new QLineEdit(groupBox);
        lineEdit_FSize->setObjectName(QString::fromUtf8("lineEdit_FSize"));
        lineEdit_FSize->setGeometry(QRect(160, 140, 41, 20));
        label_6 = new QLabel(groupBox);
        label_6->setObjectName(QString::fromUtf8("label_6"));
        label_6->setGeometry(QRect(210, 60, 54, 12));
        label_7 = new QLabel(groupBox);
        label_7->setObjectName(QString::fromUtf8("label_7"));
        label_7->setGeometry(QRect(210, 100, 54, 12));
        label_8 = new QLabel(groupBox);
        label_8->setObjectName(QString::fromUtf8("label_8"));
        label_8->setGeometry(QRect(210, 140, 54, 12));
        pushButton = new QPushButton(Widget);
        pushButton->setObjectName(QString::fromUtf8("pushButton"));
        pushButton->setGeometry(QRect(310, 190, 75, 23));

        retranslateUi(Widget);

        QMetaObject::connectSlotsByName(Widget);
    } // setupUi

    void retranslateUi(QWidget *Widget)
    {
        Widget->setWindowTitle(QApplication::translate("Widget", "MemAnalyzerV1.0", nullptr));
        Button_FileSelect->setText(QApplication::translate("Widget", "SelectFile", nullptr));
        groupBox->setTitle(QApplication::translate("Widget", "Parameters", nullptr));
        label->setText(QApplication::translate("Widget", "EEPROM1", nullptr));
        label_2->setText(QApplication::translate("Widget", "EEPROM2", nullptr));
        label_3->setText(QApplication::translate("Widget", "FLASH", nullptr));
        label_4->setText(QApplication::translate("Widget", "Chip ID", nullptr));
        label_5->setText(QApplication::translate("Widget", "ChipSize", nullptr));
        label_6->setText(QApplication::translate("Widget", "K Bytes", nullptr));
        label_7->setText(QApplication::translate("Widget", "K Bytes", nullptr));
        label_8->setText(QApplication::translate("Widget", "M Bytes", nullptr));
        pushButton->setText(QApplication::translate("Widget", "Start", nullptr));
    } // retranslateUi

};

namespace Ui {
    class Widget: public Ui_Widget {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_WIDGET_H
